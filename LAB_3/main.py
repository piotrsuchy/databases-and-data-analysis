import numpy as np
import pickle

from sqlalchemy import create_engine
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = create_engine("postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb")

def film_in_category(category_id:int)->pd.DataFrame:
    if isinstance(category_id, int):
        condition = 'f_c.category_id = {}'.format(category_id)
        df = pd.read_sql('\
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
    
    
def number_films_in_category(category_id:int)->pd.DataFrame:
    if isinstance(category_id, int):
        condition = 'f_c.category_id = {}'.format(category_id)
        df = pd.read_sql('\
            SELECT \
                name, \
                COUNT(f_c.film_id) \
            FROM \
                film f \
                JOIN film_category f_c ON f.film_id = f_c.film_id \
                JOIN category c ON f_c.category_id = c.category_id \
            WHERE \
                {} \
            GROUP BY name'.format(condition), con=connection)
        df.columns = ['category', 'count']
        return df
    else:
        return None


def number_film_by_length(min_length: Union[int,float] = 0, max_length: Union[int,float] = 1e6 ):
    if isinstance(min_length, (int, float)) and isinstance(max_length, (int, float)) and min_length <= max_length:
        df = pd.read_sql('\
            SELECT \
                length, \
                COUNT(film_id) \
            FROM \
                film f \
            WHERE \
                length BETWEEN {} AND {} \
            GROUP BY length'.format(min_length, max_length), con=connection)
        df.columns = ['length', 'count']
        return df
    else:
        return None


def client_from_city(city:str)->pd.DataFrame:
    if isinstance(city, str):
        condition = "ci.city = '{}'".format(city)
        df = pd.read_sql('\
            SELECT \
                city, \
                first_name, \
                last_name \
            FROM \
                customer c \
                JOIN address a ON c.address_id = a.address_id \
                JOIN city ci ON a.city_id = ci.city_id \
            WHERE \
                {} \
            ORDER BY last_name ASC, first_name ASC'.format(condition), con=connection)
        df.columns = ['city', 'first_name', 'last_name']
        return df
    else:
        return None


def avg_amount_by_length(length:Union[int,float])->pd.DataFrame:
    if isinstance(length, (int, float)):
        condition = "f.length = '{}'".format(length)
        df = pd.read_sql('\
            SELECT \
                length, \
                AVG(amount) \
            FROM \
                film f \
                JOIN inventory i ON f.film_id = i.film_id \
                JOIN rental r ON i.inventory_id = r.inventory_id \
                JOIN payment p ON r.rental_id = p.rental_id \
            WHERE \
                {} \
            GROUP BY length'.format(condition), con=connection)
        df.columns = ['length', 'avg']
        return df
    else:
        return None
    

def client_by_sum_length(sum_min:Union[int,float])->pd.DataFrame:
    if isinstance(sum_min, (int, float)):
        df = pd.read_sql("\
                SELECT \
                    c.first_name, \
                    c.last_name, \
                    SUM(f.length) AS suma_dlug \
                FROM \
                    customer c \
                    JOIN rental r ON c.customer_id = r.customer_id \
                    JOIN inventory i ON r.inventory_id = i.inventory_id \
                    JOIN film f ON i.film_id = f.film_id \
                GROUP BY \
                    first_name, last_name \
                HAVING \
                    SUM(f.length) > {} \
                ORDER BY \
                    suma_dlug ASC, last_name ASC, first_name ASC".format(sum_min), con=connection)
        df.columns = ['first_name', 'last_name', 'sum']
        return df
    else:
        return None


def category_statistic_length(name:str)->pd.DataFrame:
    if isinstance(name, str):
        condition = "c.name = '{}'".format(name)
        df = pd.read_sql('\
                SELECT \
                    c.name, \
                    AVG(f.length), \
                    SUM(f.length), \
                    MIN(f.length), \
                    MAX(f.length) \
                FROM \
                    film f \
                    JOIN film_category f_c ON f.film_id = f_c.film_id \
                    JOIN category c ON f_c.category_id = c.category_id \
                GROUP BY \
                    c.name \
                HAVING \
                    {}'.format(condition), con=connection)
        df.columns = ['category', 'avg', 'sum', 'min', 'max']
        return df
    else:
        return None