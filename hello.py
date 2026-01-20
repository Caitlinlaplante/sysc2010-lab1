import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Part 5
#Part 5.1
t = np.arange(0, 1, 1/500)
data = 5*np.sin(2*np.pi*10*t)


plt.plot(t,data)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()

#Part 5.2
t = np.arange(0, 1, 1/500)
data = 5*np.sin(2*np.pi*10*t)
noise = 0.25*np.random.randn(len(t))
signal = data + noise


plt.plot(t,signal)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()

#Part 5.3
t = np.arange(0,120*60, 60)
temp = 36.0 + np.random.uniform(-0.5, 0.5, 120)

dataf = pd.DataFrame({"Time (s)": t, "Temperature (°C)": temp})

dataf.to_csv("env_temp_humidity_clean.csv")
dataf_read = pd.read_csv("env_temp_humidity_clean.csv")
subset = dataf_read.iloc[41:81]


plt.plot(subset["Time (s)"], subset["Temperature (°C)"])
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.show()

#Part 6
t = np.arange(0,120*60, 60)
temp = 36.0 + np.random.uniform(-0.5, 0.5, 120)

dataf = pd.DataFrame({"Time (s)": t, "Temperature (°C)": temp})

dataf.to_csv("env_temp_humidity_clean.csv")
dataf_read = pd.read_csv("env_temp_humidity_clean.csv")


plt.plot(subset["Time (s)"], subset["Temperature (°C)"])
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.show()


