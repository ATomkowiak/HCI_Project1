from django import forms




class sprawdz(forms.Form):
  error_css_class = 'error' ##custom css for form errors - ".error";
  required_css_class = 'required' ##custom css for required fields - ".required";
  info_text = forms.CharField()
