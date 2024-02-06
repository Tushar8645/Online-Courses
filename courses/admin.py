from django.contrib import admin
from courses.models import Course, Tag, Prerequisite, Learning, Video, UserCourse, Payment


class TagAdmin(admin.TabularInline):
    model = Tag


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class LearningAdmin(admin.TabularInline):
    model = Learning


class VideoAdmin(admin.TabularInline):
    model = Video


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        TagAdmin,
        PrerequisiteAdmin,
        LearningAdmin,
        VideoAdmin,
    ]
    prepopulated_fields = {
        'slug': ('name',),
    }


admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(UserCourse)
admin.site.register(Payment)
