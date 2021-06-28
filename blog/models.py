from django.db import models


class BaseModel(models.Model):
    created_by = models.CharField(max_length=100, null=True)
    updated_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    summery = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title
