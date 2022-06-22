import time,subprocess
from .tasks import celery_run
from django.shortcuts import render

def home(request):
    if 'mainform' in request.POST:
        command = request.POST.get('command')
        rep = request.POST.get('rep')
        dur = request.POST.get('dur')
        cmd ='powershell -command '+command
        result=runcommand(cmd,rep,dur)
        context = {'output':result}
        return render(request,'home.html',context)

    if 'celeryform' in request.POST:
        command = request.POST.get('command')
        rep = request.POST.get('rep')
        dur = request.POST.get('dur')
        cmd ='powershell -command '+command 
        result=celery_run.delay(cmd,rep,dur)
        context = {'output':result}
        return render(request,'home.html',context)       
    return render(request,'home.html')

def runcommand(cmd,rep,dur):
    output=''
    for i in range(int(rep)):
        time.sleep(int(dur))
        p=subprocess.run(cmd,capture_output=True,text=True,shell=True)
        output += p.stdout
    return output
        