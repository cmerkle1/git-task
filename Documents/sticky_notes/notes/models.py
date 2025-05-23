# notes/models.py
from django.db import models


class Note(models.Model):
    """Represents a virtual sticky note. 
    Fields:
    - title: CharField for the post title with a maximum length of 255
    characters.
    - content: TextField for the post content.
    - created_at: DateTimeField set to the current date and time when the
    post is created.

    Relationships:
    - author: ForeignKey representing the author of the post.

    Methods:
    - __str__: Returns a string representation of the post, showing the
    title.
    :param models.Model: Django's base model class.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
      "Author", on_delete=models.CASCADE, null=True, blank=True
      )

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Model representing the author of the sticky note.
    Fields:
    - name: CharField for the author's name.

    Methods:
    - __str__: Returns a string representation of the author, showing the
    name.
    :param models.Model: Django's base model class.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
