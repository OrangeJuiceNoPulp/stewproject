# Generated by Django 4.2.6 on 2023-10-29 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='teams', through='main.Membership', to=settings.AUTH_USER_MODEL, verbose_name='Members'),
        ),
        migrations.AddField(
            model_name='team',
            name='parent_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subteams', to='main.team'),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='grader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='graded_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_task', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_submissions', to='main.task'),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submitted_tasks', to='main.team'),
        ),
        migrations.AddField(
            model_name='task',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_tasks', to='main.course'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_level', to='main.team'),
        ),
        migrations.AddField(
            model_name='membership',
            name='Team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='main.team'),
        ),
        migrations.AddField(
            model_name='membership',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='main.course'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosted_meetings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='main.team'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='main.course'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taught_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses', through='main.Enrollment', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
    ]
