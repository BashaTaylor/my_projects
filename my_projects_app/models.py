from django.db import models

class ProjectManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Project title should be at least 2 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Project description should be at least 10 characters"
        if len(postData['deployed_link']) < 3:
            errors["deployed_link"] = "Project link should be at least 3 characters"
        return errors

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deployed_link = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'<{self.title}, {self.description}, {self.deployed_link})>'
