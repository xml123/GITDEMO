from django.db import models

# Create your models here.
#文章所属分类
class Classify(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.title
#游客信息
class Visitor(models.Model):
    name = models.CharField(max_length=100, blank=True)
    avatar = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

#文章模型
class Artical(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    content_text = models.TextField(blank=True)
    view = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    classify = models.ForeignKey(Classify, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

#文章评论
class ArticalMessage(models.Model):
    message = models.CharField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    artical = models.ForeignKey(Artical, on_delete=models.CASCADE)
    #父评论
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message

#留言
class LiveMessage(models.Model):
    message = models.CharField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message

#友情链接
class Friends(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True)
    abstract = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name




















