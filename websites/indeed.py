# coding=utf-8
# 
# Scrapes the Indeed site and gathers job information.
#
# Author: Olin Gallet
# Date: 25 Oct 2020
from bs4 import BeautifulSoup
import requests
import re

#: Remote Python Jobs URL
PYTHON_JOBS = 'https://www.indeed.com/jobs?q=python+developer&l=remote&explvl=entry_level&sort=date&limit=50&fromage=1'
#: Remote Java Jobs URL
JAVA_JOBS = 'https://www.indeed.com/jobs?q=java+developer&l=remote&rbl=Remote&jlid=aaa2b906602aa8f5&explvl=entry_level&sort=date&fromage=1'
#: Remote Javascript Jobs URL
JAVASCRIPT_JOBS = 'https://www.indeed.com/jobs?q=javascript+developer&l=remote&rbl=Remote&jlid=aaa2b906602aa8f5&explvl=entry_level&sort=date&fromage=1'
#: Remote Copywriter Jobs URL
COPYWRITER_JOBS = 'https://www.indeed.com/jobs?q=copywriter&l=remote&explvl=entry_level&sort=date&fromage=1'

def scrape(url):
    """
    Go to the specified Indeed site and scrape it.
    """
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    divs = soup.findAll('div',{'id':re.compile(r'^p_')})
    jobs = []
    for div in divs:
        job_company = div.find('span', {'class': 'company'}).string
        midlink = div.find('a', {'class': 'jobtitle'})
        job_title = midlink.get('title')
        job_link = 'https://www.indeed.com' + midlink.get('href')
        if not job_company:
            job_company = div.find('a', {'data-tn-element':'companyName'})
            if job_company:
                job_company = re.sub('\n', '', job_company.string)
            else:
                job_company = "Unknown Employer"
        job_company = re.sub('\n', '', job_company)
        jobs.append([job_company, job_title, job_link])
    return jobs
