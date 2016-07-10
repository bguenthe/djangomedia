from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

import json
import psycopg2
import django_tables2 as tables
import spotipy

class NameTable(tables.Table):
    id = tables.Column()
    mediatype = tables.Column()
    rating = tables.Column()
    new = tables.Column()
    autor = tables.Column()
    class Meta:
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
    
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def getallmedia(request):
    con = psycopg2.connect(database='bguenthe', user='postgres', password='!eddefiu05$')
    cur = con.cursor()

    li = []
    cur.execute("select * from media")
    rows = cur.fetchall()
    i = 0
    for row in rows:
        data = {'id': row[0], 'mediatype': row[1], 'rating': row[2], 'new': row[3], 'autor': row[4], 'lend': row[5], 'private': row[6], 'title': row[7], 'modified': row[8], 'created_date': row[9], 'last_modified_date': row[10], 'deleted_date': row[11], 'comment': row[12]}
        li = li + [data]
        i += 1
#        if i == 3:
#            break

    ret = json.dumps(li)

    template = loader.get_template('media/getallmedia.html')
    context = RequestContext(request, {
        'li': li,
    })
    return HttpResponse(template.render(context))

def getallmedia_dt2(request):
    con = psycopg2.connect(database='bguenthe', user='postgres', password='!eddefiu05$')
    cur = con.cursor()

    cur.execute("select * from media")
    rows = cur.fetchall()
    
    data = []
    for row in rows:
        data.append({'id': row[0], 'mediatype': row[1], 'rating': row[2], 'new': row[3], 'autor': row[4], 'lend': row[5], 'private': row[6], 'title': row[7], 'modified': row[8], 'created_date': row[9], 'last_modified_date': row[10], 'deleted_date': row[11], 'comment': row[12]})

    table = NameTable(data)
    table.paginate(page=request.GET.get('page', 1), per_page=25)
    return render(request, "media/getallmedia_dt2.html", {"media": table})


def getspotify(request):
    scope = 'user-library-read'
    token = spotipy.util.prompt_for_user_token("bernd.stuebe@gmail.com", scope, "7644fa55dadc474d81ab5062c79535f7", "05c25aa91fb744c599c507cc2dcd5d9c")

    spotify = spotipy.Spotify(auth=token)

    results = spotify.current_user_followed_artists(limit=20, after=None)

    return render(request, "media/getallmedia_dt2.html", {"media": table})

