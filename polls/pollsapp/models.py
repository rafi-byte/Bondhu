from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=1000)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices')
    options = models.CharField(max_length=1000)
    vote = models.IntegerField(default=0)
    urltext = models.CharField(max_length=1000, default="Some String")

    def __str__(self):
        return self.options


# class Links(models.Model):
#     optionsb = models.ForeignKey(
#         Choice, on_delete=models.CASCADE, related_name='linksop')
#     optionsl = models.CharField(max_length=1000)
#     vote1 = models.IntegerField(default=0)

#     def __str__(self):
#         return self.optionsl
