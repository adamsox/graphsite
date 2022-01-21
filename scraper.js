/**
 * CIS*3760
 * Team 10
 * Jan 20, 2022
 * Course Web Scraper
 */

import playwright from 'playwright'
import fs from 'fs'

(async () => {
  // array for all courses
  let allData = []

  // accessing all programs offered at Guelph 
  // with their respective links to access all courses 
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage();
  await page.goto(
    "https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/"
  );

  const programUrls = await page.$eval(".az_sitemap", (all_items) => {
    const data = [];

    const links = all_items.getElementsByTagName('a');    
    // pushing all links that were scraped from the 'az_sitemap' html dom 
    for (let c = 0; c < links.length; c++){
        data.push(links[c].href);
    }

    // returning array of links
    return data;
  });

  // iterating thro
  programUrls.forEach( async url => {
      if (!url.includes("#") && url.length > 0){
        // getting all courses in tmp array
        let tmp = await scrapFunc(url);
        tmp.forEach( courseObj => {
          // pushing program specific courses to all courses array
          allData.push(courseObj)
        });
        
        // writing all data out to JSON file
        fs.writeFile('courses.json', JSON.stringify(allData), err => {if (err) throw err});
      }
  });

  // closing browser
  await browser.close();
})();

/**
 * simple function for scraping program specific courses web page
 * and storing them in array of JSON objects 
 * @param {*} url // url with program specific course information 
 */
async function scrapFunc(url) {
    // launching browser and creating page
    const browser = await playwright.chromium.launch();
    const page = await browser.newPage();
    // going to program specific web page 
    await page.goto(url);

    // accessing all 'courseblock' classes 
    // they hold all information regarding each course (relative to program)
    const courses = await page.$$eval(".courseblock", (all_items) => {
      const data = [];
  
      all_items.forEach((course) => {
        // getting course code 
        const cc = course.querySelector(".detail-code").innerText;
        // getting course title/description 
        const desc =  course.querySelector('.detail-title').innerText
        // getting credit worth
        const cred = course.querySelector(".detail-hours_html").innerText;
        // getting offered courses  
        const off = course.querySelector('.detail-typically_offered')?.innerText;

        // pushing extracted data to array of JSON objects 
        data.push({ cc, cred, desc, off });
      });
      return data;
    });

    
    // const divsCounts = await page.$$eval(".courseblock", (divs) => divs.length);

    // closing browser
    await browser.close();

    return courses;
  };