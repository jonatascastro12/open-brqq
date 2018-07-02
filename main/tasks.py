from collections import Counter

import os
from celery import shared_task
import json
import requests
import re

from main.models import City, GloboVideo
# Imports the Google Cloud client library


# @shared_task(bind=True, name='Video crawler')
def run_crawler(self):
    response = requests.get('https://especiais.g1.globo.com/o-brasil-que-eu-quero/2018/videos/js/data.json')

    data = response.json()

    i = 0
    municipios = data.get('municipios')
    for mun in municipios:
        i = i + 1

        # self.update_state(state='PROGRESS',
        #                   meta={'current': i, 'total': len(municipios)})

        city = City.objects.get_or_create(name=mun.get('municipio'), uf=mun.get('estado'))[0]

        if (mun.get('video')):
            try:
                if not city.video:

                    video = GloboVideo.objects.filter(globo_id=mun.get('video')).first()

                    if video:
                        city.video = video
                        city.save()
                        continue

                    response2 = requests.get(
                        'https://api.globovideos.com/videos/%s/playlist/callback/wmPlayerPlaylistLoaded%s' % (
                            mun.get('video'), mun.get('video')))
                    videoInfo = response2.text

                    result = re.search('wmPlayerPlaylistLoaded[0-9]+\((.+)\)\;', videoInfo)
                    videoInfo = result.group(1)
                    videoInfo = json.loads(videoInfo).get('videos')[0]

                    video = GloboVideo.objects.create(title=videoInfo.get('title'),
                                                      globo_id=videoInfo.get('id'),
                                                      video_info=json.dumps(videoInfo),
                                                      description=videoInfo.get('description'),
                                                      exhibited_at=videoInfo.get('exhibited_at'),
                                                      )

                    city.video = video
                    city.save()

                    subtitles = [r for r in videoInfo.get('resources') if r.get('type') == 'subtitle']

                    if len(subtitles) > 0 and subtitles[0].get('url'):
                        sub_url = subtitles[0].get('url')
                        video.subtitle_url = sub_url
                        response3 = requests.get(sub_url)

                        video.subtitle_content = response3.content.decode('utf8')

                        video.save()
            except Exception:
                print('error', mun.get('video'))


