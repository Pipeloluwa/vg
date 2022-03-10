from django.urls import path
from django import urls
from . import views

urlpatterns= [
    path("vista-gora/", views.index, name="index"),
    path("vista-gora/error-404", views.error404, name="error404"),

    path("vista-gora/audio-tracks/next-page/<int:nmbr>", views.npage, name="npage"),
    path("vista-gora/audio-tracks/previous-page/<int:nmbr>", views.ppage, name="ppage"),

    path("vista-gora/videos/next-page/<int:nmbr>", views.vnpage, name="vnpage"),
    path("vista-gora/videos/previous-page/<int:nmbr>", views.vppage, name="vppage"),

    path("vista-gora/artistes/next-page/<int:nmbr>", views.anpage, name="anpage"),
    path("vista-gora/artistes/previous-page/<int:nmbr>", views.appage, name="appage"),

    path("vista-gora/about", views.about, name="about"),
    path("vista-gora/recording", views.recording, name="recording"),
    path("vista-gora/home-recording", views.home_recording, name="home-recording"),
    path("vista-gora/rehearsal", views.rehearsal, name="rehearsal"),
    path("vista-gora/mini-sound-set", views.mini, name="mini"),
    path("vista-gora/half-sound-set", views.half, name="half"),
    path("vista-gora/full-sound-set", views.full, name="full"),
    path("vista-gora/mega-sound-set", views.mega, name="mega"),
    path("vista-gora/music-school", views.music, name="music"),
    path("vista-gora/news-and-articles", views.news, name="news"),
    path("vista-gora/audio-tracks", views.audio, name="audio"),
    path("vista-gora/videos", views.video, name="video"),
    path("vista-gora/artistes", views.artiste, name="artiste"),

    path("vista-gora/contact", views.contact, name="contact"),


    path("vista-gora/search-course11/<str:tok>", views.search_course11, name="search_course11"),
    path("vista-gora/search-course111/<str:tok>", views.search_course111, name="search_course111"),
    path("vista-gora/search-course1111/<str:tok>", views.search_course1111, name="search_course1111"),

]


