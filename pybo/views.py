from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    page = request.GET.get('page','1') #페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) # 페이지당 10개 씩 보여줌
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj}
    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    """
    pybo 질문 상세 내용 출력
    """
    question = get_object_or_404(Question,pk=question_id)
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)

def answer_create(request, question_id):
    """
       pybo 질문에 대한 답변 등록
    """
    question = get_object_or_404(Question,pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    """
    pybo 질문 등록
    """
    # POST
    if request.method =='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=0)
            #timezone.now()는 django.utils의 timezone의 메소드
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    # GET
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
