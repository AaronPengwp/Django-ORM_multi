# Generated by Django 2.1.5 on 2019-01-19 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190119_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book_author',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Book'),
        ),
    ]