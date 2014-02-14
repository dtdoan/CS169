#from django.contrib import admin

# Register your models here.
import datetime
from django.utils import timezone
from django.contrib import admin
from loginCount.models import UserModel

# replaced this line with the next,
# any time you need to change the admin options for an obj
# admin.site.register(Poll)

# switches the order of pubdate and question,
# where it defaulted to question, pubdate in the form
#class PollAdmin(admin.ModelAdmin):
 #   fields = ['pub_date', 'question']

#admin.site.register(Poll, PollAdmin)

#separates sections and adds headings and titles
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        #titles or headings before question
        ('Username', {'fields': ['username']}), 
        ('Password', {'fields': ['password']}),
    ]
    #adds search bar to top of list, searchs question field
    search_fields = ['username']


    '''
class ChoiceInline(admin.StackedInline): # TabularInline is more compact
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    #Filter sidebar filters by the pub_date field; type filtered by is django auto
    list_filter = ['pub_date']
    #adds search bar to top of list, searchs question field
    search_fields = ['question']
    
    #err0r: date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
    '''

admin.site.register(UserModel, UserAdmin)
