# Imports
import matplotlib.pyplot as plt

# Describing data
plt.plot([1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2019],
         [2136391, 2372594, 2626645, 2818387, 3082633, 3146619, 3268236, 3398172, 3674936, 
          3858999, 4135355, 4370062, 4614532, 4792409])

# Defining Graph
plt.ylabel('Population')
plt.xlabel('Year')
plt.title("New Zealand's Population Growth")
plt.show()

# Console Messages
print('Plot Compilied')
