import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def count_Ruth_and_Robert():

    names_by_year = {}

    for year in range(1900, 2000):
        names_by_year[year] = pd.read_csv('yob{}.txt'.format(year), names = ['name', 'gender', 'count'])

    names_all = pd.concat(names_by_year,names=['year', 'pos']) 

    name_dynamics_cols = (names_all.groupby([names_all.index.get_level_values(0), 'name']).sum().query("name == ['Ruth', 'Robert']").unstack('name')).plot()


def number_of_names_by_years():

    names_by_year = {}

    for year in range(1900, 2000, 5):
        names_by_year[year] = pd.read_csv('yob{}.txt'.format(year), names = ['name', 'gender', 'count'])
    
    names_all = pd.concat(names_by_year,names=['year', 'count'])

    names_all.groupby('year').count()['name'].plot.bar()


def pie_top10():
    
    years = 1950

    names_all = pd.read_csv('yob{}.txt'.format(year), names = ['name', 'gender', 'count'])

    names_group = names_all.groupby('name').sum()

    names_start_r = names_group[names_group.index.str.startswith('R')]
    
    names_start_r.nlargest(10, 'count', keep='first').plot.pie(y = 'count')

    
def consonants_in_names():
    
    names_all = None

    for year in range(1900, 2000):
        names = pd.read_csv('yob{}.txt'.format(year), names = ['name', 'gender', 'count'])
        if names_all is None:
            names_all = names
        else:
            names_all = pd.concat([names, names_all])            
            
    names_sum = names_all.groupby(['name', 'gender'], as_index = False).sum()

    names_sum.name = names_sum.name.apply(consonants_in_word)
    
    names_sum.plot.scatter(x='name', y='count')

    
def consonants_in_word(row):

    consonants = 0
    for char in row.upper():
        if char in ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']:
            consonants += 1
        
    return consonants
    
    
count_Ruth_and_Robert()

pie_top10()

consonants_in_names()

number_of_names_by_years()
