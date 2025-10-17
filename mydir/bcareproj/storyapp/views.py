from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Story

def stories(request):
    """
    Display all stories: static categories + approved user stories.
    """
    stories = Story.objects.filter(status="approved").order_by("-created_at")
    return render(request, "storyapp/stories.html", {
        "stories": stories
    })

@login_required
def sharestory(request):
    """
    Allow logged-in users to submit their story.
    Story will be marked as 'pending' until approved by admin.
    """
    if request.method == "POST":
        storyteller = request.POST.get("storyteller") or "Anonymous"
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title or not content:
            return render(request, "storyapp/sharestory.html", {
                "error": "⚠ Please provide both a title and content.",
                "storyteller": storyteller,
                "title": title,
                "content": content,
            })

        # Save story as pending
        Story.objects.create(
            storyteller=storyteller,
            title=title,
            content=content,
            user=request.user,
            status="pending",
            created_at=timezone.now()
        )

        # Show success box instead of form
        return render(request, "storyapp/sharestory.html", {
            "story_submitted": True,
            "storyteller": storyteller,
            "title": title
        })

    return render(request, "storyapp/sharestory.html")
