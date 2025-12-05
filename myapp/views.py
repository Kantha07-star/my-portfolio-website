from django.shortcuts import render
from myapp.models import Contact
from django.contrib import messages
# Create your views here.


def contact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		if len(name)>1 and len(name)<30 and len(phone)>=10:
			pass
		else:
			messages.error(request, "Please fill the form correctly")
			return render(request, 'base/home.html')
		
		# Save the contact information to the database
		
		new_contact = Contact(name=name, email=email, phone=phone, message=message)
		new_contact.save()
		messages.success(request, "Your message has been sent successfully!")
		
		
	return render(request, 'base/home.html')