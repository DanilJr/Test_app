from django.db import models, IntegrityError, DataError
from django.urls import reverse
from datetime import datetime, timezone, timedelta
import pytz


class Book(models.Model):
    '''
    This class represents an Book.\n
    Attributes:
    -----------
    param name: Describes name of the book
    type name: str max_length=128
    param slug: Describes the slug
    type slug: str, max_lenght=24, pk
    param author: Describes author's name of the book
    type author: str max_lenght=128
    param was_published: Date of publishing current book
    type was_published: date object

    '''
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=24, primary_key=True)
    author = models.CharField(max_length=128)
    was_buplished = models.DateField()


    def __repr__(self):
        ''' 
        Magic method is redefined to show all information about Alias.
        :return: name, slug  
        '''
        return f'{self.name}, {self.slug}'


    def get_absolute_url(self):
        '''
        This method help us to form correctly url-address and work with admin-panel
        '''
        return reverse('get_by_slug', kwargs={'book_slug': self.slug})

    class Meta:
        '''
        This class represent what name will have object in admin-panel and the sort order
        '''
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name']



# def check_overlap(starts=[], ends=[]):
#     '''
    
#     '''    
#     latest_start = max(*starts)
#     earliest_end = min(*ends)
#     delta = (earliest_end - latest_start).total_seconds() + 1
#     return max(0, delta)


class AliasManager(models.Manager):
    '''
    This class represents an Manager for Alias models\n
    it helps us to validate new instances
    '''
    def create_alias(self, id, name, slug, start, end):
        '''
        This method  help us validate paramethers for Alias obj
        :return: Alias obj
        '''
        aliases = list(Alias.objects.all())
        for alias in aliases:
            if alias.alias == name and alias.target == slug and\
            self.check_overlap([alias.start, start], [alias.end, end]) > 0:
                print('Invalid elements of alias')
                return None
        return self.create(id=id, alias=name, target=slug, start=start, end=end)
        
        
    @staticmethod
    def check_overlap(starts=[], ends=[]):
        '''
        Chek if dates are overlaping
        :return: 0 if not overlaped, otherwise count of microseconds
        '''    
        latest_start = max(*starts)
        earliest_end = min(*ends)
        delta = (earliest_end - latest_start).total_seconds() + 1
        return max(0, delta)
        

class Alias(models.Model):
    '''
    This class represents an Alias.\n
    Attributes:
    -----------
    param alias: Describes name of the alias
    type name: str max_length=128
    param target: pointer to Book slug
    type target: target -> Book.slug
    param start: Describes since when the alias is active
    type start: datetime obj
    param end: Describes till when the alias is active
    type end: datetime obj
    param objects: Helpful pointer to manager class
    type objects: AliasManager obj
    '''    
    alias = models.CharField(max_length=128, db_index=True)
    target = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='get_books')
    start = models.DateTimeField(editable=True)
    end = models.DateTimeField(default=None, editable=True, null=True)
    objects = AliasManager()

    
    def __str__(self):
        '''
        Magic method is redefined to show all information about Alias.
        :return: alias, target, start date, end date
        '''
        return f'{self.alias}, {self.target}, {self.start}, {self.end}'


    def __repr__(self):
        '''
        Magic method is redefined to show some usefull information about Alias.
        :return: alias, target
        '''
        return f'{self.alias}, {self.target}'
    
 
    @staticmethod    
    def get_aliases(target=None, from_=None, to=None):
        '''
        By this method we are getting aliases by target or by timerange
        param target: name of target
        type target: str
        param from_: describes since what date we are searching
        type from: datetime obj
        param to: describes till what date we are searching
        type to: datetime obj
        :return: list with objects that we are searched
        '''
        result = []
        if not target:
            aliases = Alias.objects.all()
            for alias in aliases:
                if from_ <= alias.start <= to and from_ <= alias.end <= to:
                    result.append(alias)
        if not from_ and not to:
            result.append(Alias.objects.filter(target=target))
        else:
            aliases = Alias.objects.filter(target=target)
            for alias in aliases:
                if from_ <= alias.start <= to and from_ <= alias.end <= to:
                    result.append(alias)
        return result        
   
   
    @staticmethod 
    def alias_replace(id_existing_alias, replace_at, new_alias_value):
        '''
        This method replaces an existing alias with a new one at a specific time point
        param id_existing_alias: id of existing alias
        type id_existing_alias: int
        param replace_at: start date time we are need to chenge
        type replace_at: datetime obj
        param new_alias_value: alias value we are need to chenge
        type new_alias_value: str
        :return: Alias obj
        '''
        alias = Alias.objects.get(id=id_existing_alias)
        alias.alias=new_alias_value
        alias.start=replace_at
        alias.end=None
        alias.save()
        return alias
           

    class Meta:
        '''
        This class represent what name will have object in admin-panel and the sort order
        '''
        verbose_name = 'Alias'
        verbose_name_plural = 'Aliases'
        ordering = ['alias']
