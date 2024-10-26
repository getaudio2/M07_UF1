import matplotlib.pyplot as plt
import exerciciA

total_cases = exerciciA.casos_totals_mes_pais()
total_deaths = exerciciA.morts_totals_mes_pais_2021()
reproduction_rate = exerciciA.reproduction_rate_mes_pais()

window = plt.figure()
graf1 = window.add_subplot(2,2,1)
graf2 = window.add_subplot(2,2,2)
graf3 = window.add_subplot(2,2,3)

graf1.plot(total_cases)
graf1.set_title('Casos totals')
graf1.legend(total_cases.columns, title="països")
graf2.plot(total_deaths)
graf2.set_title('Morts totals')
graf2.legend(total_deaths.columns, title="països")
graf3.plot(reproduction_rate)
graf3.set_title('Reproduction rate')
graf3.legend(reproduction_rate.columns, title="països", bbox_to_anchor=(1.05, 1.0), loc='upper left')

plt.show()