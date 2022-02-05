import playwright from 'playwright'
import fs from 'fs'

process.setMaxListeners(0);

const browser = await playwright.chromium.launch();
const page = await browser.newPage();
await page.goto("https://calendar.uoguelph.ca/undergraduate-calendar/degree-programs/");

let all_programs_data = []

const degree_urls = await page.$eval(".page_content", all_items => {

    const links = all_items.getElementsByTagName('a'); 

    // Array of links to courses within programs
    const degree_links = [];

    // Pushing all links that were scraped from the 'page_content' HTML DOM 
    for (let c = 0; c < links.length; c++){
        degree_links.push(links[c].href);
    }

    return degree_links;
});

await browser.close();


// Iterating through links to each degree
degree_urls.forEach(async (url) => {
    if (!url.includes("#") && url.length > 0) {
        // scraping program links from degree page 
        let program_urls = await scrape_program_links(url);
        // if programs exist 
        if (program_urls !== null){
            program_urls.forEach( async program_url => {
                // scraping requirements from program data
                let tmp_data = await scrape_programs(program_url);
                all_programs_data.push(tmp_data);
                // writing out updated data to JSON file 
                fs.writeFile("programs.json", JSON.stringify(all_programs_data), err => {if (err) throw err});
            });
        }
    }
});


/**
 * scrapes all program/requirement urls
 * @param {*} url | represents degree url e.g. BCOMP
 * @returns array of links to programs
 */
async function scrape_program_links(url) {
    const browser_links = await playwright.chromium.launch();
    const page_links = await browser_links.newPage();
    await page_links.goto(url);

    // checking if degree has programs 
    let program_exist = await page_links?.$$("#programstexttab");

    if (program_exist.length > 0){
        const program_urls = await page_links.$eval(".sitemap", all_items => {

            const links = all_items.getElementsByTagName('a'); 

            // Array of links to courses within programs
            const program_links = [];

            // Pushing all links that were scraped from the 'sitemap' HTML DOM 
            for (let c = 0; c < links.length; c++){
                program_links.push(links[c].href);
            }

            return program_links;
        });

        await browser_links.close();

        return program_urls;
    }
    
    await browser_links.close();

    return null;

}

/**
 * scrapes required courses for a program
 * @param {*} url | represents program url e.g. Software Engineering (SENG) 
 * @returns JSON of all required courses for a program
 */
async function scrape_programs(url) {
    const browser_program = await playwright.chromium.launch();
    const page_program = await browser_program.newPage();
    await page_program.goto(url);

    const program_name = await page_program.$eval(".page-title", all_items => {
        return all_items.innerHTML;
    });

    let courses = "";

    // manually collected all special cases 
    let special_cases = [" Co-op ", "Hospitality and Tourism Management (HTM)", "Family and Child Studies (FCS)",
        "Culture and Technology Studies (CTS)", "Philosophy (PHIL)", "Sociology (SOC)", "Food and Agricultural Business (FAB)", 
        "Marketing Management (MKMN)", "Real Estate (RE)", "Sport and Event Management (SPMT)", "Management (MGMT)", "Accounting (ACCT)",
        "Government, Economics and Management (GEM)", "Hospitality and Tourism Management (HTM)", "Management Economics and Finance (MEF)",
        "Food, Agricultural and Resource Economics (FARE)", "Studio Art (SART)"];

    // if program is standard for scraping (only has one table)
    if (!special_cases.includes(program_name) && !program_name.includes("Co-op")){
        courses = await page_program.$eval(".sc_courselist", all_items => {

            const courses_html = all_items.getElementsByClassName('codecol');
            const cred_requirements = all_items.getElementsByClassName('courselistcomment'); 

            // Array of all required courses within respective program
            const courses_arr = [];

            // Pushing all links that were scraped from the 'az_sitemap' HTML DOM 
            for (let c = 0; c < courses_html.length; c++){
                courses_arr.push(courses_html[c].innerText);
            }

            // Pushing all links that were scraped from the 'az_sitemap' HTML DOM 
            for (let c = 0; c < cred_requirements.length; c++){
                if(!cred_requirements[c].innerText.includes("Semester")){
                    courses_arr.push(cred_requirements[c].innerText);
                }
            }

            return courses_arr;
        });
    // else for special cases/programs with multiple tables 
    } else { 
        courses = await page_program.$$eval(".sc_courselist", all_items => {

            // Array of all required courses within respective program
            const courses_arr = [];

            // going through all tables on page 
            for(let i = 0; i  < all_items.length; i++){
                const courses_html = all_items[i].getElementsByClassName('codecol');
                const cred_requirements = all_items[i].getElementsByClassName('courselistcomment'); 

                // Pushing all courses that were scraped from the 'sc_courselist' HTML DOM 
                for (let c = 0; c < courses_html.length; c++){
                    courses_arr.push(courses_html[c].innerText);
                }

                // Pushing all data that was scraped from the 'sc_courselist' HTML DOM 
                for (let c = 0; c < cred_requirements.length; c++){
                    let tmp_data = cred_requirements[c].innerText;
                    if(tmp_data.includes("*") || tmp_data.includes("electives") || tmp_data.includes("credits")){
                        courses_arr.push(cred_requirements[c].innerText);
                    }
                }
            }

            return courses_arr;
        });
    }

    await browser_program.close();

    // returning structured JSON struct 
    return {url: url, program: program_name, reqs: courses};
}
