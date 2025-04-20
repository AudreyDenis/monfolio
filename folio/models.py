from django.db import models

class Profile(models.Model):
    nom           = models.CharField(max_length=180)
    prenom        = models.CharField(max_length=180)
    bio           = models.TextField(blank=True, null=True)
    avatar        = models.ImageField(upload_to='media/images', blank=True, null=True)
    phone         = models.CharField(max_length=15)
    contact_email = models.EmailField()
    whatsapp      = models.URLField(blank=True, null=True) 
    linkedin_url  = models.URLField(blank=True, null=True)
    github_url    = models.URLField(blank=True, null=True)
    website_url   = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_experience')
    title_poste = models.CharField(max_length=255)
    company     = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    start_date  = models.DateField()
    end_date    = models.DateField(blank=True, null=True)  # Null si toujours en cours

class Projet(models.Model):
    profile          = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_project')
    title            = models.CharField(max_length=255)
    description      = models.TextField()
    image            = models.ImageField(upload_to='projet_images/', blank=True, null=True)
    github_url       = models.URLField(blank=True, null=True)
    live_url         = models.URLField(blank=True, null=True)
    is_future_projet = models.BooleanField(default=False)
    created_at       = models.DateTimeField(auto_now_add=True)
    start_date       = models.DateField()
    end_date         = models.DateField(blank=True, null=True)  # Null si toujours en cours

class Certification(models.Model):
    profile         = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_certifications')
    title           = models.CharField(max_length=255)
    institution     = models.CharField(max_length=255)
    date_obtention  = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)  # Null si pas de date d'expiration
    credential_id   = models.CharField(max_length=255, blank=True, null=True)
    credential_url  = models.URLField(blank=True, null=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    
class Skill(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_skills')
    name        = models.CharField(max_length=100)
    niveau      = models.IntegerField(default=1)  # Note sur 1-10 ou utiliser un système de choix
    category    = models.CharField(max_length=100, blank=True, null=True)  # e.g. "Tech", "Soft Skill"
    created_at       = models.DateTimeField(auto_now_add=True)

class Accomplissement(models.Model):
    profile         = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_accomplissement')
    related_projet  = models.ForeignKey(Projet, on_delete=models.SET_NULL, blank=True, null=True, related_name='project_profile_accomplissement')
    title           = models.CharField(max_length=255)
    description     = models.TextField(blank=True, null=True)
    date            = models.DateField()
    created_at      = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    experience  = models.ForeignKey(Experience, on_delete=models.CASCADE, null=True, blank=True, related_name='experience_image')
    projet      = models.ForeignKey(Projet, on_delete=models.CASCADE, null=True, blank=True, related_name='project_image')
    content     = models.ImageField(upload_to='media/images')
