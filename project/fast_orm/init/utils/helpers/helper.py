from datetime import date, datetime

# From Date to Str
def format_date_str(date: datetime) -> str:
    """
     Formatar objetos do tipo date para str
    :param date: recebe objeto do tipo date
    :return: String formatada para representar datas com o padrão (`DD/MM/AAAA`)
    """
    return date.strftime('%d/%m/%Y')


# From Str to Date
def format_str_date(date: str) -> date:
    """
     Formatar objetos do tipo str para date
    :param date: recebe objeto do tipo str
    :return: date formatada com o padrão (`DD/MM/AAAA`)
    """
    return datetime.strptime(date, "%d/%m/%Y")


if __name__ == '__main__':

    # Teste format_date_str
    date_now: datetime = datetime.now() # Test Válido datetime.today()
    date_to_str: str = format_date_str(date_now)
    print(type(date_to_str), f"\n{dir(date_to_str)}")
