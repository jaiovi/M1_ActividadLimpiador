from money_model import MoneyModel

import matplotlib
import matplotlib.pyplot as plt


def basic_example_space():
    # empty_model = MoneyModel(10)
    # empty_model.step()
    print(matplotlib.get_backend())

    model = MoneyModel(50, 10, 10)
    for i in range(20):
        model.step()

    agent_wealth = [a.wealth for a in model.schedule.agents]
    print(agent_wealth)

    plt.hist(agent_wealth)
    plt.show()

    agent_wealth = model.datacollector.get_agent_vars_dataframe()
    agent_wealth.head()


basic_example_space()