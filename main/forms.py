from django.forms import ModelForm
from .models import Course, Team, Meeting, Task

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'join_code']
        
class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'join_code']
        
class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['link', 'memo', 'meeting_time']
        
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','attached','due_date','is_team_task']