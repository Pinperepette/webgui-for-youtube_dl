#!/usr/bin/python 
#-*- coding: utf-8 -*-from flask import Flask

from flask import render_template
from flask import request
import youtube_dl

app = Flask(__name__)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

@app.route("/", methods=['GET', 'POST'])
def calculation():
    result = 0
    error = ''

    if request.method=='POST':
        url = request.form['first']
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            error = 'fatto'
            #per ora metto questo, poi farò un controllo per vedere se hanno inserito l'url e cazzi e mazzi
    return render_template('pinpegui.html',error=error)

if __name__ == "__main__":
    app.run()
