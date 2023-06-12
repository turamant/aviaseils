from django.db import models


class Adult(models.Model):
    title = models.CharField(max_length=20)
    serial_number_passport = models.CharField(max_length=12)
    point_of_issue = models.CharField(max_length=20)
    passenger = models.ForeignKey('Passengers', models.DO_NOTHING)

    class Meta:
        db_table = 'adult'

    def __str__(self):
        return self.title


class Airways(models.Model):
    departure_point = models.CharField(max_length=50)
    airport_departure = models.CharField(max_length=30)
    point_of_arrival = models.CharField(max_length=50)
    point_airport_arrival = models.CharField(max_length=30)
    medium_duration_flight = models.IntegerField()
    company = models.ForeignKey('Companies', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'airways'

    def __str__(self):
        return self.company.name


class Companies(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=18)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name


class Flights(models.Model):
    date_time_departure = models.DateTimeField()
    date_time_arrive = models.DateTimeField()
    status = models.CharField(max_length=20)
    airway = models.ForeignKey(Airways, models.DO_NOTHING)

    class Meta:
        db_table = 'flights'


class Infant(models.Model):
    birth_certificate_nuber = models.CharField(max_length=10)
    age = models.IntegerField()
    lastname_accompanying_person = models.CharField(max_length=50)
    passenger = models.ForeignKey('Passengers', models.DO_NOTHING)

    class Meta:
        db_table = 'infant'


class Passengers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        db_table = 'passengers'

    def __str__(self):
        return self.user.name


class Tickets(models.Model):
    airplane = models.CharField(max_length=20)
    seat = models.IntegerField()
    price = models.IntegerField()
    passenger = models.ForeignKey(Passengers, models.DO_NOTHING)
    flight = models.ForeignKey(Flights, models.DO_NOTHING)
    reservation = models.CharField(max_length=20)

    class Meta:
        db_table = 'tickets'


class Users(models.Model):
    user_type = models.CharField(max_length=15)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    user_email = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.login


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)





class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


