# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from smsforms.models import DecisionTrigger
from django.db.models.aggregates import Count

def download(request):
    triggers = DecisionTrigger.objects.annotate(num_sessions=Count('xformssession'))
    return render_to_response("smscouchforms/smsform_download.html",
                              {"triggers": triggers}, 
                              context_instance=RequestContext(request))