from django.shortcuts import render

# # Create your views here.
#  movie_review_form = MovieReviewForm(
#             initial={'movie':movie,
#             'user': request.user,
#             'title': moviereview.title,
#             'rating': moviereview.rating,
#             'text': moviereview.text})
#         print(movie_review_form)
#         # movie_review_form.movie = movie
#         # print(movie_review_form.movie)
#     # print(movie_review_form)
#         return render(request, 'portal/manage_review.html', 
#         {'movie': movie,
#         'movie_review_form': movie_review_form})   