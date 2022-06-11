from ast import arg
from audioop import reverse
from urllib import response
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from matplotlib.pyplot import cla 
from .models import Question,Choice
from django.views import View
from django.views import generic



# class Index(View):
#      def get(self,request):
#          latest_question_list=Question.objects.order_by('-pub_date')[:6]
#          return render(request,'polls/index.html',{'latest_question_list':latest_question_list})

# class Index(View):
#     model = Question
#     def get(self,request):
#         modelname=self.model._meta.object_name.lower()
#         cntxt=self.model.objects.all()
#         return render(request,'polls/index.html',{'cntxt':cntxt})
         
class Index(generic.ListView):

    template_name ='polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        '''return the last five questions'''
        return Question.objects.order_by('-pub_date')[:5]


# # Create your views here.
# def index(request):
 
#     latest_question_list=Question.objects.order_by('-pub_date')[:6]

#     return render(request,'polls/index.html',{'latest_question_list':latest_question_list})




class DetailView(generic.DetailView):
    model=Question
    template_name = 'polls/detail.html'
 
 

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)

    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':'you did not select a choice' })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return redirect('polls:results',question_id=question.id)
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def vote(request, question_id):
#     print("reponse########################",request.POST)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return redirect('polls:results',question_id=question.id)
#         # return HttpResponseRedirect(reverse('polls:results', args=(question.id)))


class ResultsView(generic.DetailView):
    model= Question
    pk_url_kwarg = 'question_id'
    template_name = 'polls/results.html'

# def results(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})