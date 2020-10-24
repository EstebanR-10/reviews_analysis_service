import re
import datetime

months = { 'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06', 'july': '07', 'august': '08',
           'september': '09', 'october': '10', 'november': '11', 'december': '12'}
           
###
# Función encargada de convertir la fecha obtenida por defecto de tripadvisor al formato convencional ISO8601 (yyyy-mm-dd)
# @param String 'unformat_date' fecha en el formato de tripadvisor
# @return String 'ISO_Date' la fecha codificada en formato ISO6801 (yyyy-mm-dd)
# Nota: Mejorar funcionalidad ya que no siempre la fecha podría llegar en el orden { Mes dd, YYYY } Ej. October 8, 2020
def TripDateToISO8601(unformat_date):
    date = re.findall(r'\w+|\d+', unformat_date)
    date = [d.lower() for d in date]
    date_str = ''
    date_str = date[2] + '-' + months[date[0]] + '-' + date[1]
    format_str = '%Y-%m-%d'
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
    #print(date_str)
    return datetime_obj.date()