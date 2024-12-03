from django.contrib import admin
from blog.models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["title","author","counted_view","status","login_required"]
    list_filter = ["status"]
    search_fields = ["title","content"]
    summernote_fields = ('content',)

    
    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name","post","approved","created_date"]
    list_filter = ["post","approved"]
    summernote_fields = ('name','post')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)

    
    
