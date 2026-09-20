from django.db import models

# Create your models here.


class Match(models.Model):
    opponent = models.CharField(max_length=100)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    match_date = models.DateTimeField()
    is_home = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=[('Upcoming', 'Upcoming'), ('Full Time', 'Full Time')], default='Upcoming')

    def __str__(self):
        return f"Ocean Stars FC vs {self.opponent} ({self.status})"
    
    from django.db import models

from django.db import models

class Player(models.Model):
    POSITION_CHOICES = [
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Forward', 'Forward'),
    ]
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    jersey_number = models.IntegerField()
    bio = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True, help_text="Path to image inside static folder e.g., 'images/players/player1.jpg'")

    def __str__(self):
        return f"#{self.jersey_number} {self.name} ({self.position})"
class Formation(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="e.g. 4-4-2, 4-2-3-1")
    code = models.CharField(max_length=20, unique=True, help_text="Type layout format numbers here e.g. 4-4-2, 4-3-3, or 4-2-3-1")
    description = models.TextField(blank=True, null=True, help_text="Brief tactical notes.")
    is_active = models.BooleanField(default=True, help_text="Check to display on public site.")

    def __str__(self):
        return f"{self.name} ({self.code})"



class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.submitted_at.strftime('%Y-%m-%d')})"
    

    from django.db import models

class GroupStanding(models.Model):
    GROUP_CHOICES = [
        ('A', 'Group A'),
        ('B', 'Group B'),
        ('C', 'Group C'),
        ('D', 'Group D'),
        ('E', 'Group E'),
        ('F', 'Group F'),
    ]
    
    group_name = models.CharField(max_length=1, choices=GROUP_CHOICES, default='A')
    team_name = models.CharField(max_length=100)
    played = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    drawn = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    position = models.PositiveIntegerField(default=1)
    is_ocean_stars = models.BooleanField(default=False, help_text="Check if this team is Ocean Stars FC")

    class Meta:
        ordering = ['group_name', 'position']

    def __str__(self):
        return f"Group {self.group_name} - {self.team_name} (Pos {self.position})"