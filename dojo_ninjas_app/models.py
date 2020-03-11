from django.db import models
class Dojo(models.Model):
    def __repr__(self):
        return f"<object: {self.name} ({self.id})>"
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    desc = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    def __repr__(self):
        return f"<object: {self.first_name} {self.last_name} ({self.dojo_location})>"
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dojo_location = models.ForeignKey(Dojo, related_name="Ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)