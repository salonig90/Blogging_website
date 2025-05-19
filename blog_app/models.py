from django.db import models
from django.utils.text import slugify 


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:# Check if slug is present
            self.slug = slugify(self.title) # Generate slug from title if not provided
            counter = 1
            original_slug = self.slug
            while Post.objects.filter(slug=self.slug).exists(): # Check for uniqueness if not unique then add a counter eg:hello-world-1
                self.slug = original_slug + "-" + str(counter)
                counter += 1
        super().save(*args, **kwargs)

        def __str__(self):
            return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.post.title