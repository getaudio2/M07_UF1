import pandas as pd

def casos_totals_mes_pais():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location','date','total_cases'])

    paisos = arxiu['location'].unique()[:10] # Agafem els 10 primer països sense repetir
    mesos = ['2020-03','2020-04','2020-05', '2020-06'] # Seleccionem la data dels 4 mesos

    arxiu['date'] = pd.to_datetime(arxiu['date']) # Convertim date a datetime
    arxiu_filtrat = arxiu[arxiu['location'].isin(paisos) & arxiu['date'].isin(mesos)]  # Filtrem les rows amb els països i mesos anteriors
    grup = arxiu_filtrat.groupby(['location','date'])['total_cases'].sum().reset_index()

    print(grup)
    return grup

'''
def morts_totals_mes_pais_2021():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location', 'date', 'total_deaths'])

    paisos = arxiu['location'].unique()[:10]
    mesos = pd.period_range(start='2021-01', end='2021-04', freq='M')

    arxiu['date'] = pd.to_datetime(arxiu['date'])
    arxiu['mes'] = arxiu['date'].dt.to_period('M')
    filtre = arxiu[arxiu['location'].isin(paisos) & arxiu['mes'].isin(mesos)]
    grup = filtre.groupby(['location', 'mes'])['total_deaths'].sum().reset_index()

    print(grup)
    return grup

def reproduction_rate_mes_pais():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location', 'date', 'reproduction_rate'])

    paisos = arxiu['location'].unique()[:10]
    mesos = pd.period_range(start='2022-02', end='2022-05', freq='M')

    arxiu['date'] = pd.to_datetime(arxiu['date'])
    arxiu['mes'] = arxiu['date'].dt.to_period('M')
    filtre = arxiu[arxiu['location'].isin(paisos) & arxiu['mes'].isin(mesos)]
    grup = filtre.groupby(['location', 'mes'])['reproduction_rate'].sum().reset_index()

    print(grup)
    return grup
'''