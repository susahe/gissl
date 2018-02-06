﻿from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
        n_list = (('SI','සිංහල'),('TA','ද්‍රවිඩ'),('MU','මුස්ලිම්'),('BR','බර්ගර්'),('MA','මැලේ'),('OT','වෙනත්'))
        r_list = (('BU','බෞද්ධ'),('RC','කතෝලික'),('HI','හින්දු'),('IS','ඉස්ලාම්'),('CH','ක්‍රිස්තියානි'),('OT','වෙනත්'))
        e_list = (('PS','පාසල් යාමට පෙර'),('PR','පෙර පාසැල්'),('OF','1-5 ශ්‍රේණිය දක්වා'),('FO','5 සිට සා/පෙළ දක්වා'),('OP','සාමන්‍ය පෙළ සමත්'),('UA','උසස් පෙළ දක්වා'),('AP','උසස් පෙළ සමත්'),('DG','උපාධි හා ඊට ඉහල'),('NS','කිසිදා පසැල් නොගිය'))
        g_list = (('M','පිරිමි'),('F','ගැහැණු'))
        j_list = (('GS','රාජ්‍ය අංශය'),('SG','අර්ධ රාජ්‍ය අංශ්‍ය'),('PR','පේද්ගලික අංශය'),('FJ','විදේශ රැකියා'),('GS','රජයේ ආරක්ෂක අංශ'),('SJ','ස්වයං රැකියා'),('AG','කෘෂි කාර්මීක'),('FH','ධීවර'),('AS','සත්ව පාලන '),('SS','සේවා යෝජක'),('PN','විශ්ශ්‍රාමික'),('HW','ගෘහණිය'),('NJ','රැකියාවක් නොකරන'),('SC','පාසැල් යන'),('CH','ළදරු') )
        #models adttributes --------------------------------------------------------------------------------------------------------
        p_full_name = models.CharField(max_length=100,verbose_name="සම්පූර්ණ  නම") # Person First Name
       # p_lname = models.CharField(max_length=300,verbose_name="වාසගම") # Person Last Name
       # p_oname =  models.CharField(max_length=300,verbose_name="අනිකුත් නම්") # Person Other Name
        #p_nic   = models.CharField(max_length=10,verbose_name="ජාතික හැඳුනුම්පත් අංකය") # Person National Identity card
        p_edu   = models.CharField(max_length=2,verbose_name= "අධ්‍යාපන සුදුසුකම්",choices=e_list , default='OP')
        p_job   = models.CharField(max_length=100,verbose_name= "රැකියාව",choices=j_list)
        p_job_position = models.CharField(max_length=50, verbose_name="තනතුර")
        p_nationality  = models.CharField(max_length=2,verbose_name="ජාතිය",choices = n_list,default='SI')
        p_religion     = models.CharField(max_length=2,verbose_name="ආගම",choices = r_list,default='BU')
        p_birthdate    = models.DateField(default="1/1/1977",verbose_name="උපන්දිනය")
        p_gender       = models.CharField(max_length=1,verbose_name="ස්ත්‍රී/ පුරුෂ භාවය",choices= g_list, default= 'F')
        p_pic   = models.ImageField(upload_to='profile_image',blank=True,verbose_name='ඡායාරූපය')
       # user	= models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='ජාතික හැඳුනුම්පත් අංකය')
	#----------------------------------------------------------------------------------------------------------------------------
        def __str__(self):
                return self.p_full_name   
