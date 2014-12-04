from django.contrib.auth.models import User
from blog.models import Post

user = User.objects.get(pk=1)

p1 = Post(title="Hello, djblog", author=user, content="Hello, Django")
p1.save()