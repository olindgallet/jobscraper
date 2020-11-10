# coding=utf-8
# 
# Scrapes the StackOverflow site and gathers job information.
#
# Author: Olin Gallet
# Date: 25 Oct 2020
from bs4 import BeautifulSoup
import requests
import re

#: Remote Python Jobs URL
PYTHON_JOBS = 'https://stackoverflow.com/jobs?q=python+developer&r=true&sort=p'
#: Remote Java Jobs URL
JAVA_JOBS = 'https://stackoverflow.com/jobs?q=java+developer&r=true&sort=p'
#: Remote Javascript Jobs URL
JAVASCRIPT_JOBS = 'https://stackoverflow.com/jobs?q=javascript+developer&r=true&sort=p'

def scrape(url):
    """
    Go to the specified so URL and scrape it.
    """
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    divs = soup.findAll('div',{'class':'-job'})
    jobs = []
    for div in divs:
        link = div.find('h2').find('a')
        job_title = link.string
        job_company = re.sub('', '', div.find('h3').find('span').string).strip()
        job_link = 'https://stackoverflow.com'+link.get('href')
        jobs.append([job_company, job_title, job_link])
    return jobs
