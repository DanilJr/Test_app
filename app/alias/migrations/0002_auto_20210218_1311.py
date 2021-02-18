# Generated by Django 3.1.6 on 2021-02-18 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alias',
            options={'ordering': ['alias'], 'verbose_name': 'Alias', 'verbose_name_plural': 'Aliases'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterField(
            model_name='alias',
            name='alias',
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='alias',
            name='end',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='alias',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_books', to='alias.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=24, primary_key=True, serialize=False),
        ),
    ]