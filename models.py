import datetime
from datetime import datetime
from django.db import models
from django.utils import timezone

#Demographics Tables

class Country(models.Model):
    country_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    class Meta:
        verbose_name_plural = 'countries'
    def __str__(self):
        return self.country_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Contact_type(models.Model):
    CONTACT_TYPE_CHOICES = [
        ('HOME', 'home'),
        ('WORK', 'work'),
        ('SCHOOL', 'school')
    ]
    contact_type = models.CharField(
        max_length=20,
        choices=CONTACT_TYPE_CHOICES,
        default='HOME'
    )
    def __str__(self):
        return self.contact_type
    class Meta:
        verbose_name_plural = 'Contact types'

class Address(models.Model):
    street_line_1 = models.CharField(max_length=255, blank=True)
    street_line_2 = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state_or_province = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    custom_address_type = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    contact_type = models.ForeignKey(Contact_type, on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'addresses'
    def __str__(self):
        return self.street_line_1

class Phone(models.Model):
#    contact_type = models.ForeignKey(Contact_type, on_delete=models.SET_NULL, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    phone_extension = models.CharField(max_length=20, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.phone_number

class Entity(models.Model):
    location_name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'entities'
    def __str__(self):
        return self.location_name

#Educational History Tables

class University(models.Model):
    university_name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'universities'
    def __str__(self):
        return self.university_name

class Concentration(models.Model):
    concentration_name = models.CharField(max_length=255)
    def __str__(self):
        return self.concentration_name

#Jobs Tables

class Job(models.Model):
    title = models.CharField(max_length=255)
    job_description = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.title

class Department(models.Model):
    department_name = models.CharField(max_length=30)
    department_code = models.IntegerField()
    def __str__(self):
        return self.department_name

class Employment_status(models.Model):
    #Add choices
    employment_status = models.CharField(max_length=20)
    reason_for_leaving = models.CharField(max_length=255, blank=True)
    class Meta:
        verbose_name_plural = 'employment statuses'
    def __str__(self):
        return self.employment_status

class Employment_type(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('FPT', 'Foreign Part-timers/Contractors'),
        ('FS', 'Foreign Staff'),
        ('FSC', 'Foreign Staff Children'),
        ('FSP', 'Foreign Staff Spouse'),
        ('I/V', 'Intern/Volunteer'),
        ('LH', 'Local Hire'),
        ('NP/C', 'National Part-timers/Contractors'),
        ('NS', 'National Staff')
    ]
    employment_type = models.CharField(
        max_length=255,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default='FS',
        )
    class Meta:
        verbose_name_plural = 'employment types'
    def __str__(self):
        return self.employment_type

class Equivalency(models.Model):
    PERCENTAGE_WORKLOAD = [
        ('5', '5%'),
        ('10', '10%'),
        ('15', '15%'),
        ('20', '20%'),
        ('25', '25%'),
        ('30', '30%'),
        ('35', '35%'),
        ('40', '40%'),
        ('45', '45%'),
        ('50', '50%'),
        ('55', '55%'),
        ('60', '60%'),
        ('65', '65%'),
        ('70', '70%'),
        ('75', '75%'),
        ('80', '80%'),
        ('85', '85%'),
        ('90', '90%'),
        ('95', '95%'),
        ('PB', 'Project-Based')
    ]
    full_time_percentage = models.CharField(max_length=255,
                                            choices=PERCENTAGE_WORKLOAD,
                                            blank=True)
    WORKLOAD_OPTIONS = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-time')
    ]
    full_or_part_time = models.CharField(max_length=9,
                                         choices=WORKLOAD_OPTIONS,
                                         blank=True)
    class Meta:
        verbose_name_plural = 'equivalencies'
    def __str__(self):
        return self.full_or_part_time

class Job_category(models.Model):
    JOB_CATEGORY_CHOICES = [
        ('CEO', 'CEO'),
        ('EXC', 'Executives'),
        ('EL/HS', 'Entity Leader/Head of School'),
        ('EDL/DP', 'Entity Divisional Leader/Divisional Principal'),
        ('D/HD', 'Director/Head of department'),
        ('M/LT', 'Manager/Lead Teacher'),
        ('S/T', 'Specialist/Teacher'),
        ('S/CT2', 'Supervisor/Co-Teacher 2'),
        ('AS/CT1', 'Assistant Supervisor/Co-Teacher 1'),
        ('PAS', 'Professional Assistant or Support'),
        ('A/TA', 'Assistant/Teaching Assistant'),
        ('GA', 'General Assistant'),
        ('GS', 'General Support')
    ]
    job_category = models.CharField(
        max_length=30,
        choices=JOB_CATEGORY_CHOICES,
        default='CEO'
    )
    job_category_code = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Job categories'
    def __str__(self):
        return self.job_category_name

#Emergency Contact Tables

class Emergency(models.Model):
    contact_name = models.CharField(max_length=255)
    contact_email_address = models.EmailField(max_length=254, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, null=True)
    IN_OUT_COUNTRY = [
        ('IC', 'In Country'),
        ('OC', 'Out of Country')
    ]
    in_or_out_of_county = models.CharField(max_length=10,
                                           choices=IN_OUT_COUNTRY,
                                           blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'Emergency Contacts'
    def __str__(self):
        return self.contact_name

class Family(models.Model):
    family_name = models.CharField(max_length=255, blank=True)
    class Meta:
        verbose_name_plural = 'Families'
    def __str__(self):
        return self.family_name

#Tables that have multiple foreign keys from tables that need to be created prior

class User(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    preferred_name = models.CharField(max_length=255, blank=True)
    native_language_name = models.CharField(max_length=255, blank=True)
    maiden_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    personal_email_address = models.EmailField(max_length=254, blank=True)
    work_email_address = models.EmailField(max_length=254, blank=True)
    ssn = models.CharField(max_length=20, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    entity = models.ForeignKey(Entity, on_delete=models.SET_NULL, blank=True, null=True)
    employment_status = models.ForeignKey(Employment_status, on_delete=models.SET_NULL, blank=True, null=True)
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.preferred_name + self.last_name

#Immigration Tables

class Immigration(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('P', 'Passport'),
        ('V', 'Visa'),
        ('WP', 'Work Permit')
    ]
    document_type = models.CharField(max_length=255,
                                     choices=DOCUMENT_TYPE_CHOICES,
                                     blank=True)
    visa_number = models.CharField(max_length=255, blank=True)
    passport_number = models.CharField(max_length=255, blank=True)
    work_permit_number = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    issued_by = models.CharField(max_length=255, blank=True)
    issued_date = models.DateField()
    expiry_date = models.DateField()
    VISA_TYPE_CHOICES = [
        ('APEC', 'APEC商务旅行卡(s)'),
        ('URVSE', 'UAE Residence Visa sponsored by Entity'),
        ('URVSF', 'UAE Residence Visa sponsored by Family'),
        ('R', '人才签证(R)'),
        ('TL', '停留证件(TL)'),
        ('JL', '居留证件(JL)'),
        ('Z', '工作签证(Z)'),
        ('L', '旅游签证(L)'),
        ('S2', '短期私人事务签证(S2)'),
        ('YQ', '签证延期(YQ)'),
        ('F', '访问签证(F)'),
        ('M', '贸易签证(M)'),
        ('S1', '长期私人事务签证(S1)')
    ]
    visa_type = models.CharField(max_length=255,
                                 choices=VISA_TYPE_CHOICES,
                                 blank=True)
    duration = models.IntegerField()
    WORK_PERMIT_CHOICES = [
        ('A', 'China(A)'),
        ('B', 'China(B)'),
        ('C', 'China(C)'),
        ('E', 'China(工作许可通知书)'),
        ('UAE', 'UAE')
    ]
    work_permit_type = models.CharField(max_length=255,
                                        choices=WORK_PERMIT_CHOICES,
                                        blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    last_entry_date = models.DateField()
    comment = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'Immigration documents'
    def __str__(self):
        return self.passport_number

#Join tables (or 'through' tables, as Django calls them)

class Emergency_user(models.Model):
    emergency = models.ForeignKey(Emergency, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contact_user_relationship = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Emergency Contacts and Users'
    def __str__(self):
        return self.user + self.emergency

#Salary Tables
class Pay_grade(models.Model):
    PAY_GRADE_CHOICES = [
        ('D', 'Director'),
        ('T', 'Teacher')
    ]
    pay_grade_type = models.CharField(max_length=20,
                                      choices=PAY_GRADE_CHOICES,
                                      blank=True)
    class Meta:
        verbose_name_plural = 'Pay Grades'
    def __str__(self):
        return self.pay_grade_type

class Currency(models.Model):
    #Add choices here: USD, RMB, AED
    CURRENCY_CHOICES = [
        ('USD', 'United States Dollar'),
        ('RMB', 'Chinese Yuan Renminbi'),
        ('AED', 'United Arab Emirates Dirham')
    ]
    currency_type = models.CharField(max_length=20,
                                     choices=CURRENCY_CHOICES,
                                     blank=True)
    class Meta:
        verbose_name_plural = 'Currencies'
    def __str__(self):
        return self.currency_type

class Salary(models.Model):
    gross_salary = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'Salaries'
    def __str__(self):
        return self.salary

class Identification(models.Model):
    IDENTIFICATION_TYPE_CHOICES = [
        ('China', 'Chinese'),
        ('UAE', 'Emirati'),
    ]
    identification_type = models.CharField(
        max_length=30,
        choices=IDENTIFICATION_TYPE_CHOICES,
        default='Chinese'
    )
    identification_number = models.CharField(max_length=255, blank=True)
    issuing_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    issued_date = models.DateField()
    expiry_date = models.DateField()
    chinese_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='chinese_address')
    chinese_minority = models.CharField(max_length=255, blank=True)
    identification_issued_by = models.CharField(max_length=255, blank=True)
    hukou_type = models.CharField(max_length=255, blank=True)
    hukou_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='hukou_address')
    hukou_city = models.CharField(max_length=255, blank=True)
    hukou_issued_by = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.identification_number + self.user

class Job_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employment_type = models.ForeignKey(Employment_type, on_delete=models.CASCADE)
    equivalency = models.ForeignKey(Equivalency, on_delete=models.CASCADE)
    job_category = models.ForeignKey(Job_category, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now)
    effective_date = models.DateTimeField(null=True)
    end_date = models.DateField(null=True)
    class Meta:
        verbose_name_plural = 'Job Instances'
    def __str__(self):
        return self.user + self.job + self.entity

class Phone_user(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(Contact_type, on_delete=models.CASCADE, null=True)
    active = models.BooleanField()
    class Meta:
        verbose_name_plural = 'Employee Phones'
    def __str__(self):
        return self.user + self.phone

#Qualifications Tables

class Work_experience(models.Model):
    organization = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    creditable = models.BooleanField()
    class Meta:
        verbose_name_plural = 'Work Experiences'
    def __str__(self):
        return self.organization + self.user

class Language(models.Model):
    LANGUAGE_CHOICES_ONE = [
        ('ENG', 'English'),
        ('CHN', 'Mandarin'),
        ('CHN', 'Cantonese'),
        ('JPN', 'Japanese'),
        ('HIN', 'Hindi'),
        ('SPN', 'Spanish'),
        ('FRN', 'French'),
        ('ARB', 'Arabic'),
        ('BNG', 'Bengali'),
        ('RSN', 'Russian'),
        ('PTG', 'Portuguese'),
        ('IND', 'Indonesian')
    ]
    language = models.CharField(max_length=255,
                                choices=LANGUAGE_CHOICES_ONE,
                                blank=True)
    def __str__(self):
        return self.language

class Language_user(models.Model):
    LANGUAGE_CHOICES_TWO = [
        ('ENG', 'English'),
        ('CHN', 'Mandarin'),
        ('CHN', 'Cantonese'),
        ('JPN', 'Japanese'),
        ('HIN', 'Hindi'),
        ('SPN', 'Spanish'),
        ('FRN', 'French'),
        ('ARB', 'Arabic'),
        ('BNG', 'Bengali'),
        ('RSN', 'Russian'),
        ('PTG', 'Portuguese'),
        ('IND', 'Indonesian')
    ]
    language = models.ForeignKey(Language,
                                 choices=LANGUAGE_CHOICES_TWO,
                                 on_delete=models.SET_NULL,
                                 null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    SKILLS_CHOICES = [
        ('R', 'Reading'),
        ('W', 'Writing'),
        ('S', 'Speaking')
    ]
    skill = models.CharField(max_length=20,
                             choices=SKILLS_CHOICES,
                             blank=True)
    FLUENCY_CHOICES = [
        ('P', 'Poor'),
        ('B', 'Basic'),
        ('G', 'Good'),
        ('MT', 'Mother Tongue')
    ]
    fluency = models.CharField(max_length=20,
                               choices=FLUENCY_CHOICES,
                               blank=True)
    comment = models.CharField(max_length=255, blank=True)
    class Meta:
        verbose_name_plural = 'Languages spoken'
    def __str__(self):
        return self.language + self.user

class License(models.Model):
    LICENSE_CHOICES = [
        ('D', 'Class D'),
        ('DJ', 'Junior License'),
        ('A', 'Commercial Class A'),
        ('B', 'Commercial Class B'),
        ('C', 'Commercial Class C'),
        ('TL', 'Taxi and Livery'),
        ('M', 'Motorcycle')
    ]
    license_type = models.CharField(max_length=255,
                                    choices=LICENSE_CHOICES,
                                    blank=True)
    issuing_organization = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.license_type

class License_user(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=255, blank=True)
    issued_date = models.DateField()
    expiry_date = models.DateField()
    #attachments
    class Meta:
        verbose_name_plural = 'Users Licenses'
    def __str__(self):
        return self.license + self.user

#Education Tables
class Concentration_major(models.Model):
    #Add choices for major or minor
    concentration = models.ForeignKey(Concentration, on_delete=models.CASCADE)
    major_or_minor = models.CharField(max_length=5, blank=True)
    class Meta:
        verbose_name_plural = 'Concentrations and Majors'
    def __str__(self):
        return self.concentration + self.major_or_minor

class University_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    start_date = models.DateField()
    graduation_date = models.DateField()
    class Meta:
        verbose_name_plural = 'Users and Universities'
    def __str__(self):
        return self.user + self.university

class University_user_concentration_major(models.Model):
    university_user = models.ForeignKey(University_user, on_delete=models.CASCADE)
    concentration_major = models.ForeignKey(Concentration_major, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Educational Histories'
    def __str__(self):
        return self.university_user + self.concentration_major