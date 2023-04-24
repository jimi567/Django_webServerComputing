from django.contrib import admin
from .models import Question
#추가된 부분
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
                              #추가된 부분
admin.site.register(Question, QuestionAdmin)
