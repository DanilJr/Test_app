from django.test import TestCase

from datetime import datetime
import pytz
from alias.models import *


class TestAliasModel(TestCase):
    '''
    Class for CustomAlias model test 
    '''

    def set_up(self):
        '''
        Create a alias obj to be used by the tests
        '''
        self.alias1 = Alias.objects.create(id=101, alias='interesting', target='detective', start=datetime.now(pytz.UTC)-timedelta(days=90), end=datetime.now(pytz.UTC)-timedelta(days=40))
        self.alias2 = Alias.objects.create(id=102, alias='kids', target='for_children', start=datetime.now(pytz.UTC)-timedelta(days=60), datetime.now(pytz.UTC)
        self.alias3 = Alias.objects.create(id=103, alias='interesting', target='interesting', start=datetime.now(pytz.UTC)-timedelta(days=30), datetime.now(pytz.UTC)+timedelta(days=20))
        self.alias1.save()
        self.alias2.save()
        self.alias3.save()
# Create your tests here.
