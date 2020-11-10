# coding=utf-8
# 
# Scrapes the Glassdoor site and gathers job information.
#
# Author: Olin Gallet
# Date: 25 Oct 2020
from bs4 import BeautifulSoup
import requests
import re
import cfscrape

#: Remote Python Jobs URL
PYTHON_JOBS = 'https://www.glassdoor.com/Job/remote-python-developer-jobs-SRCH_IL.0,6_IS11047_KO7,23.htm?fromAge=3'
#: Remote Java Jobs URL
JAVA_JOBS = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=Java&sc.keyword=Java+Developer&locT=S&locId=11047&jobType='
#: Remote Javascript Jobs URL
JAVASCRIPT_JOBS = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=Java&sc.keyword=Javascript+Developer&locT=S&locId=11047&jobType='
#: Remote Copywriting Jobs URL
COPYWRITING_JOBS = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=Java&sc.keyword=Copywriter&locT=S&locId=11047&jobType='

def scrape(url):
    """
    Go to the specified Glassdoor URL and scrape it.
    """
    scraper = cfscrape.create_scraper()
    html_text = scraper.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    divs = soup.findAll('script')
    jobs = []
    for div in divs:
        links = []
        if div.string and '@type' in div.string:
            parts = div.string.split(' ')
            for part in parts:
                if 'https://www.glassdoor.com/job-listing/' in part:
                    part = part.replace('"', '')
                    jobs.append(['N/A', 'N/A', part.strip()])  
    return jobs
