M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py startapp patients

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>mysql -u root -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.21-log MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> drop database monica;
ERROR 1008 (HY000): Can't drop database 'monica'; database doesn't exist
mysql> create database monica;
Query OK, 1 row affected (0.02 sec)

mysql> exit
Bye

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py makemigrations patients
Traceback (most recent call last):
  File "C:\Users\mathenge\M\lib\site-packages\django\db\backends\mysql\base.py", line 15, in <module>
    import MySQLdb as Database
ModuleNotFoundError: No module named 'MySQLdb'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 15, in <module>
    execute_from_command_line(sys.argv)
  File "C:\Users\mathenge\M\lib\site-packages\django\core\management\__init__.py", line 371, in execute_from_command_line
    utility.execute()
  File "C:\Users\mathenge\M\lib\site-packages\django\core\management\__init__.py", line 347, in execute
    django.setup()
  File "C:\Users\mathenge\M\lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "C:\Users\mathenge\M\lib\site-packages\django\apps\registry.py", line 112, in populate
    app_config.import_models()
  File "C:\Users\mathenge\M\lib\site-packages\django\apps\config.py", line 198, in import_models
    self.models_module = import_module(models_module_name)
  File "C:\Users\mathenge\AppData\Local\Programs\Python\Python36-32\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\mathenge\M\lib\site-packages\django\contrib\auth\models.py", line 2, in <module>
    from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
  File "C:\Users\mathenge\M\lib\site-packages\django\contrib\auth\base_user.py", line 47, in <module>
    class AbstractBaseUser(models.Model):
  File "C:\Users\mathenge\M\lib\site-packages\django\db\models\base.py", line 114, in __new__
    new_class.add_to_class('_meta', Options(meta, app_label))
  File "C:\Users\mathenge\M\lib\site-packages\django\db\models\base.py", line 315, in add_to_class
    value.contribute_to_class(cls, name)
  File "C:\Users\mathenge\M\lib\site-packages\django\db\models\options.py", line 205, in contribute_to_class
    self.db_table = truncate_name(self.db_table, connection.ops.max_name_length())
  File "C:\Users\mathenge\M\lib\site-packages\django\db\__init__.py", line 33, in __getattr__
    return getattr(connections[DEFAULT_DB_ALIAS], item)
  File "C:\Users\mathenge\M\lib\site-packages\django\db\utils.py", line 202, in __getitem__
    backend = load_backend(db['ENGINE'])
  File "C:\Users\mathenge\M\lib\site-packages\django\db\utils.py", line 110, in load_backend
    return import_module('%s.base' % backend_name)
  File "C:\Users\mathenge\AppData\Local\Programs\Python\Python36-32\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "C:\Users\mathenge\M\lib\site-packages\django\db\backends\mysql\base.py", line 20, in <module>
    ) from err
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>pip install mysql-python
Collecting mysql-python
  Downloading MySQL-python-1.2.5.zip (108kB)
    100% |████████████████████████████████| 112kB 106kB/s
Installing collected packages: mysql-python
  Running setup.py install for mysql-python ... error
    Complete output from command C:\Users\mathenge\M\Scripts\python.exe -u -c "import setuptools, tokenize;__file__='C:\\Users\\mathenge\\AppData\\Local\\Temp\\pip-build-ua9yzq8u\\my
sql-python\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\mathe
nge\AppData\Local\Temp\pip-zjoxuqum-record\install-record.txt --single-version-externally-managed --compile --install-headers C:\Users\mathenge\M\include\site\python3.6\mysql-python:

    running install
    running build
    running build_py
    creating build
    creating build\lib.win32-3.6
    copying _mysql_exceptions.py -> build\lib.win32-3.6
    creating build\lib.win32-3.6\MySQLdb
    copying MySQLdb\__init__.py -> build\lib.win32-3.6\MySQLdb
    copying MySQLdb\converters.py -> build\lib.win32-3.6\MySQLdb
    copying MySQLdb\connections.py -> build\lib.win32-3.6\MySQLdb
    copying MySQLdb\cursors.py -> build\lib.win32-3.6\MySQLdb
    copying MySQLdb\release.py -> build\lib.win32-3.6\MySQLdb
    copying MySQLdb\times.py -> build\lib.win32-3.6\MySQLdb
    creating build\lib.win32-3.6\MySQLdb\constants
    copying MySQLdb\constants\__init__.py -> build\lib.win32-3.6\MySQLdb\constants
    copying MySQLdb\constants\CR.py -> build\lib.win32-3.6\MySQLdb\constants
    copying MySQLdb\constants\FIELD_TYPE.py -> build\lib.win32-3.6\MySQLdb\constants
    copying MySQLdb\constants\ER.py -> build\lib.win32-3.6\MySQLdb\constants
    copying MySQLdb\constants\FLAG.py -> build\lib.win32-3.6\MySQLdb\constants
    copying MySQLdb\constants\REFRESH.py -> build\lib.win32-3.6\MySQLdb\constants
    copying MySQLdb\constants\CLIENT.py -> build\lib.win32-3.6\MySQLdb\constants
    running build_ext
    building '_mysql' extension
    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools

    ----------------------------------------
Command "C:\Users\mathenge\M\Scripts\python.exe -u -c "import setuptools, tokenize;__file__='C:\\Users\\mathenge\\AppData\\Local\\Temp\\pip-build-ua9yzq8u\\mysql-python\\setup.py';f=
getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\mathenge\AppData\Local\Temp\p
ip-zjoxuqum-record\install-record.txt --single-version-externally-managed --compile --install-headers C:\Users\mathenge\M\include\site\python3.6\mysql-python" failed with error code
1 in C:\Users\mathenge\AppData\Local\Temp\pip-build-ua9yzq8u\mysql-python\

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>pip install mysqlclient
Collecting mysqlclient
  Using cached mysqlclient-1.3.12-cp36-cp36m-win32.whl
Installing collected packages: mysqlclient
Successfully installed mysqlclient-1.3.12

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py makemigrations patients
SystemCheckError: System check identified some issues:

ERRORS:
patients.Patient.doctor_assigned: (fields.E300) Field defines a relation with model 'doctors.Doctor', which is either not installed, or is abstract.
patients.Patient.doctor_assigned: (fields.E307) The field patients.Patient.doctor_assigned was declared with a lazy reference to 'doctors.doctor', but app 'doctors' isn't installed.
patients.Patient.med: (fields.E300) Field defines a relation with model 'medications.Medication', which is either not installed, or is abstract.
patients.Patient.med: (fields.E307) The field patients.Patient.med was declared with a lazy reference to 'medications.medication', but app 'medications' isn't installed.

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py startapp medications

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py startapp doctors

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py makemigrations patients
Migrations for 'doctors':
  doctors\migrations\0001_initial.py
    - Create model Doctor
Migrations for 'medications':
  medications\migrations\0001_initial.py
    - Create model Medication
Migrations for 'patients':
  patients\migrations\0001_initial.py
    - Create model Patient

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py sqlmigrate pa
usage: manage.py sqlmigrate [-h] [--version] [-v {0,1,2,3}]
                            [--settings SETTINGS] [--pythonpath PYTHONPATH]
                            [--traceback] [--no-color] [--database DATABASE]
                            [--backwards]
                            app_label migration_name
manage.py sqlmigrate: error: the following arguments are required: migration_name

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py sqlmigrate patients 0001
BEGIN;
--
-- Create model Patient
--
CREATE TABLE `patients_patient` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(50) NOT NULL, `residence` varchar(50) NOT NULL, `next_of_kin` varchar(50) NOT NULL,
`allergies` varchar(1000) NOT NULL, `past_medical_history` varchar(1000) NOT NULL, `medication_history` varchar(1000) NOT NULL, `doctor_assigned_id` integer NULL, `med_id` integer NU
LL);
ALTER TABLE `patients_patient` ADD CONSTRAINT `patients_patient_doctor_assigned_id_6a56ad79_fk_doctors_d` FOREIGN KEY (`doctor_assigned_id`) REFERENCES `doctors_doctor` (`id`);
ALTER TABLE `patients_patient` ADD CONSTRAINT `patients_patient_med_id_e3368739_fk_medications_medication_id` FOREIGN KEY (`med_id`) REFERENCES `medications_medication` (`id`);
COMMIT;

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, doctors, medications, patients, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying doctors.0001_initial... OK
  Applying medications.0001_initial... OK
  Applying patients.0001_initial... OK
  Applying sessions.0001_initial... OK

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py makemigrations medications
No changes detected in app 'medications'

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>python manage.py makemigrations doctors
No changes detected in app 'doctors'

(M) C:\Users\mathenge\Desktop\projects\STMonica_Admin>^A
