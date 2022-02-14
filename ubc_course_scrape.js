/**
 * Team 10
 * CIS*3760
 * Sprint #4
 * Feb 13, 2022
 * Description:
 *      scraper for all undergrad courses at UBC
 */

import playwright from 'playwright'
import fs from 'fs'

const browser = await playwright.chromium.launch();
const page = await browser.newPage();
await page.goto("http://www.calendar.ubc.ca/vancouver/courses.cfm?page=code");

let courses_info = [];

const course_urls = await page.$eval("table", (all_items) => {
    
    // Array of links to courses within programs
    const course_links = [];

    const links = all_items.getElementsByTagName('a');    
    
    // Pushing all links that were scraped from the 'az_sitemap' HTML DOM 
    for (let c = 0; c < links.length; c++){
        course_links.push(links[c].href);
    }

    // Returning array of links
    return course_links;
});

browser.close();


// CODE FOR GETTING ALL COURSE INFORMATION 
for(let i = 0; i < course_urls.length; i++){
    let tmp = await scrape_courses(course_urls[i]);

    tmp.forEach (course_data => {
        courses_info.push(course_data);
    });

    fs.writeFile('uvic_courses.json', JSON.stringify(courses_info), err => {if (err) throw err});
}


// CODE FOR GETTING ONE COURSE'S INFOMATION
// let tmp = await scrape_courses("http://www.calendar.ubc.ca/vancouver/courses.cfm?page=code&code=MATH");

// console.log(JSON.stringify(tmp));

/**
 * Simple function for scraping program-specific courses' web pages
 * and storing them in array of JSON objects
 * @param {*} url // url with program-specific course information 
 */
async function scrape_courses(url) {

    // Launching browser and creating page
    const browser_link = await playwright.chromium.launch();
    const page_link = await browser_link.newPage();
    
    // Accessing program-specific web page 
    await page_link.goto(url);

    
    // Accessing content within scope of HTML dom by using tag UbcMainContent
    const courses = await page_link.$eval("#UbcMainContent", (all_items) => {

        let tmp = [];

        // getting all dt (course titles) and dd (course data) components
        let tmpArr = all_items.querySelectorAll('dt, dd');


        for (let i = 0; i < tmpArr.length; i+=2){

            //Removing HTML tags 
            let remove_script = tmpArr[i].innerHTML.replace(/<script\b[^>]*>([\s\S]*?)<\/script>/gm, "");
            let remove_style = remove_script.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gm, "");
            let title_data = remove_style.replace(/(<([^>]+)>)/gi, "");

            //Removing HTML tags 
            remove_script = tmpArr[i+1].innerHTML.replace(/<script\b[^>]*>([\s\S]*?)<\/script>/gm, "");
            remove_style = remove_script.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gm, "");
            let preq = remove_style.replace(/(<([^>]+)>)/gi, "");


            let tmp_title = title_data.split(' ');
            // getting course code 
            let cc = tmp_title[0] + tmp_title[1];
            // getting credits
            let cred = tmp_title[2];

            let desc = ""

            // getting course name 
            for (let c = 3; c < tmp_title.length; c++){
                desc += tmp_title[c] + " ";
            }

            // getting prerequisites 
            let tmp_preq = preq.split("Prerequisite: ");
            let all_preq = ""; 

            // removing all unneccessary characters
            if (tmp_preq.length > 1){
                all_preq = tmp_preq[tmp_preq.length-1].replace(/[^a-zA-Z0-9~@#$^*()_+=[\]{}|\\,.?: -]/g, "");
            }else{
                all_preq = "";
            }

            // pushing course structure 
            tmp.push({ cc, cred, desc, all_preq});
        }

        return tmp;

    });

    // Closing browser
    await browser_link.close();

    return courses;
}