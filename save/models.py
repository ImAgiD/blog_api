# from django.db import models

# from django.contrib.auth import get_user_model

# User = get_user_model()

# class SavedPost(models.Model):
#     user = models.ForeignKey(User, related_name='saved_posts', on_delete=models.CASCADE)
#     post = models.ForeignKey('posts.Post', related_name='saved_by', on_delete=models.CASCADE)
#     saved_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ['user', 'post']
