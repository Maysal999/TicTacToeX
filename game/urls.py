from django.contrib import admin
from django.urls import path
from game.views import (
                        Index,
                        Faq,
                        PlayPage,
                        contacts
                        # save_game_result,
                        # Play
                        )

urlpatterns = [
    path('contact/',contacts,name='contact'),
    path('',Index.as_view(),name='index'),
    path('faq',Faq.as_view(),name='faq'),
    path('tictactoe/',PlayPage.as_view(),name='tictactoe'),
]