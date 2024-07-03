from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.
def index(requests):
    templates_name = 'pages/index.html'
    return render(requests,template_name=templates_name)


def faq(requests):
    templates_name = 'pages/faq.html'
    return render(requests,template_name=templates_name)

def contacts(requests):
    templates_name = 'pages/contacts.html'
    return render(requests,template_name=templates_name)

# def play_with(request):
#     return render(request,template_name='play_with.html')


class Index(generic.TemplateView):
    template_name = 'pages/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'index'
        return context
    
class Faq(generic.TemplateView):
    template_name = 'pages/faq.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FAQ - Часто задаваемые вопросы'
        return context


class PlayPage(generic.TemplateView):
    template_name = 'pages/tictactoe_page.html'
    




#---------------------------------------------------------------------------------------------------#
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
# import json

# @csrf_exempt
# def save_game_result(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         player1 = User.objects.get(username=data['player1'])
#         player2 = None  # игрок2 - бот
#         winner = None
#         if data['winner']:
#             winner = player1 if data['winner'] == "X" else None

#         game = Game(player1=player1, player2=player2, winner=winner, against_bot=data['against_bot'])
#         game.save()
#         return JsonResponse({"status": "success"})
#     return JsonResponse({"status": "error"}, status=400)
