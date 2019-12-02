from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    POST_DRAFT = 0
    POST_NORMAL = 1
    POST_HIDDEN = 2
    POST_TYPE = (
        (POST_DRAFT, '草稿'),
        (POST_NORMAL, '正常'),
        (POST_HIDDEN, '隱藏'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    post_title = models.CharField(max_length=200, verbose_name='標題')
    post_content = models.TextField(max_length=1024, verbose_name='內容')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    mod_time = models.DateTimeField(auto_now=True, verbose_name='更新時間')
    views = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ['-pub_time']
        verbose_name = verbose_name_plural = '文章'


class Category(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='分頖名字')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    mod_time = models.DateTimeField(auto_now=True, verbose_name='更新時間')


    class Meta:
        ordering = ['-pub_time']
        verbose_name = verbose_name_plural = '分頖'


class Tag(models.Model):
    tag_name = models.CharField(max_length=200, verbose_name='標籤名字')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    mod_time = models.DateTimeField(auto_now=True, verbose_name='更新時間')

    class Meta:
        ordering = ['-pub_time']
        verbose_name = verbose_name_plural = '標籤'