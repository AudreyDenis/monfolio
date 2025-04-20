from django.contrib import admin
from . import models as m 

class FormatProfile(admin.ModelAdmin):
    list_display    = ['nom', 'prenom','phone', 'contact_email',]
    list_filter     = ['nom', 'prenom']

class FormatExperience(admin.ModelAdmin):
    list_display    = ['profile', 'title_poste','company', 'start_date','end_date']
    list_filter     = ['profile', 'title_poste','company', 'start_date','end_date']

class FormatProjet(admin.ModelAdmin):
    list_display    = ['profile', 'title', 'start_date','end_date']
    list_filter     = ['profile', 'title', 'start_date','end_date']

class FormatCertif(admin.ModelAdmin):
    list_display    = ['profile', 'title', 'institution','date_obtention']
    list_filter     = ['profile', 'title', 'institution','date_obtention']

class FormatSkill(admin.ModelAdmin):
    list_display    = ['profile', 'name', 'niveau','category']
    list_filter     = ['profile', 'name', 'niveau','category']

class FormatAccomp(admin.ModelAdmin):
    list_display    = ['profile', 'related_projet', 'title','date']
    list_filter     = ['profile', 'related_projet', 'title','date']


admin.site.register(m.Profile, FormatProfile)
admin.site.register(m.Experience, FormatExperience)
admin.site.register(m.Projet, FormatProjet)
admin.site.register(m.Certification, FormatCertif)
admin.site.register(m.Skill, FormatSkill)
admin.site.register(m.Accomplissement, FormatAccomp)
admin.site.register(m.Image)