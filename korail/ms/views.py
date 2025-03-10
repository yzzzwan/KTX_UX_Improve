from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.


def testms(request):
    print("!@@@@@@@@@@@@@@@")
    # POST
    if request.method == 'POST':
        # form의 'text_data_input' 에 입력한 데이터를 불러옴
        data = request.POST.get('text_data_input')

        # 'text_data_session' 이라는 이름으로 data 를 저장하고
        # settings.py 에서 설정했던 것처럼 DB 내에 저장
        request.session['text_data_session'] = data

        return redirect('using_session')

    # GET
    else:
        # DB 내에 request 한 클라이언트 의 session 데이터중
        # 'text_data_session' 이 있는지 검사
        # True : session data load
        # False : None
        data = request.session.get('text_data_session', None)

        context = {'text_data': data}


    # return render(request, 'index.html', context)
    return render(request, 'e.html',context)