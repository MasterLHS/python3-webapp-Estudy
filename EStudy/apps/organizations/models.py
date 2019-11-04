from django.db import models

from apps.users.models import BaseModel
from apps.users.models import UserProfile
from DjangoUeditor.models import UEditorField


class City(BaseModel):
    name = models.CharField(verbose_name="城市名", max_length=20)
    desc = models.CharField(verbose_name="描述", max_length=200)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(verbose_name="机构名称", max_length=50)
    desc = UEditorField(verbose_name="描述", width=600, height=300, imagePath="org/ueditor/images/",
                          filePath="org/ueditor/files/", default="")
    tag = models.CharField(verbose_name="机构标签", default="全国知名", max_length=10)
    category = models.CharField(verbose_name="机构类别", default="pxjg", max_length=4,
                                choices=(('pxjg','培训机构'),('gr','个人'),('gx','高校')))
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    image = models.ImageField(verbose_name="logo", upload_to="org/%Y/%m", max_length=100)
    address = models.CharField(verbose_name="机构地址", max_length=150)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    course_nums = models.IntegerField(verbose_name="课程数", default=0)

    is_auth = models.BooleanField(default=False, verbose_name="是否认证")
    is_gold = models.BooleanField(default=False, verbose_name="是否是金牌")

    city = models.ForeignKey(City, verbose_name="所在城市", on_delete=models.CASCADE)

    def courses(self):
        courses = self.course_set.filter(is_classic=True)[:3]
        return courses

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(verbose_name="教师名", max_length=50)
    work_years = models.IntegerField(verbose_name="工作年限", default=0)
    work_company = models.CharField(verbose_name="就职公司", max_length=50)
    work_position = models.CharField(verbose_name="公司职位", max_length=50)
    points = models.CharField(verbose_name="教学特点", max_length=50)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    age = models.IntegerField(verbose_name="年龄", default=20)
    image = models.ImageField(verbose_name="头像", upload_to="techter/%Y/%m", default="")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.all().count()