from django.contrib.auth.models import User
from .models import ParkingSpot
from django import forms


class SearchForm(forms.ModelForm):
    city = forms.CharField(max_length=20)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for key in self.fields:
        	self.fields[key].widget.attrs.update({
            'class': 'form-control'
        })

      	# self.fields['first_name'].widget.attrs.update({
      	# 	'class': 'form-control mini'
      	# 	})

      	# self.fields['last_name'].widget.attrs.update({
      	# 	'class': 'form-control mini'
      	# 	})
        
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        help_texts = {
            'username': None,
        }


class ParkingSpotForm(forms.ModelForm):
	class Meta:
		model = ParkingSpot
		fields = ['title', 'street', 'city', 'state', 'zipcode', 'price', 'picture', 'description']

	def __init__(self, *args, **kwargs):
		super(ParkingSpotForm, self).__init__(*args, **kwargs)

		for key in self.fields:
			if key is not 'picture':
				self.fields[key].widget.attrs.update({
					'class': 'form-control'
					})


