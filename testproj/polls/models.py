from django.db import models

# Create your models here.

# two models: polls and choices.
# A poll has a question and a publication date.
# A choice has two fields: the text of the choice and a vote tally.
# Each choice is associated with a poll.

from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()