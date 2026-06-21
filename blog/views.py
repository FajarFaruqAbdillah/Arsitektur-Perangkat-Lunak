from django.http import Http404
from django.shortcuts import render

from .content import ARCHITECTURE_NOTES, POSTS, TOPICS


def home(request):
    context = {
        "featured_posts": POSTS,
        "topics": TOPICS,
        "architecture_notes": ARCHITECTURE_NOTES,
    }

    return render(request, "blog/index.html", context)


def post_detail(request, slug):
    for index, post in enumerate(POSTS):
        if post["slug"] == slug:
            next_post = POSTS[index + 1] if index + 1 < len(POSTS) else None
            previous_post = POSTS[index - 1] if index > 0 else None
            return render(
                request,
                "blog/detail.html",
                {
                    "post": post,
                    "next_post": next_post,
                    "previous_post": previous_post,
                },
            )

    raise Http404("Materi tidak ditemukan.")
