// Importing required objects
import playwright from 'playwright'
import fs from 'fs'

  // Array of JSON objects storing information for each course
  let coursesInfo = []
  let validLinks = []

  // Accessing all programs offered at Guelph 
  // with their respective links in order to access all courses 
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage();
  await page.goto("https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/");

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
    // Closing browser
    await browser.close(); 

  // // Iterating through links to each course's info
  programUrls.forEach( async url => {
      if (!url.includes("#") && url.length > 0){
        console.log(url);
        // validLinks.push(url);
      }
  });