from django.shortcuts import render, redirect

# Create your views here.
from train_schedules.models import TrainSchedule
from urllib.parse import urlencode
from django.http import HttpResponse
def index(request):
    if request.method == 'GET':
        return render(request, "home/home.html")

    elif request.method == 'POST':

        request.session['DepartureStation'] = request.POST.get('DepartureStation_Input')
        request.session['ArrivalStation'] = request.POST.get('ArrivalStation_Input')
        request.session['Departure_Date'] = request.POST.get('Departure_Date_Input')
        request.session['Passenger_CNT'] = request.POST.get('Passenger_CNT_Input')

        if request.user.is_authenticated:
            return redirect('/train_schedules')
        else:
            return redirect('user/login')




def test(request):
    print(request.GET)
    data = request.GET
    request.session['DepartureStation'] = request.GET.get('DepartureStation_Input')
    request.session['ArrivalStation'] = request.GET.get('ArrivalStation_Input')
    request.session['Departure_Date'] = request.GET.get('Departure_Date_Input')
    request.session['Passenger_CNT'] = request.GET.get('Passenger_CNT_Input')

    # station 필드 값이 "강릉"인 데이터 가져오기
    # schedules = TrainSchedule.objects.filter(station="강릉")

    query_string = urlencode(data, doseq=True)
    redirect_url = f"/train_schedules?{query_string}"
    print(redirect_url)


    return redirect(redirect_url)



