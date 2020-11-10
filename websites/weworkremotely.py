# coding=utf-8
# 
# Scrapes the WeWorkRemotely site and gathers job information.
#
# Author: Olin Gallet
# Date: 25 Oct 2020
from bs4 import BeautifulSoup
import requests
import re
from datetime import date

#: Remote Programming Jobs URL
PROGRAMMING_JOBS = 'https://weworkremotely.com/categories/remote-programming-jobs'
#: Copywriting Programming Jobs URL
COPYWRITING_JOBS = 'https://weworkremotely.com/categories/remote-copywriting-jobs'
#: Contract Jobs URL
CONTRACT_JOBS = 'https://weworkremotely.com/remote-contract-jobs'

def scrape(url):
    """
    Go to the specified wwr url and scrape it.
    """
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    links = soup.findAll('a')
    jobs = []
    for link in links:
        if link.get('href') and '/remote-jobs/' in link.get('href') and not link.get('href').endswith('/remote-jobs/new'):
            job_date = link.find('time')
            if job_date and job_date.string == date.today().strftime('%b %d'):
                job_title = link.find('span', {'class': 'title'}).string
                job_company = link.find('span', {'class': 'company'}).string
                job_link = 'https://weworkremotely.com' + link.get('href')
                jobs.append([job_company, job_title, job_link])
    return jobs
