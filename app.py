from flask import Flask, render_template
import requests, re
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

        # Define the URL to scrape
        url = "https://www.gadgets360.com/news"
        # Perform the HTTP request to get the web page content
        req = requests.get(url)
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(req.content, "html.parser")

        outerdata = soup.find_all("div", class_="caption_box", limit=5)
        finalnews = ""
        for data in outerdata:
            news = data.a.span.text
            finalnews += f"\u2022 {news}\n"
        
        date_line = soup.find("div", class_="dateline").text
        pattern = r"\d{1,2}\s\w+\s\d{4}"
        match = re.search(pattern, date_line)
        if match:
            date = match.group()
        else:
            date = ""    

        return render_template("index.html", News=finalnews, Date = date)

