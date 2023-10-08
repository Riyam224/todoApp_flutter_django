from audioop import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Todo(models.Model):
    
    title = models.CharField(_("title"), max_length=50)
    desc = models.TextField(_("desc"))
    isDone = models.BooleanField(_("is done") ,  default=False)
    create_at = models.DateTimeField(_("created at"),  auto_now_add=True)
    

    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})
