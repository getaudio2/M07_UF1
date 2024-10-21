import matplotlib.pyplot as plt
import exerciciA

total_cases = exerciciA.casos_totals_mes_pais()
#total_deaths = exerciciA.morts_totals_mes_pais_2021()
#reproduction_rate = exerciciA.reproduction_rate_mes_pais()

total_cases.plot()
plt.xlabel('paisos-mesos')
plt.ylabel('total_cases')
plt.show()