import read_csv
import charts
import utils
import pandas as pd


def run():

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  
  countries = df['Country/Territory'].values
  porcentages = df['World Population Percentage'].values
  
  charts.generate_pie_chart(countries, porcentages)


  data = read_csv.read_csv('data.csv')
  country = input('Elegite el pais ==> ')
  country_name = country 
  #use country to send to generate_bar_chart
  #send country_name just the string to generate_bar_chart to create the file name

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    print(labels, values) 
    charts.generate_bar_chart(country_name, labels, values)
  

if __name__ == '__main__':
  run()