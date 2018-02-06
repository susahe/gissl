# Generated by Django 2.0.1 on 2018-02-05 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_full_name', models.CharField(max_length=100, verbose_name='සම්පූර්ණ  නම')),
                ('p_edu', models.CharField(choices=[('PS', 'පාසල් යාමට පෙර'), ('PR', 'පෙර පාසැල්'), ('OF', '1-5 ශ්\u200dරේණිය දක්වා'), ('FO', '5 සිට සා/පෙළ දක්වා'), ('OP', 'සාමන්\u200dය පෙළ සමත්'), ('UA', 'උසස් පෙළ දක්වා'), ('AP', 'උසස් පෙළ සමත්'), ('DG', 'උපාධි හා ඊට ඉහල'), ('NS', 'කිසිදා පසැල් නොගිය')], default='OP', max_length=2, verbose_name='අධ්\u200dයාපන සුදුසුකම්')),
                ('p_job', models.CharField(choices=[('GS', 'රාජ්\u200dය අංශය'), ('SG', 'අර්ධ රාජ්\u200dය අංශ්\u200dය'), ('PR', 'පේද්ගලික අංශය'), ('FJ', 'විදේශ රැකියා'), ('GS', 'රජයේ ආරක්ෂක අංශ'), ('SJ', 'ස්වයං රැකියා'), ('AG', 'කෘෂි කාර්මීක'), ('FH', 'ධීවර'), ('AS', 'සත්ව පාලන '), ('SS', 'සේවා යෝජක'), ('PN', 'විශ්ශ්\u200dරාමික'), ('HW', 'ගෘහණිය'), ('NJ', 'රැකියාවක් නොකරන'), ('SC', 'පාසැල් යන'), ('CH', 'ළදරු')], max_length=100, verbose_name='රැකියාව')),
                ('p_job_position', models.CharField(max_length=50, verbose_name='තනතුර')),
                ('p_nationality', models.CharField(choices=[('SI', 'සිංහල'), ('TA', 'ද්\u200dරවිඩ'), ('MU', 'මුස්ලිම්'), ('BR', 'බර්ගර්'), ('MA', 'මැලේ'), ('OT', 'වෙනත්')], default='SI', max_length=2, verbose_name='ජාතිය')),
                ('p_religion', models.CharField(choices=[('BU', 'බෞද්ධ'), ('RC', 'කතෝලික'), ('HI', 'හින්දු'), ('IS', 'ඉස්ලාම්'), ('CH', 'ක්\u200dරිස්තියානි'), ('OT', 'වෙනත්')], default='BU', max_length=2, verbose_name='ආගම')),
                ('p_birthdate', models.DateField(default='1/1/1977', verbose_name='උපන්දිනය')),
                ('p_gender', models.CharField(choices=[('M', 'පිරිමි'), ('F', 'ගැහැණු')], default='F', max_length=1, verbose_name='ස්ත්\u200dරී/ පුරුෂ භාවය')),
                ('p_pic', models.ImageField(blank=True, upload_to='profile_image', verbose_name='ඡායාරූපය')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ජාතික හැඳුනුම්පත් අංකය')),
            ],
        ),
    ]
