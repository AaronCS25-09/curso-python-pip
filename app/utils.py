def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def population_by_country(data, country):
    result = list(filter(lambda i: i['Country/Territory'] == country, data))
    return result

import csv

def all_population_by_country(path, country):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader)
        """ for row in reader:
            if row[2] == country:
                data = [int(i) for i in row[5:13]]
                return data """
        """ data = filter(lambda x: x[2] == country, reader)
        return [i for i in data] """
        """ data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        data = list(filter(lambda x: x['Country/Territory'] == country, data))
        return [data[0]['2022 Population'], data[0]['2020 Population'], data[0]['2015 Population'],
                data[0]['2010 Population'], data[0]['2000 Population'], data[0]['1990 Population'],
                data[0]['1980 Population'], data[0]['1970 Population']] """

def all_rows_by_column(path, column):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader)
        data = []
        dict_v2 = {}
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            dict_v2 = {'Country/Territory': country_dict['Country/Territory'], column: country_dict[column]}
            data.append(dict_v2)
        return data
