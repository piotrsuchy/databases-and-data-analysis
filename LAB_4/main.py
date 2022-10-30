import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    if isinstance(category, int):
        condition = 'f_c.category_id = {}'.format(category)
        df = pd.read_sql_query('\
            SELECT \
                title, \
                l.name, \
                c.name \
            FROM \
                film f \
                JOIN language l ON f.language_id = l.language_id \
                JOIN film_category f_c ON f.film_id = f_c.film_id \
                JOIN category c ON f_c.category_id = c.category_id \
            WHERE \
                {} \
            ORDER BY \
                title, l.name ASC'.format(condition), con=connection)
        df.columns = ['title', 'languge', 'category']
        return df
    elif isinstance(category, str):
        condition = "c.name = '{}'".format(category)
        df = pd.read_sql_query('\
            SELECT \
                title, \
                l.name, \
                c.name \
            FROM \
                film f \
                JOIN language l ON f.language_id = l.language_id \
                JOIN film_category f_c ON f.film_id = f_c.film_id \
                JOIN category c ON f_c.category_id = c.category_id \
            WHERE \
                {} \
            ORDER BY \
                title ASC'.format(condition), con=connection)
        df.columns = ['title', 'languge', 'category']
        return df
    else:
        return None
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    if isinstance(category, int):
        condition = 'f_c.category_id = {}'.format(category)
        df = pd.read_sql_query('\
            SELECT \
                title, \
                l.name, \
                c.name \
            FROM \
                film f \
                JOIN language l ON f.language_id = l.language_id \
                JOIN film_category f_c ON f.film_id = f_c.film_id \
                JOIN category c ON f_c.category_id = c.category_id \
            WHERE \
                {} \
            ORDER BY \
                title, l.name ASC'.format(condition), con=connection)
        df.columns = ['title', 'languge', 'category']
        return df
    elif isinstance(category, str):
        condition = "c.name iLIKE '{}'".format(category)
        df = pd.read_sql_query('\
            SELECT \
                title, \
                l.name, \
                c.name \
            FROM \
                film f \
                JOIN language l ON f.language_id = l.language_id \
                JOIN film_category f_c ON f.film_id = f_c.film_id \
                JOIN category c ON f_c.category_id = c.category_id \
            WHERE \
                {} \
            ORDER BY \
                title, l.name ASC'.format(condition), con=connection)
        df.columns = ['title', 'languge', 'category']
        return df
    return None
    
def film_cast(title:str)->pd.DataFrame:
    if isinstance(title, str):
        condition = "f.title = '{}'".format(title)
        df = pd.read_sql_query('\
            SELECT \
                a.first_name, \
                a.last_name \
            FROM \
                film f \
                JOIN film_actor f_a ON f.film_id = f_a.film_id \
                JOIN actor a ON f_a.actor_id = a.actor_id \
            WHERE \
                {} \
            ORDER BY \
                a.last_name, a.first_name ASC'.format(condition), con=connection)
        df.columns = ['first_name', 'last_name']
        return df
    return None
    

def film_title_case_insensitive(words:list):
    if isinstance(words, list):
        words_str = '|'.join(words)
        df = pd.read_sql_query("select title \
                                    from film \
                                    where title ~* '(?:^| )({})".format(words_str) + "{1,}(?:$| )' \
                                    order by title", con=connection)
        return df
    return None