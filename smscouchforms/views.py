# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from touchforms.formplayer.models import XForm

def download(request):
    forms = XForm.objects.all()
    return render_to_response("smscouchforms/smsform_download.html",
                              {"forms": forms}, 
                              context_instance=RequestContext(request))