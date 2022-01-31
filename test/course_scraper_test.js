// Importing required objects
import playwright from 'playwright'
import fs from 'fs'

// Launching browser and creating page
const browser = await playwright.chromium.launch();
const page = await browser.newPage();

// Accessing program-specific web page 
await page.goto('https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/math/');

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
        const off = course.querySelector('.detail-typically_offered')?.innerText ? course.querySelector('.detail-typically_offered')?.innerText : "";

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
          if(tmpArr[idx].toLowerCase().includes(" or ") && !tmpArr[idx].toLowerCase().includes("above")){
              // checking if prerequisite has selection
              preqArr.push(JSON.stringify({preq: tmpArr[idx], type: 'or'}));
          }else if(tmpArr[idx].toLowerCase().includes('of')){
              // assuming prerequsite is "# of "
              // e.g. "1 of CIS*1300, CIS1500, or CIS*1200"
              let tmpPreq = "";
              let tmpIdx;
              // get all 
              for (tmpIdx = idx; tmpIdx < tmpArr.length; tmpIdx++){
                  tmpPreq = tmpPreq + tmpArr[tmpIdx];
              }
              preqArr.push(JSON.stringify({preq: tmpPreq, type: 'numOf'}));
              idx = tmpIdx;
          }else if (tmpArr[idx] !== "" ) {
              if(tmpArr[idx].toLowerCase().includes("including") && !(tmpArr[idx].toLowerCase().includes("from"))){
                  let tmpPreq = tmpArr[idx].split('including');
                  tmpPreq.forEach(req => {
                    if(req !== ""){
                        preqArr.push(JSON.stringify({preq: req, type: 'mand'}));
                    }
                })
              }else if(tmpArr[idx].toLowerCase().includes("including") && tmpArr[idx].toLowerCase().includes("from")){
                let tmpPreq = "";
                let tmpIdx;
                // get all 
                for (tmpIdx = idx; tmpIdx < tmpArr.length; tmpIdx++){
                    tmpPreq = tmpPreq + tmpArr[tmpIdx];
                }
                idx = tmpIdx;
                preqArr.push(JSON.stringify({preq: tmpPreq, type: 'mand'}));
              }else if(tmpArr[idx].toLowerCase().includes("recommended")){
                preqArr.push(JSON.stringify({preq: tmpArr[idx], type: 'rec'}));
              }else{
                  preqArr.push(JSON.stringify({preq: tmpArr[idx], type: 'mand'}));
              }
              
          }
      }
        //     let preqCourse = {};
        //     // initializing prerequisite course 
        //     preqCourse.preq = tmpArr[idx].replace(/[\(\)]/g, "");
        //     if(tmpArr[idx].includes('4U')){
        //         preqCourse.preq = tmpArr[idx].replace(/[\(\)]/g, "") + tmpArr[idx+1];
        //     // determining whether prerequisite is manditory course, replacable course or credit requirement
        //     }else if(isNaN(tmpArr[idx]) && tmpArr[idx].includes("*")){
        //         if(tmpArr[idx+1] === 'or'){
        //             preqCourse.type = 'or';
        //             preqCourse.preq = tmpArr[idx] + " " + tmpArr[idx+1] + " " + tmpArr[idx+2]
        //             idx = idx+2;
        //             preqArr.push(JSON.stringify(preqCourse));
        //         }else{
        //             preqCourse.type = 'mand';
        //             preqArr.push(JSON.stringify(preqCourse));
        //         }
        //     }else if (!isNaN(tmpArr[idx]) && tmpArr[idx].length > 0){
        //         preqCourse.type = 'cred';
        //         preqCourse.preq = tmpArr[idx] + " credits";
        //         preqArr.push(JSON.stringify(preqCourse));
        //     }
        // }

        // Pushing extracted data to array of JSON objects 
        courseInfoObjs.push({ cc, cred, desc, off, preqArr});
    });

    return courseInfoObjs;
});

console.log(courses);

// Closing browser
await browser.close();

// return courses;