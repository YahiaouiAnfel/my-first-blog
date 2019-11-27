from django.shortcuts import render

# A view is a place where we put the "logic" of our application.
#It will request information from the model you created before and pass it to a template
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    #we created a function (def) called post_list that takes request and 
    #will return the value it gets from calling another function render that will render 
    #(put together) our template blog/post_list.html.