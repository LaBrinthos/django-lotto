from django.shortcuts import render, redirect

from django.http import HttpResponse

from lotto.models import GuessNumbers

from lotto.forms import PostForm

# Create your views here.
def index(request):

    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos':lottos})


def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            lotto = form.save(commit=False) # 중간 저장
            lotto.generate()

            return redirect('index') # 데이터를 보내고자 하는 URL의 별명(name)을 적어줌


        print('\n\n\n')
        print(type(lotto)) # <class 'lotto.models.GuessNumbers'>
        print(lotto)
        print('\n\n\n')


    form = PostForm()

    return render(request, 'lotto/form.html', {'form':form})


def hello(request):

    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key

    return render(request, 'lotto/detail.html', {'lotto':lotto})
