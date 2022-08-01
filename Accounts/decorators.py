from functools import wraps
from django.shortcuts import redirect
from .models import User


def logout_required():
	def decorator(func):
		@wraps(func)
		def wrapper(request,*args,**kwargs):
			if not request.user.is_authenticated:
				return func(request,*args,**kwargs)
			else:
				return redirect("Accounts:logout")
		return wrapper
	return decorator

def login_required():
	def decorator(func):
		@wraps(func)
		def wrapper(request,*args,**kwargs):
			if request.user.is_authenticated:
				return func(request,*args,**kwargs)
			else:
				return redirect("Accounts:login")
		return wrapper
	return decorator

 



