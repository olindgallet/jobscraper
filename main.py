# coding=utf-8
# Copyright (c) 2019, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import print_function
from datetime import datetime
import websites.weworkremotely as wwr
import websites.indeed as indeed
import websites.stackoverflow as so
import websites.glassdoor as gd
import pickle
import os.path
import ezsheets

def main():
    """List files in the spreadsheet"""
    #print(gd.scrape(gd.PYTHON_JOBS))
    #print(gd.scrape(gd.JAVA_JOBS))
    #print(gd.scrape(gd.JAVASCRIPT_JOBS))
    #print(gd.scrape(gd.COPYWRITING_JOBS))
    
    ss=ezsheets.Spreadsheet('putyourcodehere')
    ss.createSheet(datetime.now().strftime("%d %b, %H:%M"),0,3,rowCount=2000)
    sh = ss.sheets[0]
    sh.update(1, 1, 'Company')
    sh.update(2, 1, 'Position')
    sh.update(3, 1, 'Link')
    row = 2
    
    try:
        wwrpjobs = wwr.scrape(wwr.PROGRAMMING_JOBS)
        for wwrpjob in wwrpjobs:
            sh.update(1, row, wwrpjob[0])
            sh.update(2, row, wwrpjob[1])
            sh.update(3, row, wwrpjob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        wwrcojobs = wwr.scrape(wwr.COPYWRITING_JOBS)
        for wwrcojob in wwrcojobs:
            sh.update(1, row, wwrcojob[0])
            sh.update(2, row, wwrcojob[1])
            sh.update(3, row, wwrcojob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        wwrcnjobs = wwr.scrape(wwr.CONTRACT_JOBS)
        for wwrcnjob in wwrcnjobs:
            sh.update(1, row, wwrcnjob[0])
            sh.update(2, row, wwrcnjob[1])
            sh.update(3, row, wwrcnjob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        pytjobs = indeed.scrape(indeed.PYTHON_JOBS)
        for pytjob in pytjobs:
            sh.update(1, row, pytjob[0])
            sh.update(2, row, pytjob[1])
            sh.update(3, row, pytjob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        javajobs = indeed.scrape(indeed.JAVA_JOBS)
        for javajob in javajobs:
            sh.update(1, row, javajob[0])
            sh.update(2, row, javajob[1])
            sh.update(3, row, javajob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        jsjobs = indeed.scrape(indeed.JAVASCRIPT_JOBS)
        for jsjob in jsjobs:
            sh.update(1, row, jsjob[0])
            sh.update(2, row, jsjob[1])
            sh.update(3, row, jsjob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        cpjobs = indeed.scrape(indeed.COPYWRITER_JOBS)
        for cpjob in cpjobs:
            sh.update(1, row, cpjob[0])
            sh.update(2, row, cpjob[1])
            sh.update(3, row, cpjob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        pytjobs = so.scrape(so.PYTHON_JOBS)
        for pytjob in pytjobs:
           sh.update(1, row, pytjob[0])
           sh.update(2, row, pytjob[1])
           sh.update(3, row, pytjob[2])
           row = row + 1
    except:
        pass
    row = row + 1
    try:
        javajobs = so.scrape(so.JAVA_JOBS)
        for javajob in javajobs:
            sh.update(1, row, javajob[0])
            sh.update(2, row, javajob[1])
            sh.update(3, row, javajob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        jsjobs = so.scrape(so.JAVASCRIPT_JOBS)
        for jsjob in jsjobs:
            sh.update(1, row, jsjob[0])
            sh.update(2, row, jsjob[1])
            sh.update(3, row, jsjob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        cpyjobs = gd.scrape(gd.COPYWRITING_JOBS)
        for cpyjob in cpyjobs:
            sh.update(1, row, cpyjob[0])
            sh.update(2, row, cpyjob[1])
            sh.update(3, row, cpyjob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        javajobs = gd.scrape(gd.JAVA_JOBS)
        for javajob in javajobs:
            sh.update(1, row, javajob[0])
            sh.update(2, row, javajob[1])
            sh.update(3, row, javajob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        jsjobs = gd.scrape(gd.JAVASCRIPT_JOBS)
        for jsjob in jsjobs:
            sh.update(1, row, jsjob[0])
            sh.update(2, row, jsjob[1])
            sh.update(3, row, jsjob[2])
            row = row + 1
    except:
        pass
    row = row + 1
    try:
        pytjobs = gd.scrape(gd.PYTHON_JOBS)
        for pytjob in pytjobs:
            sh.update(1, row, pytjob[0])
            sh.update(2, row, pytjob[1])
            sh.update(3, row, pytjob[2])
            row = row + 1
    except:
        pass
    
    
if __name__ == "__main__":
    main()
