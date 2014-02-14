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


admin.site.register(UserModel, UserAdmin)