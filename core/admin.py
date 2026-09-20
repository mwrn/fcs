from django.contrib import admin

# Register your models here.
from .models import Match, Player, News, ContactMessage , Formation, GroupStanding



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title', 'summary')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('opponent', 'match_date', 'status', 'is_home', 'home_score', 'away_score')
    list_filter = ('status', 'is_home')
    search_fields = ('opponent',)

@admin.register(GroupStanding)
class GroupStandingAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'position', 'team_name', 'played', 'won', 'points', 'is_ocean_stars')
    list_filter = ('group_name', 'is_ocean_stars')
    search_fields = ('team_name',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('subject', 'submitted_at')




from django.contrib import admin
from .models import Player, Formation

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('jersey_number', 'name', 'position')
    list_filter = ('position',)
    search_fields = ('name',)

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')  # <--- Cleaned up to match your exact model fields
    list_editable = ('is_active',)
    search_fields = ('name', 'code')