# Create your views here.
from django.shortcuts import render, redirect
from .models import Match, Player, News


def home_view(request):
    latest_match = Match.objects.filter(status='Full Time').order_by('-match_date').first()
    upcoming_match = Match.objects.filter(status='Upcoming').order_by('match_date').first()
    news_list = News.objects.all().order_by('-published_date')[:3]
    
    # Added group standings query to match your news view logic
    group_standings = GroupStanding.objects.all().order_by('group_name', 'position')
    
    context = {
        'latest_match': latest_match,
        'upcoming_match': upcoming_match,
        'news_list': news_list,
        'group_standings': group_standings, # Included in the context dictionary
    }
    return render(request, 'core/home.html', context)

def matches_view(request):
    matches = Match.objects.all().order_by('-match_date')
    return render(request, 'core/matches.html', {'matches': matches})

from django.shortcuts import render
from .models import Player, Formation

def squad_view(request):
    players = Player.objects.all().order_by('jersey_number')
    formations = Formation.objects.filter(is_active=True)
    return render(request, 'core/squad.html', {
        'players': players,
        'formations': formations
    })

from django.shortcuts import render
from .models import News, Match , GroupStanding # Import both models



def news_view(request):
    news_list = News.objects.all().order_by('-published_date')
    matches = Match.objects.all().order_by('-match_date')[:6]
    
    # Fetch all group entries from database
    group_standings = GroupStanding.objects.all()
    
    context = {
        'news_list': news_list,
        'matches': matches,
        'group_standings': group_standings,
    }
    return render(request, 'core/news.html', context)
def contact_view(request):
    if request.method == 'POST':
        # Handle contact/trial form submission logic here
        return redirect('contact')
    return render(request, 'core/contact.html')

#contact page   
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Saves the message data directly to the database!
            messages.success(request, 'Your message has been sent successfully to Ocean Stars FC!')
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, 'core/contact.html', {'form': form})


