from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'mt/homepage.html')

def board(request):
  return render(request, 'mt/board.html')

def timetable(request):
  return render(request, 'mt/timetable.html')