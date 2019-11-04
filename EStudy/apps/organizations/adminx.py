import xadmin

from .models import Teacher, CourseOrg, City


class TeacherAdmin(object):
    list_display = ["name", "work_years", "work_company", "work_position", "fav_nums", "click_nums"]
    search_fields = ["name", "work_years", "work_company", "age"]
    list_filter = ["name", "work_years", "work_company", "work_position", "age"]


class CourseOrgAdmin(object):
    list_display = ["name", "desc", "tag", "category", "click_nums", "fav_nums"]
    search_fields = ["name", "category", "tag"]
    list_filter = ["name", "tag", "category", "click_nums", "fav_nums"]

    style_fields = {
        "desc": "ueditor"
    }


class CityAdmin(object):
    list_display = ["id","name","desc"]
    search_fields = ["name","desc"]
    list_filter = ["name","desc","add_time"]
    list_editable = ["name","desc"]


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)