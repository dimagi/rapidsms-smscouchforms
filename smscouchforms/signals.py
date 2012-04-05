from smsforms.signals import form_complete
from couchforms.util import post_xform_to_couch

def save_form_to_couch(sender, session, form, **kwargs):
    post_xform_to_couch(form)
    
form_complete.connect(save_form_to_couch)