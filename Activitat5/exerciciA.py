import pandas as pd

def casos_totals_mes_pais():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location','date','total_cases'])

    paisos = arxiu['location'].unique()[:10] # Agafem els 10 primer països sense repetir
    mesos = pd.date_range('2020-05', periods=4, freq='M') # Seleccionem els 4 mesos

    arxiu['date'] = pd.to_datetime(arxiu['date']) # Convertim date a datetime
    arxiu['mes'] = arxiu['date'].dt.to_period(freq = 'M') # Creem una nova columna amb els periodes de temps en mesos
    arxiu_filtrat = arxiu[arxiu['location'].isin(paisos) & arxiu['date'].isin(mesos)]  # Filtrem les rows amb els països i mesos anteriors
    grup = arxiu_filtrat.groupby(['location', 'mes'])['total_cases'].sum().reset_index() # Agrupem per països i mesos i afegim la suma de casos per mes

    grup = grup.pivot(index='mes', columns='location', values='total_cases') # Creem una columna per pais amb 4 rows pels casos segons el mes
    grup.index = grup.index.to_series().astype(str)

    print(grup)
    return grup


def morts_totals_mes_pais_2021():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location', 'date', 'total_deaths'])

    paisos = arxiu['location'].unique()[:10]
    mesos = pd.date_range('2021-05', periods=4, freq='M')

    arxiu['date'] = pd.to_datetime(arxiu['date'])
    arxiu['mes'] = arxiu['date'].dt.to_period(freq='M')
    arxiu_filtrat = arxiu[arxiu['location'].isin(paisos) & arxiu['date'].isin(mesos)]
    grup = arxiu_filtrat.groupby(['location', 'mes'])['total_deaths'].sum().reset_index()

    grup = grup.pivot(index='mes', columns='location', values='total_deaths')
    grup.index = grup.index.to_series().astype(str)

    print(grup)
    return grup

def reproduction_rate_mes_pais():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location', 'date', 'reproduction_rate'])

    paisos = arxiu['location'].unique()[:10]
    mesos = pd.date_range('2022-02', periods=4, freq='M')

    arxiu['date'] = pd.to_datetime(arxiu['date'])
    arxiu['mes'] = arxiu['date'].dt.to_period(freq='M')
    arxiu_filtrat = arxiu[arxiu['location'].isin(paisos) & arxiu['date'].isin(mesos)]
    grup = arxiu_filtrat.groupby(['location', 'mes'])['reproduction_rate'].sum().reset_index()

    grup = grup.pivot(index='mes', columns='location', values='reproduction_rate')
    grup.index = grup.index.to_series().astype(str)

    print(grup)
    return grup
