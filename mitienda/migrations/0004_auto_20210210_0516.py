# Generated by Django 3.1.6 on 2021-02-10 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mitienda', '0003_auto_20210210_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billproduct',
            name='product_id',
        ),
        migrations.AddField(
            model_name='billproduct',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='mitienda.product'),
            preserve_default=False,
        ),
    ]