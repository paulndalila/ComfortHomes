from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, to='owners.Owner'),
        ),
    ]
