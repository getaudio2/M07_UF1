import pandas as pd

def casos_totals_mes_pais():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location','date','total_cases'])

    paisos = arxiu['location'].unique()[:10] # Agafem els 10 primer països sense repetir
    #mesos = ['2020-03','2020-04','2020-05', '2020-06'] # Seleccionem la data dels 4 mesos
    mesos = pd.date_range('2020-03', periods=4, freq='M') # Seleccionem els 4 mesos

    arxiu['date'] = pd.to_datetime(arxiu['date']) # Convertim date a datetime
    arxiu['mes'] = arxiu['date'].dt.to_period(freq = 'M') # Creem una nova columna amb els periodes de temps en mesos
    arxiu_filtrat = arxiu[arxiu['location'].isin(paisos) & arxiu['date'].isin(mesos)]  # Filtrem les rows amb els països i mesos anteriors
    grup = arxiu_filtrat.groupby(['location', 'mes'])['total_cases'].sum().reset_index() # Agrupem per països i mesos i afegim la suma de casos per mes

    location_list = grup['location'].values.tolist()
    total_cases_list = grup['total_cases'].values.tolist()
    mesos_list = grup['mes'].values.tolist()
    print(grup['mes'])

    df = pd.DataFrame(total_cases_list, location_list, columns=['total cases'])

    print(df)
    return df


def morts_totals_mes_pais_2021():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location', 'date', 'total_deaths'])

    paisos = arxiu['location'].unique()[:10]
    mesos = ['2021-01','2021-02','2021-03', '2021-04']

    arxiu['date'] = pd.to_datetime(arxiu['date'])
    arxiu_filtrat = arxiu[arxiu['location'].isin(paisos) & arxiu['date'].isin(mesos)]
    grup = arxiu_filtrat.groupby(['location', 'date'])['total_deaths'].sum().reset_index()

    print(grup)
    return grup

def reproduction_rate_mes_pais():
    arxiu = pd.read_csv("df_covid19_countries.csv", usecols=['location', 'date', 'reproduction_rate'])

    paisos = arxiu['location'].unique()[:10]
    mesos = ['2022-02','2022-03','2022-04', '2022-05']

    arxiu['date'] = pd.to_datetime(arxiu['date'])
    arxiu_filtrat = arxiu[arxiu['location'].isin(paisos) & arxiu['date'].isin(mesos)]
    grup = arxiu_filtrat.groupby(['location', 'date'])['reproduction_rate'].sum().reset_index()

    print(grup)
    return grup
