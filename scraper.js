/**
 * CIS*3760
 * Team 10
 * Jan 20, 2022
 * Course Web Scraper
 */

// Importing required objects
import playwright from 'playwright'
import fs from 'fs'

(async () => {
  
  // Array of JSON objects storing information for each course
  let coursesInfo = []

  // Accessing all programs offered at Guelph 
  // with their respective links in order to access all courses 
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage();
  await page.goto(
    "https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/"
  );

  const programUrls = await page.$eval(".az_sitemap", (all_items) => {
    
    // Array of links to courses within programs
    const courseLinks = [];

    const links = all_items.getElementsByTagName('a');    
    
    // Pushing all links that were scraped from the 'az_sitemap' HTML DOM 
    for (let c = 0; c < links.length; c++){
        courseLinks.push(links[c].href);
    }

    // Returning array of links
    return courseLinks;
  });

  // Iterating through links to each course's info
  programUrls.forEach( async url => {
      if (!url.includes("#") && url.length > 0){
        
        // Storing all course info objects in a temp array
        let tmp = await scrapFunc(url);
        tmp.forEach( courseObj => {
          
          // Pushing course info object to array of all courses
          coursesInfo.push(courseObj)
        });
        
        // Writing all data to JSON file
        fs.writeFile('courses.json', JSON.stringify(coursesInfo), err => {if (err) throw err});
      }
  });

  // Closing browser
  await browser.close();
})();

/**
 * Simple function for scraping program-specific courses' web pages
 * and storing them in array of JSON objects
 * @param {*} url // url with program-specific course information 
 */
async function scrapFunc(url) {
    
    // Launching browser and creating page
    const browser = await playwright.chromium.launch();
    const page = await browser.newPage();
    
    // Accessing program-specific web page 
    await page.goto(url);

    // Accessing all 'courseblock' classes 
    // 'courseblock' classes hold all information regarding each course (relative to program)
    const courses = await page.$$eval(".courseblock", (all_items) => {
      const courseInfoObjs = [];
  
      all_items.forEach((course) => {
        
        // Getting course code 
        const cc = course.querySelector(".detail-code").innerText;
        
        // Getting course title/description 
        const desc =  course.querySelector('.detail-title').innerText
        
        // Getting credit worth
        const cred = course.querySelector(".detail-hours_html").innerText;

        // Getting semesters that the course is offered in  
        const off = course.querySelector('.detail-typically_offered')?.innerText ? course.querySelector('.detail-typically_offered')?.innerText : " ";

        // getting prequisites 
        const preq = course.querySelector('.detail-prerequisite_s_')?.innerText ? course.querySelector('.detail-prerequisite_s_')?.innerText : "";
        // splitting line of prerequisites into indivdual strings  
        let tmpArr = preq.split(",");
        // removing subtitle
        tmpArr[0] = tmpArr[0].slice(17);
        // array that will store the parsed data
        let preqArr = []

        // looping through all words in prerequisites 
        for(let idx = 0; idx < tmpArr.length; idx++) {
          if(tmpArr[idx].includes(" or ") && !tmpArr[idx].includes("above")){
              // checking if prerequisite has selection
              preqArr.push({preq: tmpArr[idx], type: 'or'});
          }else if(tmpArr[idx].includes('of')){
              // assuming prerequsite is "# of "
              // e.g. "1 of CIS*1300, CIS1500, or CIS*1200"
              let tmpPreq = "";
              let tmpIdx;
              // get all 
              for (tmpIdx = idx; tmpIdx < tmpArr.length; tmpIdx++){
                  tmpPreq = tmpPreq + tmpArr[tmpIdx];
              }
              preqArr.push({preq: tmpPreq, type: 'numOf'});
              idx = tmpIdx;
          }else if (tmpArr[idx] !== "" ) {
              if(tmpArr[idx].includes("including") && !(tmpArr[idx].includes("from"))){
                  let tmpPreq = tmpArr[idx].split('including');
                  tmpPreq.forEach(req => {
                    if(req !== ""){
                        preqArr.push({preq: req, type: 'mand'});
                    }
                })
              }else if(tmpArr[idx].includes("including") && tmpArr[idx].includes("from")){
                let tmpPreq = "";
                let tmpIdx;
                // get all 
                for (tmpIdx = idx; tmpIdx < tmpArr.length; tmpIdx++){
                    tmpPreq = tmpPreq + tmpArr[tmpIdx];
                }
                idx = tmpIdx;
                preqArr.push({preq: tmpPreq, type: 'mand'});
              }else{
                  preqArr.push({preq: tmpArr[idx], type: 'mand'});
              }
              
          }
      }


        // Pushing extracted data to array of JSON objects 
        courseInfoObjs.push({ cc, cred, desc, off, preqArr});
      });
      return courseInfoObjs;
    });

  
    // Closing browser
    await browser.close();

    return courses;
  };
