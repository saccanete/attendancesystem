from django.shortcuts import render, redirect
from .models import eventList
from .forms import eventForm, editForm
from datetime import date
# Create your views here.

def Attendance(request):
    today = date.today()
    if request.method == 'POST': 
        form = eventForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_student = eventList.objects.all()
            context = {'all_student':all_student, 'user':"mbgingo3", 'date':today}
            return render(request, 'Attendance.html', context)
    else:
        all_student = eventList.objects.all()
        context = {'all_student': all_student, 'user':"mbgingo3", 'date':today}
        return render(request, 'Attendance.html',context)
        
def edit(request, list_id):
    if request.method == 'POST':
        list_item = eventList.objects.get(pk=list_id)
        form = editForm(request.POST or None)
        if form.is_valid():
            updated_lastname = form.cleaned_data.get("lastname")
            list_item.lastname = updated_lastname
            list_item.save()
            updated_firstname = form.cleaned_data.get("firstname")
            list_item.firstname = updated_firstname
            list_item.save()
            updated_level = form.cleaned_data.get("level")
            list_item.level = updated_level
            list_item.save()
            updated_course = form.cleaned_data.get("course")
            list_item.course = updated_course
            list_item.save()
            updated_gender = form.cleaned_data.get("gender")
            list_item.gender = updated_gender
            list_item.save()
            updated_event = form.cleaned_data.get("event")
            list_item.event = updated_event
            list_item.save()
            return redirect('Attendance')  
    else:
        list_item = eventList.objects.get(pk=list_id)
        context = {"list_id": list_id, "list_item":list_item}
        return render(request, 'edit.html',context)
def delete(request, list_id):
	item = eventList.objects.get(pk=list_id)
	item.delete()
	return redirect('Attendance')
