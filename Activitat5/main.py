import matplotlib.pyplot as plt
import exerciciA

total_cases = exerciciA.casos_totals_mes_pais()
#total_deaths = exerciciA.morts_totals_mes_pais_2021()
#reproduction_rate = exerciciA.reproduction_rate_mes_pais()

total_cases.plot()
plt.xlabel('mesos')
plt.ylabel('total cases')
plt.legend(title="països")
plt.show()