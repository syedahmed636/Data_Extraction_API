import urllib.request
import json
import sqlite3
conn = sqlite3.connect('data.db')
curr = conn.cursor()
curr.execute("""create table flickzee(
                Popularity text,
                Vote_Count text,
                Video text,
                ID text,
                Adult text,
                Original_Language text,
                Original_Title text,
                Title text,
                Vote_Average text,
                Release_Date text
                )""")
for i in range(1,9,1):
    url = 'https://api.themoviedb.org/3/movie/upcoming?api_key=ca5ab1db8be0addcaf291b958ef760e0&page={}'.format(i)
    json_obj = urllib.request.urlopen(url)
    data = json.load(json_obj)
    for data in data['results']:
        curr.execute("""insert into flickzee values(?,?,?,?,?,?,?,?,?,?)""",(
            data['popularity'],
            data['vote_count'],
            data['video'],
            data['id'],
            data['adult'],
            data['original_language'],
            data['original_title'],
            data['title'],
            data['vote_average'],
            data['release_date']
        ))
        conn.commit()
conn.close()


