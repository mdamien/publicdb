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
# ./manage.py dumpscript datasets
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
    from django.contrib.auth.models import User

    #Processing model: API

    from datasets.models import API

    datasets_api_1 = API()
    datasets_api_1.name = 'Blog'
    datasets_api_1.slug = 'blog'
    datasets_api_1.owner =  importer.locate_object(User, "id", User, "id", 1, {'username': 'tic', 'last_name': '', 'first_name': '', 'id': 1, 'is_active': True, 'last_login': datetime.datetime(2014, 3, 30, 3, 32, 54, 841742, tzinfo=<UTC>), 'email': 't@tt.tt', 'password': 'pbkdf2_sha256$12000$5zRIXSMrV09W$5pLqQt9wLkNiB0ZqH/3DJFFgz7CZbLvD4oqRhEzcJNQ=', 'is_superuser': True, 'is_staff': True, 'date_joined': datetime.datetime(2014, 3, 30, 3, 30, 36, 118682, tzinfo=<UTC>)} ) 
    datasets_api_1.meta = {}
    datasets_api_1.created = dateutil.parser.parse("2014-03-30T15:59:18.253066+00:00")
    datasets_api_1 = importer.save_or_locate(datasets_api_1)

    datasets_api_2 = API()
    datasets_api_2.name = 'Cat social graph'
    datasets_api_2.slug = 'cat-social'
    datasets_api_2.owner =  importer.locate_object(User, "id", User, "id", 1, {'username': 'tic', 'last_name': '', 'first_name': '', 'id': 1, 'is_active': True, 'last_login': datetime.datetime(2014, 3, 30, 3, 32, 54, 841742, tzinfo=<UTC>), 'email': 't@tt.tt', 'password': 'pbkdf2_sha256$12000$5zRIXSMrV09W$5pLqQt9wLkNiB0ZqH/3DJFFgz7CZbLvD4oqRhEzcJNQ=', 'is_superuser': True, 'is_staff': True, 'date_joined': datetime.datetime(2014, 3, 30, 3, 30, 36, 118682, tzinfo=<UTC>)} ) 
    datasets_api_2.meta = {}
    datasets_api_2.created = dateutil.parser.parse("2014-03-30T19:29:48.790673+00:00")
    datasets_api_2 = importer.save_or_locate(datasets_api_2)

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

