from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    slug = models.CharField(
        max_length=80,
        null=False,
        blank=False,
        unique=True
    )
    description = models.CharField(max_length=280, null=True, blank=True)
    price = models.IntegerField(null=False, blank=False)
    discount = models.IntegerField(default=0, null=False, blank=False)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='thumbnail')
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='resource')
    length = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description = models.CharField(max_length=180, null=False, blank=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.description

    class Meta:
        abstract = True


class Tag(CourseProperty):
    pass


class Prerequisite(CourseProperty):
    pass


class Learning(CourseProperty):
    pass


class Video(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    serial_number = models.IntegerField(null=False, blank=False)
    video_id = models.CharField(max_length=180, null=False, blank=False)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title.title()

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(Video, self).save(*args, **kwargs)


class UserCourse(models.Model):
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + self.course.name


class Payment(models.Model):
    order_id = models.CharField(max_length=80, null=False, blank=False)
    payment_id = models.CharField(max_length=80)
    user_course = models.ForeignKey(
        UserCourse,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
