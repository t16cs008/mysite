from django.http import HttpResponseRedirect
#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
#from django.template import loader
from django.views import generic
from .models import Choice, Question


# Create your views here.

class IndexView(generic.ListView):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'polls/index.html', context)
    template_name = 'polls/index.html'
    context_object_name = 'latest_qustion_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s."% question_id)
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question}

                  
class ResultsView(generic.DetailView):
    #response = "You're lookng at the results of question %s."
    #return HttpResponse(response % question_id)
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/results.html', {'question': question})
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
         return render(request, 'polls/detail.html',{
             'question': question,
             'error_massage': "You didn't select a choice.",
     })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
        
    #return HttpResponse("You're voting on question %s." % question_id)



