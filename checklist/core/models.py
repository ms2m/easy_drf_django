from django.db import models


# Create your models here.
class CheckList(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    ## auto_now_add 1st time create set to current value
    created_on = models.DateTimeField(auto_now_add=True)
    ## auto_now update time update set to current value
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CheckListItem(models.Model):
    text = models.CharField(max_length=100)
    is_checked = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
