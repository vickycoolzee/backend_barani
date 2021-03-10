# Generated by Django 3.1.7 on 2021-03-10 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_supplier_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier_evaluation',
            name='Supplier_code',
        ),
        migrations.AddField(
            model_name='supplier_rating',
            name='Supplier_detail',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='purchase.supplier_detail'),
        ),
        migrations.CreateModel(
            name='Supplier_assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Term_1', models.IntegerField()),
                ('Term_2', models.IntegerField()),
                ('Term_3', models.IntegerField()),
                ('Term_4', models.IntegerField()),
                ('Term_5', models.IntegerField()),
                ('Term_6', models.IntegerField()),
                ('Term_7', models.IntegerField()),
                ('Term_8', models.IntegerField()),
                ('Term_9', models.IntegerField()),
                ('Term_10', models.IntegerField()),
                ('Supplier_detail', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='purchase.supplier_detail')),
            ],
        ),
    ]
