'''
Created on 16 Sep 2014
@author: rlat
'''

from time import time
import random

from peewee import SqliteDatabase, Model, TextField, IntegerField, CharField, fn

class BaseModel(Model):
    db = SqliteDatabase('catch_phrases.sqlite')

class CatchPhrase(BaseModel):
    id = IntegerField(primary_key=True)
    date = IntegerField()
    user = CharField()
    text = TextField()
    
    class Meta:
        database = BaseModel.db
        
class InvalidUserError(Exception):
    pass

class CatchPhrases(object):
    '''
    Class for storing and retrieving catch phrases.
    '''
    
    __allowed_users = set(['Jenda', 'Radek', 'Profi', 'Pt', 'Renca', 'Danca', 'Dominik', 'Klara_k', 'Milan', 'Terka'])

    def __init__(self):
        '''
        Constructor.
        '''
        BaseModel.db.create_tables([CatchPhrase], safe=True)
        
    @property
    def allowed_users(self):
        return list(self.__allowed_users)
        
    def insert(self, user, phrase):
        """
        Inserts a catch phrase.
        @param str user: A valid user name. See
        :attr:`~CatchPhrase.__allowed_users` attribute.
        @param str phrase: Text of the phrase.
        @raise InvalidUserError: When the user is not valid.
        """
        if user not in self.__allowed_users:
            raise InvalidUserError()
        
        CatchPhrase(date=int(time()), user=user, text=phrase).save()
        
        return True
        
    def get_random(self):
        """
        Fetches random catch phrase.
        @return: :class:`CatchPhrase` instance or None when there are no catch
        phrases.
        """
        try:
            return random.choice([cp for cp in CatchPhrase.select()])
        except IndexError:
            return None
        
    def get_random_user(self, user):
        """
        Fetches random catch phrase from given user.
        @param str user: A valid user name. See
        :attr:`~CatchPhrase.__allowed_users` attribute.
        @return: :class:`CatchPhrase` instance or None when there are no catch
        phrases for given user.
        @raise InvalidUserError: When the user is not valid.
        """
        if user not in self.__allowed_users:
            raise InvalidUserError()
        
        try:
            return random.choice([cp for cp in CatchPhrase.select().where(CatchPhrase.user == user)])
        except IndexError:
            return None
        
    def get_stats(self):
        """
        :return: List of tuples (<user>, <number of catch phrases>). Users with
        zero catch phrases are excluded.
        """
        return [(cp.user, cp.count) for cp in CatchPhrase
            .select(CatchPhrase, fn.Count(CatchPhrase.id).alias('count'))
            .group_by(CatchPhrase.user)
        ]