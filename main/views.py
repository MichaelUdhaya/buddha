from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages

#utiltis
from datetime import datetime

from .choices import FEEDBACK_RATING
from .models import Post, Feedback, Contact, Advertisement


# Home Page
def home_view(request):
	""" Home Page of school site """

	#get the recent post
	recent_post_count = Post.objects.count()
	post = Post.objects.filter(pk=recent_post_count)

	#Get all advertisment only expire date greater than today date.
	ads = Advertisement.objects.filter(ad_expire_date__gt = datetime.now()).order_by('-ad_updated_date')

	#Get all post by desending order
	post_lists = Post.objects.order_by('-post_published')[:4]


	context = {
		'post' : post,
		'post_lists' : post_lists,
		'ads' : ads
	}

	return render(request, 'main/index.html', context)

# Post Page
def post_view(request, pk):
	"""Annoncement page """
	post = get_object_or_404(Post, pk=pk)
	all_posts = Post.objects.order_by('-post_published')

	paginator = Paginator(all_posts, 5)
	page = request.GET.get('page')
	paged_posts = paginator.get_page(page)

	context = {
		'post' : post,
		'all_posts' : paged_posts,
	}

	return render(request, 'main/post.html', context)

# Post List
def post_list(request):
	"""Annoncements page """
	posts = Post.objects.order_by('-post_published')

	paginator = Paginator(posts, 10)
	page = request.GET.get('page')
	paged_posts = paginator.get_page(page)

	context = {
		'posts' : paged_posts,
	}

	return render(request, 'main/post_list.html', context)

# Facilities Page
def facilities_view(request):
	""" Facilities Page of school site """
	posts = Post.objects.all()
	return render(request, 'main/facilities.html', {})

# Admissions Page
def admissions_view(request):
	""" Admissions Page of school site """
	posts = Post.objects.all()
	return render(request, 'main/admissions.html', {})

# Policies/Staffs Page
def policies_view(request):
	""" Policies/Staffs Page of school site """
	#Get the last updated object's pk and pass to it
	# policy = Policy.objects.filter(pk=Policy.objects.count())
	return render(request, 'main/policies.html', {'policy':'policy'})

# Gallery Page
def gallery_view(request):
	""" Policies/Staffs Page of school site """
	return render(request, 'main/working.html', {})

# About Us Page
def about_us_view(request):
	""" About Us Page of school site """
	posts = Post.objects.all()
	return render(request, 'main/about.html', {})

# Contact Us Page
def contact_us_view(request):
	""" About Us Page of school site """
	contact = Contact.objects.filter(pk=Contact.objects.count())
	return render(request, 'main/contact-us.html', {'contact':contact})

# Feedback Page
def feedback_view(request):
	""" Get the Feedback from users """
	if request.method == "POST":
		#Get forom values.
		name = request.POST['fullname']
		email = request.POST['email']
		rating = request.POST['rating']
		message = request.POST['feedback']

		feedback = Feedback(name=name, email=email, rating=rating, message=message)

		feedback.save()

		messages.success(request, ' Hi '+ name + '! Your feedback submitted successfully!')

		return redirect('main:url_home')
	else:
		return render(request, 'main/feedback.html', {'FEEDBACK_RATING': FEEDBACK_RATING})
