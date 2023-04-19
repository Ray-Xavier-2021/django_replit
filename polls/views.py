from multiprocessing import context
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# Import Question, and Choice from models to set view
from .models import Question, Choice

# Get Questions and display them:
def index(request):
    # Question list to be looped through by publish date in descending order, LIMIT: 5
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Context: pass into template as a object/dictionary
    context = {'latest_question_list': latest_question_list}
    # Return a template:
    return render(request, 'polls/index.html', context)


# Show specific question and choices
def detail(request, question_id):
    # Try to find a question using primary key
    try:
        question = Question.objects.get(pk=question_id)
    # If not found raise 404 error
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    # Return if it does exist
    return render(request, 'polls/detail.html', {'question': question})


# Get question and display result
def results(request, question_id):
    # Try to find a result using question and primary key or 404 page
    question = get_object_or_404(Question, pk=question_id)
    # Return if question does exist
    return render(request, 'polls/results.html', {'question': question})


# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
