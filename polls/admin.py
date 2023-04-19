from django.contrib import admin

# Import and Register your models here.
from .models import Question, Choice

# Change Site Header/Title/Index Title
admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to Pollster admin area'


# Have Choices inline with Questions
class ChoiceInline(admin.TabularInline):
    model = Choice
    # Extra fields?
    extra = 3

# Sets Question so it can show Choice(s) inline
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets take in a Name, object/dictionary for the fields in admin
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    # Sets Choice(s) inline with Question(s)
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
