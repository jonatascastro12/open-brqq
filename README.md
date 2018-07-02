# open-brqq
Django-made utility to crawler subtitles from Rede Globo's project: "The Brazil That I Want"

## Get started ##
1. Install Python 3 if you don't have
2. Open prompt and create a virtualenv: `virtualenv venv`
3. Activate virtualenv
```
cd venv/Scripts
. activate # if linux sh
activate.bat # if windows
```
4. Install requirements: `pip install -r requirements.txt`
5. Run: `python manage.py migrate`
It should create a sqlite file
6. Run: `python manage.py createsuperuser` to create admin user - follow screen instructions
7. To start the server: `python manage.py runserver 0.0.0.0:8000`

Now you can access *http://localhost:8000* in your browser. 
Click on "Run Video Crawler" button to start the crawler.
It should last about 2-5 minutes...
You can see all data at *http://localhost:8000/admin*. Use the credentials that you created at step 6.
You can also access sqlite database directly, so that, you can make SQL queries to data. Refer to https://sqlitebrowser.org/.

## Things you should know ##
- At this site: https://especiais.g1.globo.com/o-brasil-que-eu-quero/2018/videos/, we found API that links each municipality to a video ID. You can find this API using Chrome Developer Tools
- For each video, there is between 5-7 municipalities speech
- To get video informations we are using globo's public API that can be catched at a video endpoint (the API was found using Chrome Dev Tools too)
- We get the subtitle that is provided by this API
- Although there is 5070 Brazilian municipalities, not all videos have subtitles

## Goals ##
- To get a municipality subtitle there is a tricky job to split a video's subtitle that contains 5-7 municipality - we expect someone to improve this process
- As stated before, not all videos have subtitles - another tricky job is to generate new subtitles to the videos without subtitles

## Thanks and Attributions ##
This work is part of a research at Federal University of State of Rio de Janeiro.
You can freely use this code, but you must reference this repository as well as its authors. Be sure to attach the Apache 2.0 license.
