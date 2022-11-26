from datetime import date 
from django.shortcuts import render

all_posts = [ {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Elizabeth",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt":"There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happend whilst I was enjoying the view!",
        "content": """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Inventore distinctio 
            tempora non doloremque? Odit illum maxime cupiditate, iusto temporibus architecto 
            consectetur magnam ipsa fugiat, magni optio ratione aspernatur impedit quisquam?

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Inventore distinctio 
            tempora non doloremque? Odit illum maxime cupiditate, iusto temporibus architecto 
            consectetur magnam ipsa fugiat, magni optio ratione aspernatur impedit quisquam?

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Inventore distinctio 
            tempora non doloremque? Odit illum maxime cupiditate, iusto temporibus architecto 
            consectetur magnam ipsa fugiat, magni optio ratione aspernatur impedit quisquam?
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Veniamin",
        "date": date(2022, 1, 29),
        "title": "Programming Is Great",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
            sunt in culpa qui officia deserunt mollit anim id est laborum.
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
            sunt in culpa qui officia deserunt mollit anim id est laborum.
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
            sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Veniamin",
        "date": date(2022, 2, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
          dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
          sunt in culpa qui officia deserunt mollit anim id est laborum.
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
          dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
          sunt in culpa qui officia deserunt mollit anim id est laborum.
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
          dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
          sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    }
]

def get_date(post):
    return post["date"]

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
    "posts": latest_posts
    }  )

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")