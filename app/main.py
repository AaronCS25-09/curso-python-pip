import utils
import charts
import read_csv

def run():
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)

    country = input('Type the country =>')
    #print(country)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        #print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_char(labels, values, country['Country/Territory'])


if __name__ == '__main__':
    run()

