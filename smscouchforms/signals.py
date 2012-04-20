from smsforms.signals import form_complete
from couchforms.util import post_xform_to_couch
from django.dispatch import Signal

xform_saved_with_session = Signal(providing_args=["session", "xform"])

def save_form_to_couch(sender, session, form, **kwargs):
    xform_instance = post_xform_to_couch(form)
    #Send out a signal with both the XFormInstance and the Session object.
    xform_saved_with_session.send(sender="smscouchforms", session=session, xform=xform_instance)
    
form_complete.connect(save_form_to_couch)