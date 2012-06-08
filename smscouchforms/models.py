from django.db import models
from couchforms.models import XFormInstance
from smsforms.models import XFormsSession

class FormReferenceBase(models.Model):
    """
    A base class that points at a form session and couch form, so you can 
    reference them easily.
    """
    form_id = models.CharField(max_length=100)
    session = models.ForeignKey(XFormsSession)
    
    @property
    def form(self):
        return XFormInstance.get(self.form_id)
    
    class Meta:
        abstract = True

# just to make sure these get imported once
from . import signals