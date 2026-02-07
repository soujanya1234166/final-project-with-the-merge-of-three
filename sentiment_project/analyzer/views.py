from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from textblob import TextBlob

from .models import SentimentHistory


# ---------------- LOGIN VIEW ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(
                request,
                "analyzer/login.html",
                {"error": "Invalid username or password"}
            )

    return render(request, "analyzer/login.html")


# ---------------- LOGOUT VIEW ----------------
def logout_view(request):
    logout(request)
    return redirect("/login/")


# ---------------- DASHBOARD / SENTIMENT VIEW ----------------
@login_required
def index(request):
    result = None

    if request.method == "POST":
        text = request.POST.get("text")

        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0.1:
            sentiment = "Positive"
            emoji = "😊"
        elif polarity < -0.1:
            sentiment = "Negative"
            emoji = "😞"
        else:
            sentiment = "Neutral"
            emoji = "😐"

        # Save to database (history)
        SentimentHistory.objects.create(
            user=request.user,
            text=text,
            sentiment=sentiment,
            polarity=polarity,
            subjectivity=subjectivity
        )

        result = {
            "sentiment": sentiment,
            "emoji": emoji,
            "polarity": round(polarity, 2),
            "subjectivity": round(subjectivity, 2)
        }

    # Fetch user history
    history = SentimentHistory.objects.filter(user=request.user).order_by("-created_at")

    # Data for chart
    chart_data = [h.polarity for h in history]

    return render(
        request,
        "analyzer/index.html",
        {
            "result": result,
            "history": history,
            "chart_data": chart_data
        }
    )
