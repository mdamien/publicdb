----USING DEV SETTINGS-----
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# ./manage.py dumpscript
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    # You probably want to uncomment on of these two lines
    # @transaction.atomic  # Django 1.6
    # @transaction.commit_on_success  # Django <1.6
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        #you will probably want to call this method from save_or_locate()
        #example:
        #new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        #You may change this function to do specific lookup for specific objects
        #
        #original_class class of the django orm's object that needs to be located
        #original_pk_name the primary key of original_class
        #the_class      parent class of original_class which contains obj_content
        #pk_name        the primary key of original_class
        #pk_value       value of the primary_key
        #obj_content    content of the object which was not exported.
        #
        #you should use obj_content to locate the object on the target db
        #
        #and example where original_class and the_class are different is
        #when original_class is Farmer and
        #the_class is Person. The table may refer to a Farmer but you will actually
        #need to locate Person in order to instantiate that Farmer
        #
        #example:
        #if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #    pk_name="name"
        #    pk_value=obj_content[pk_name]
        #if the_class == StaffGroup:
        #    pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        #change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    #we need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    #has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    if str(e) == "No module named import_helper":
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    #initial imports

    #Processing model: Permission

    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = 'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = 'add_logentry'
    auth_permission_1 = importer.save_or_locate(auth_permission_1)

    auth_permission_2 = Permission()
    auth_permission_2.name = 'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = 'change_logentry'
    auth_permission_2 = importer.save_or_locate(auth_permission_2)

    auth_permission_3 = Permission()
    auth_permission_3.name = 'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = 'delete_logentry'
    auth_permission_3 = importer.save_or_locate(auth_permission_3)

    auth_permission_4 = Permission()
    auth_permission_4.name = 'Can add group'
    auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_4.codename = 'add_group'
    auth_permission_4 = importer.save_or_locate(auth_permission_4)

    auth_permission_5 = Permission()
    auth_permission_5.name = 'Can change group'
    auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_5.codename = 'change_group'
    auth_permission_5 = importer.save_or_locate(auth_permission_5)

    auth_permission_6 = Permission()
    auth_permission_6.name = 'Can delete group'
    auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_6.codename = 'delete_group'
    auth_permission_6 = importer.save_or_locate(auth_permission_6)

    auth_permission_7 = Permission()
    auth_permission_7.name = 'Can add permission'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_7.codename = 'add_permission'
    auth_permission_7 = importer.save_or_locate(auth_permission_7)

    auth_permission_8 = Permission()
    auth_permission_8.name = 'Can change permission'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_8.codename = 'change_permission'
    auth_permission_8 = importer.save_or_locate(auth_permission_8)

    auth_permission_9 = Permission()
    auth_permission_9.name = 'Can delete permission'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_9.codename = 'delete_permission'
    auth_permission_9 = importer.save_or_locate(auth_permission_9)

    auth_permission_10 = Permission()
    auth_permission_10.name = 'Can add user'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_10.codename = 'add_user'
    auth_permission_10 = importer.save_or_locate(auth_permission_10)

    auth_permission_11 = Permission()
    auth_permission_11.name = 'Can change user'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_11.codename = 'change_user'
    auth_permission_11 = importer.save_or_locate(auth_permission_11)

    auth_permission_12 = Permission()
    auth_permission_12.name = 'Can delete user'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_12.codename = 'delete_user'
    auth_permission_12 = importer.save_or_locate(auth_permission_12)

    auth_permission_13 = Permission()
    auth_permission_13.name = 'Can add content type'
    auth_permission_13.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_13.codename = 'add_contenttype'
    auth_permission_13 = importer.save_or_locate(auth_permission_13)

    auth_permission_14 = Permission()
    auth_permission_14.name = 'Can change content type'
    auth_permission_14.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_14.codename = 'change_contenttype'
    auth_permission_14 = importer.save_or_locate(auth_permission_14)

    auth_permission_15 = Permission()
    auth_permission_15.name = 'Can delete content type'
    auth_permission_15.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_15.codename = 'delete_contenttype'
    auth_permission_15 = importer.save_or_locate(auth_permission_15)

    auth_permission_16 = Permission()
    auth_permission_16.name = 'Can add api'
    auth_permission_16.content_type = ContentType.objects.get(app_label="datasets", model="api")
    auth_permission_16.codename = 'add_api'
    auth_permission_16 = importer.save_or_locate(auth_permission_16)

    auth_permission_17 = Permission()
    auth_permission_17.name = 'Can change api'
    auth_permission_17.content_type = ContentType.objects.get(app_label="datasets", model="api")
    auth_permission_17.codename = 'change_api'
    auth_permission_17 = importer.save_or_locate(auth_permission_17)

    auth_permission_18 = Permission()
    auth_permission_18.name = 'Can delete api'
    auth_permission_18.content_type = ContentType.objects.get(app_label="datasets", model="api")
    auth_permission_18.codename = 'delete_api'
    auth_permission_18 = importer.save_or_locate(auth_permission_18)

    auth_permission_19 = Permission()
    auth_permission_19.name = 'Can add instance'
    auth_permission_19.content_type = ContentType.objects.get(app_label="datasets", model="instance")
    auth_permission_19.codename = 'add_instance'
    auth_permission_19 = importer.save_or_locate(auth_permission_19)

    auth_permission_20 = Permission()
    auth_permission_20.name = 'Can change instance'
    auth_permission_20.content_type = ContentType.objects.get(app_label="datasets", model="instance")
    auth_permission_20.codename = 'change_instance'
    auth_permission_20 = importer.save_or_locate(auth_permission_20)

    auth_permission_21 = Permission()
    auth_permission_21.name = 'Can delete instance'
    auth_permission_21.content_type = ContentType.objects.get(app_label="datasets", model="instance")
    auth_permission_21.codename = 'delete_instance'
    auth_permission_21 = importer.save_or_locate(auth_permission_21)

    auth_permission_22 = Permission()
    auth_permission_22.name = 'Can add klass'
    auth_permission_22.content_type = ContentType.objects.get(app_label="datasets", model="klass")
    auth_permission_22.codename = 'add_klass'
    auth_permission_22 = importer.save_or_locate(auth_permission_22)

    auth_permission_23 = Permission()
    auth_permission_23.name = 'Can change klass'
    auth_permission_23.content_type = ContentType.objects.get(app_label="datasets", model="klass")
    auth_permission_23.codename = 'change_klass'
    auth_permission_23 = importer.save_or_locate(auth_permission_23)

    auth_permission_24 = Permission()
    auth_permission_24.name = 'Can delete klass'
    auth_permission_24.content_type = ContentType.objects.get(app_label="datasets", model="klass")
    auth_permission_24.codename = 'delete_klass'
    auth_permission_24 = importer.save_or_locate(auth_permission_24)

    auth_permission_25 = Permission()
    auth_permission_25.name = 'Can add session'
    auth_permission_25.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_25.codename = 'add_session'
    auth_permission_25 = importer.save_or_locate(auth_permission_25)

    auth_permission_26 = Permission()
    auth_permission_26.name = 'Can change session'
    auth_permission_26.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_26.codename = 'change_session'
    auth_permission_26 = importer.save_or_locate(auth_permission_26)

    auth_permission_27 = Permission()
    auth_permission_27.name = 'Can delete session'
    auth_permission_27.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_27.codename = 'delete_session'
    auth_permission_27 = importer.save_or_locate(auth_permission_27)

    auth_permission_28 = Permission()
    auth_permission_28.name = 'Can add api access'
    auth_permission_28.content_type = ContentType.objects.get(app_label="tastypie", model="apiaccess")
    auth_permission_28.codename = 'add_apiaccess'
    auth_permission_28 = importer.save_or_locate(auth_permission_28)

    auth_permission_29 = Permission()
    auth_permission_29.name = 'Can change api access'
    auth_permission_29.content_type = ContentType.objects.get(app_label="tastypie", model="apiaccess")
    auth_permission_29.codename = 'change_apiaccess'
    auth_permission_29 = importer.save_or_locate(auth_permission_29)

    auth_permission_30 = Permission()
    auth_permission_30.name = 'Can delete api access'
    auth_permission_30.content_type = ContentType.objects.get(app_label="tastypie", model="apiaccess")
    auth_permission_30.codename = 'delete_apiaccess'
    auth_permission_30 = importer.save_or_locate(auth_permission_30)

    auth_permission_31 = Permission()
    auth_permission_31.name = 'Can add api key'
    auth_permission_31.content_type = ContentType.objects.get(app_label="tastypie", model="apikey")
    auth_permission_31.codename = 'add_apikey'
    auth_permission_31 = importer.save_or_locate(auth_permission_31)

    auth_permission_32 = Permission()
    auth_permission_32.name = 'Can change api key'
    auth_permission_32.content_type = ContentType.objects.get(app_label="tastypie", model="apikey")
    auth_permission_32.codename = 'change_apikey'
    auth_permission_32 = importer.save_or_locate(auth_permission_32)

    auth_permission_33 = Permission()
    auth_permission_33.name = 'Can delete api key'
    auth_permission_33.content_type = ContentType.objects.get(app_label="tastypie", model="apikey")
    auth_permission_33.codename = 'delete_apikey'
    auth_permission_33 = importer.save_or_locate(auth_permission_33)

    #Processing model: Group

    from django.contrib.auth.models import Group


    #Processing model: User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = 'pbkdf2_sha256$12000$5zRIXSMrV09W$5pLqQt9wLkNiB0ZqH/3DJFFgz7CZbLvD4oqRhEzcJNQ='
    auth_user_1.last_login = dateutil.parser.parse("2014-03-30T22:59:33.575549+00:00")
    auth_user_1.is_superuser = True
    auth_user_1.username = 'tic'
    auth_user_1.first_name = ''
    auth_user_1.last_name = ''
    auth_user_1.email = 't@tt.tt'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.date_joined = dateutil.parser.parse("2014-03-30T03:30:36.118682+00:00")
    auth_user_1 = importer.save_or_locate(auth_user_1)

    #Processing model: Session

    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = 'sgui0ro1aj3fd7sb7lnxscxmn8p0rof6'
    django_session_1.session_data = 'YTdiYmY5M2UzY2I1YTIyNjFmMTc5OTJjMmJkZmY4MGY1ODNmOTgyNDp7fQ=='
    django_session_1.expire_date = dateutil.parser.parse("2014-04-13T03:32:11.681143+00:00")
    django_session_1 = importer.save_or_locate(django_session_1)

    django_session_2 = Session()
    django_session_2.session_key = '5xptex7tkvicz7gv0oco23l03x88cdnm'
    django_session_2.session_data = 'OTdiNTY1MDliZmNlYzk1MTRjNGI5ZDQ2MzRiY2NjNTAzZGJkYmU1NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0='
    django_session_2.expire_date = dateutil.parser.parse("2014-04-13T22:59:33.683025+00:00")
    django_session_2 = importer.save_or_locate(django_session_2)

    #Processing model: API

    from datasets.models import API

    datasets_api_1 = API()
    datasets_api_1.name = 'Blog'
    datasets_api_1.slug = 'blog'
    datasets_api_1.owner = auth_user_1
    datasets_api_1.meta = {}
    datasets_api_1.created = dateutil.parser.parse("2014-03-30T15:59:18.253066+00:00")
    datasets_api_1 = importer.save_or_locate(datasets_api_1)

    datasets_api_2 = API()
    datasets_api_2.name = 'Cat social graph'
    datasets_api_2.slug = 'cat-social'
    datasets_api_2.owner = auth_user_1
    datasets_api_2.meta = {}
    datasets_api_2.created = dateutil.parser.parse("2014-03-30T19:29:48.790673+00:00")
    datasets_api_2 = importer.save_or_locate(datasets_api_2)

    datasets_api_3 = API()
    datasets_api_3.name = 'Places'
    datasets_api_3.slug = 'places'
    datasets_api_3.owner = auth_user_1
    datasets_api_3.meta = {}
    datasets_api_3.created = dateutil.parser.parse("2014-03-30T21:29:25.284826+00:00")
    datasets_api_3 = importer.save_or_locate(datasets_api_3)

    datasets_api_4 = API()
    datasets_api_4.name = 'hihi'
    datasets_api_4.slug = 'hiho'
    datasets_api_4.owner = auth_user_1
    datasets_api_4.meta = {}
    datasets_api_4.created = dateutil.parser.parse("2014-03-31T00:13:20.489644+00:00")
    datasets_api_4 = importer.save_or_locate(datasets_api_4)

    datasets_api_5 = API()
    datasets_api_5.name = 'qdsdsq'
    datasets_api_5.slug = 'sdsd'
    datasets_api_5.owner = auth_user_1
    datasets_api_5.meta = {}
    datasets_api_5.created = dateutil.parser.parse("2014-03-31T00:28:37.271181+00:00")
    datasets_api_5 = importer.save_or_locate(datasets_api_5)

    datasets_api_6 = API()
    datasets_api_6.name = 'sqd'
    datasets_api_6.slug = 'qd'
    datasets_api_6.owner = auth_user_1
    datasets_api_6.meta = {}
    datasets_api_6.created = dateutil.parser.parse("2014-03-31T02:19:53.917611+00:00")
    datasets_api_6 = importer.save_or_locate(datasets_api_6)

    datasets_api_7 = API()
    datasets_api_7.name = 'test'
    datasets_api_7.slug = 'test'
    datasets_api_7.owner = auth_user_1
    datasets_api_7.meta = {}
    datasets_api_7.created = dateutil.parser.parse("2014-03-30T22:59:58.760718+00:00")
    datasets_api_7 = importer.save_or_locate(datasets_api_7)

    #Processing model: Klass

    from datasets.models import Klass

    datasets_klass_1 = Klass()
    datasets_klass_1.api = datasets_api_1
    datasets_klass_1.name = 'Article'
    datasets_klass_1.slug = 'article'
    datasets_klass_1.validation = ''
    datasets_klass_1.meta = {}
    datasets_klass_1.created = dateutil.parser.parse("2014-03-30T15:59:41.070689+00:00")
    datasets_klass_1 = importer.save_or_locate(datasets_klass_1)

    datasets_klass_2 = Klass()
    datasets_klass_2.api = datasets_api_2
    datasets_klass_2.name = 'Cat'
    datasets_klass_2.slug = 'cat'
    datasets_klass_2.validation = ''
    datasets_klass_2.meta = {}
    datasets_klass_2.created = dateutil.parser.parse("2014-03-30T19:31:09.942245+00:00")
    datasets_klass_2 = importer.save_or_locate(datasets_klass_2)

    datasets_klass_3 = Klass()
    datasets_klass_3.api = datasets_api_2
    datasets_klass_3.name = 'Friendship'
    datasets_klass_3.slug = 'friendship'
    datasets_klass_3.validation = ''
    datasets_klass_3.meta = {}
    datasets_klass_3.created = dateutil.parser.parse("2014-03-30T19:37:06.870895+00:00")
    datasets_klass_3 = importer.save_or_locate(datasets_klass_3)

    datasets_klass_4 = Klass()
    datasets_klass_4.api = datasets_api_3
    datasets_klass_4.name = 'Place'
    datasets_klass_4.slug = 'place'
    datasets_klass_4.validation = ''
    datasets_klass_4.meta = {}
    datasets_klass_4.created = dateutil.parser.parse("2014-03-30T21:29:41.386361+00:00")
    datasets_klass_4 = importer.save_or_locate(datasets_klass_4)

    datasets_klass_5 = Klass()
    datasets_klass_5.api = datasets_api_7
    datasets_klass_5.name = 'hello'
    datasets_klass_5.slug = 'world'
    datasets_klass_5.validation = ''
    datasets_klass_5.meta = {}
    datasets_klass_5.created = dateutil.parser.parse("2014-03-30T23:27:40.434625+00:00")
    datasets_klass_5 = importer.save_or_locate(datasets_klass_5)

    #Processing model: Instance

    from datasets.models import Instance

    datasets_instance_1 = Instance()
    datasets_instance_1.created = dateutil.parser.parse("2014-03-30T16:01:00.627314+00:00")
    datasets_instance_1.modified = dateutil.parser.parse("2014-03-30T18:57:39.072409+00:00")
    datasets_instance_1.klass = datasets_klass_1
    datasets_instance_1.data = "## This is my first article\r\n\r\nWoahh..too much pressure! \r\n\r\nNo, I won't put a lorem ipsum! Nobody likes it!"
    datasets_instance_1 = importer.save_or_locate(datasets_instance_1)

    datasets_instance_2 = Instance()
    datasets_instance_2.created = dateutil.parser.parse("2014-03-30T16:03:58.030655+00:00")
    datasets_instance_2.modified = dateutil.parser.parse("2014-03-30T16:03:58.127436+00:00")
    datasets_instance_2.klass = datasets_klass_1
    datasets_instance_2.data = "## How to grow your startup like a banana ?\r\n\r\nI'm happy to share the answer in my book **Banana & Banana**. It's only 500 pages to make one point! "
    datasets_instance_2 = importer.save_or_locate(datasets_instance_2)

    datasets_instance_3 = Instance()
    datasets_instance_3.created = dateutil.parser.parse("2014-03-30T16:04:12.180211+00:00")
    datasets_instance_3.modified = dateutil.parser.parse("2014-03-30T16:04:12.253401+00:00")
    datasets_instance_3.klass = datasets_klass_1
    datasets_instance_3.data = '## This is fun?\r\n\r\nMaybe!'
    datasets_instance_3 = importer.save_or_locate(datasets_instance_3)

    datasets_instance_4 = Instance()
    datasets_instance_4.created = dateutil.parser.parse("2014-03-30T18:58:55.040437+00:00")
    datasets_instance_4.modified = dateutil.parser.parse("2014-03-30T18:58:55.114644+00:00")
    datasets_instance_4.klass = datasets_klass_1
    datasets_instance_4.data = "##Markdown example from J. Gruber\r\nNow is the time for all good men to come to\r\nthe aid of their country. This is just a\r\nregular paragraph.\r\n\r\nThe quick brown fox jumped over the lazy\r\ndog's back.\r\n\r\n### Header 3\r\n\r\n> This is a blockquote.\r\n> \r\n> This is the second paragraph in the blockquote.\r\n>\r\n> ## This is an H2 in a blockquote"
    datasets_instance_4 = importer.save_or_locate(datasets_instance_4)

    datasets_instance_5 = Instance()
    datasets_instance_5.created = dateutil.parser.parse("2014-03-30T19:33:17.908179+00:00")
    datasets_instance_5.modified = dateutil.parser.parse("2014-03-30T19:34:00.534757+00:00")
    datasets_instance_5.klass = datasets_klass_2
    datasets_instance_5.data = 'Rasputin\r\nhttp://i.imgur.com/IUfsijF.jpg'
    datasets_instance_5 = importer.save_or_locate(datasets_instance_5)

    datasets_instance_6 = Instance()
    datasets_instance_6.created = dateutil.parser.parse("2014-03-30T19:34:35.233645+00:00")
    datasets_instance_6.modified = dateutil.parser.parse("2014-03-30T19:34:35.312114+00:00")
    datasets_instance_6.klass = datasets_klass_2
    datasets_instance_6.data = 'Princess\r\nhttp://i.imgur.com/4yJh4xN.jpg'
    datasets_instance_6 = importer.save_or_locate(datasets_instance_6)

    datasets_instance_7 = Instance()
    datasets_instance_7.created = dateutil.parser.parse("2014-03-30T19:34:54.540611+00:00")
    datasets_instance_7.modified = dateutil.parser.parse("2014-03-30T19:34:54.602738+00:00")
    datasets_instance_7.klass = datasets_klass_2
    datasets_instance_7.data = 'José\r\nhttp://i.imgur.com/XTkLM1i.jpg'
    datasets_instance_7 = importer.save_or_locate(datasets_instance_7)

    datasets_instance_8 = Instance()
    datasets_instance_8.created = dateutil.parser.parse("2014-03-30T19:35:29.956282+00:00")
    datasets_instance_8.modified = dateutil.parser.parse("2014-03-30T19:35:30.039381+00:00")
    datasets_instance_8.klass = datasets_klass_2
    datasets_instance_8.data = 'Nova\r\nhttp://i.imgur.com/XHhW2JC.png'
    datasets_instance_8 = importer.save_or_locate(datasets_instance_8)

    datasets_instance_9 = Instance()
    datasets_instance_9.created = dateutil.parser.parse("2014-03-30T19:35:51.264340+00:00")
    datasets_instance_9.modified = dateutil.parser.parse("2014-03-30T19:35:51.344116+00:00")
    datasets_instance_9.klass = datasets_klass_2
    datasets_instance_9.data = 'Biffa\r\nhttp://i.imgur.com/3ZfkTfG.jpg'
    datasets_instance_9 = importer.save_or_locate(datasets_instance_9)

    datasets_instance_10 = Instance()
    datasets_instance_10.created = dateutil.parser.parse("2014-03-30T19:38:32.212193+00:00")
    datasets_instance_10.modified = dateutil.parser.parse("2014-03-30T19:38:32.274953+00:00")
    datasets_instance_10.klass = datasets_klass_3
    datasets_instance_10.data = '18-14'
    datasets_instance_10 = importer.save_or_locate(datasets_instance_10)

    datasets_instance_11 = Instance()
    datasets_instance_11.created = dateutil.parser.parse("2014-03-30T19:38:46.238494+00:00")
    datasets_instance_11.modified = dateutil.parser.parse("2014-03-30T19:38:46.299325+00:00")
    datasets_instance_11.klass = datasets_klass_3
    datasets_instance_11.data = '16-17'
    datasets_instance_11 = importer.save_or_locate(datasets_instance_11)

    datasets_instance_12 = Instance()
    datasets_instance_12.created = dateutil.parser.parse("2014-03-30T19:38:57.788468+00:00")
    datasets_instance_12.modified = dateutil.parser.parse("2014-03-30T19:38:57.895602+00:00")
    datasets_instance_12.klass = datasets_klass_3
    datasets_instance_12.data = '15-16'
    datasets_instance_12 = importer.save_or_locate(datasets_instance_12)

    datasets_instance_13 = Instance()
    datasets_instance_13.created = dateutil.parser.parse("2014-03-30T19:39:05.389088+00:00")
    datasets_instance_13.modified = dateutil.parser.parse("2014-03-30T19:39:05.479870+00:00")
    datasets_instance_13.klass = datasets_klass_3
    datasets_instance_13.data = '14-17'
    datasets_instance_13 = importer.save_or_locate(datasets_instance_13)

    datasets_instance_14 = Instance()
    datasets_instance_14.created = dateutil.parser.parse("2014-03-30T19:39:14.769326+00:00")
    datasets_instance_14.modified = dateutil.parser.parse("2014-03-30T19:39:14.846752+00:00")
    datasets_instance_14.klass = datasets_klass_3
    datasets_instance_14.data = '18-15'
    datasets_instance_14 = importer.save_or_locate(datasets_instance_14)

    datasets_instance_15 = Instance()
    datasets_instance_15.created = dateutil.parser.parse("2014-03-30T19:39:35.383628+00:00")
    datasets_instance_15.modified = dateutil.parser.parse("2014-03-30T19:39:35.488874+00:00")
    datasets_instance_15.klass = datasets_klass_3
    datasets_instance_15.data = '17-18'
    datasets_instance_15 = importer.save_or_locate(datasets_instance_15)

    datasets_instance_16 = Instance()
    datasets_instance_16.created = dateutil.parser.parse("2014-03-30T21:31:40.269695+00:00")
    datasets_instance_16.modified = dateutil.parser.parse("2014-03-30T21:31:40.351497+00:00")
    datasets_instance_16.klass = datasets_klass_4
    datasets_instance_16.data = 'Brooklyn Museum\r\n40.671064\r\n-73.963201'
    datasets_instance_16 = importer.save_or_locate(datasets_instance_16)

    datasets_instance_17 = Instance()
    datasets_instance_17.created = dateutil.parser.parse("2014-03-30T21:33:21.733424+00:00")
    datasets_instance_17.modified = dateutil.parser.parse("2014-03-30T21:33:21.824740+00:00")
    datasets_instance_17.klass = datasets_klass_4
    datasets_instance_17.data = 'Rye\r\n-73.963201\r\n0.733150'
    datasets_instance_17 = importer.save_or_locate(datasets_instance_17)

    datasets_instance_18 = Instance()
    datasets_instance_18.created = dateutil.parser.parse("2014-03-30T21:35:24.057151+00:00")
    datasets_instance_18.modified = dateutil.parser.parse("2014-03-30T21:35:24.105842+00:00")
    datasets_instance_18.klass = datasets_klass_4
    datasets_instance_18.data = 'Pont de Pont-Sainte-Maxence\r\n49.302862\r\n2.604369'
    datasets_instance_18 = importer.save_or_locate(datasets_instance_18)

    datasets_instance_19 = Instance()
    datasets_instance_19.created = dateutil.parser.parse("2014-03-30T21:37:48.383614+00:00")
    datasets_instance_19.modified = dateutil.parser.parse("2014-03-30T21:37:48.489082+00:00")
    datasets_instance_19.klass = datasets_klass_4
    datasets_instance_19.data = 'Etretat\r\n49.707258\r\n0.193377'
    datasets_instance_19 = importer.save_or_locate(datasets_instance_19)

    #Processing model: ApiAccess

    from tastypie.models import ApiAccess


    #Processing model: ApiKey

    from tastypie.models import ApiKey


    #Processing model: LogEntry

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = dateutil.parser.parse("2014-03-30T19:40:49.461492+00:00")
    django_admin_log_1.user = auth_user_1
    django_admin_log_1.content_type = ContentType.objects.get(app_label="datasets", model="api")
    django_admin_log_1.object_id = '2'
    django_admin_log_1.object_repr = 'Blog'
    django_admin_log_1.action_flag = 2
    django_admin_log_1.change_message = 'Changed name and meta.'
    django_admin_log_1 = importer.save_or_locate(django_admin_log_1)

    django_admin_log_2 = LogEntry()
    django_admin_log_2.action_time = dateutil.parser.parse("2014-03-30T19:40:36.445094+00:00")
    django_admin_log_2.user = auth_user_1
    django_admin_log_2.content_type = ContentType.objects.get(app_label="datasets", model="api")
    django_admin_log_2.object_id = '1'
    django_admin_log_2.object_repr = 'Library'
    django_admin_log_2.action_flag = 3
    django_admin_log_2.change_message = ''
    django_admin_log_2 = importer.save_or_locate(django_admin_log_2)

