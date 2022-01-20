const playwright = require("playwright");

(async () => {
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage();
  await page.goto(
    "https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/humn/"
  );

  const books = await page.$$eval(".courseblock", (all_items) => {
    const data = [];

    all_items.forEach((book) => {

        
      const cc = book.querySelector(".detail-code").innerText;

      const desc =  book.querySelector('.detail-title').innerText

      const cred = book.querySelector(".detail-hours_html").innerText;
    
        
      const off = book.querySelector('.detail-typically_offered')?.innerText
     
      data.push({ cc, cred, desc, off });
    });
    return data;
  });
//   console.log(books);

  const divsCounts = await page.$$eval(".courseblock", (divs) => divs.length);

  console.log(divsCounts);

  await browser.close();
})();