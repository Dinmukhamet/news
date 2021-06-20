from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    link = models.URLField(_("Link"), max_length=200)
    author_name = models.CharField(_("Author Name"), max_length=100)
    upvotes = models.PositiveIntegerField(_("Amount of upvotes"))

    creation_date = models.DateTimeField(_("Creation Date"), auto_now_add=True)

    class Meta:
        db_table = "posts"
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("posts.Post", verbose_name=_(
        "Post"), related_name="comments", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", verbose_name=_(
        "Parent comment"), on_delete=models.SET_NULL, null=True, blank=True)
    author_name = models.CharField(_("Author Name"), max_length=100)
    content = models.TextField(_("Content"))

    creation_date = models.DateTimeField(_("Creation Date"), auto_now_add=True)

    class Meta:
        db_table = "comments"
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.author_name
