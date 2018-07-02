# open-brqq
Django-made utility to crawler subtitles from Rede Globo`s project: "The Brazil That I Want"

## Get started ##

1. Install Python 3 if you don't have
2. Create a virtualenv: `virtualenv venv`
3. Activate venv
``
`cd venv/Scripts
. activate # if linux sh
activate.bat # if windows
``
4. Install requirements: `pip install -r requirements.txt`
5. Run: `python manage.py migrate`
It should create a sqlite file
6. Run: `python manage.py createsuperuser` to create admin user - follow screen instructions
7. To start the server: `python manage.py runserver 0.0.0.0:8000'

Now you whould access *http://localhost:8000* in your browser. 
Click on "Run Video Crawler* to start the crawler.
It should last about 2-5 minutes...

## Things you should know ##
- At this site: https://especiais.g1.globo.com/o-brasil-que-eu-quero/2018/videos/, we found API that links each municipalitie to a video ID. You can find this API using Chrome Developer Tools
- For each video, there is between 5-7 municipalities speech
- To get video informations we are using globo`s public API that can be catched at a video endpoint (using Chrome Dev Tools too)
- We get the subtitle that is provided by this API
- Although there is 5070 Brazilian municipalities, not all videos have subtitles

## Goals ##
- To get a municipalitie speech subtitle there is a tricky work to split - we expect someone to improve this process
- As stated before, not all videos have subtitles - another tricky job is to generate new subtitles to the videos without subtitles

## Thanks and Attributions ##
This work is part of a research at Federal University of State of Rio de Janeiro.
You can freely use this code, but you must reference this repository as well as its authors. Be sure to attach the Apache 2.0 license.
