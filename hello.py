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

df = pd.DataFrame({"Time (s)": t, "Temperature (°C)": temp})

# Save to CSV
df.to_csv("sensor_readings.csv", index = False)

# Read the CSV file
df_read = pd.read_csv("sensor_readings.csv")

# Extract values between indices 41 and 80
subset = df_read.iloc[41:81]

# Plot extracted data
plt.figure()
plt.plot(subset["Time (s)"], subset["Temperature (°C)"])
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.show()

#Part 6
#6.4.2
df = pd.read_csv("env_temp_humidity_clean.csv")
print("First 5 rows:")
print(df.head())

print("\nData types:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

#6.4.3
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nMin / Max values:")
print(df[["temperature_C", "humidity_pct"]].agg(["min", "max"]))

plt.figure()
plt.plot(df["timestamp"],df["temperature_C"])
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.show()

plt.figure()
plt.plot(df["timestamp"],df["humidity_pct"])
plt.xlabel("Time")
plt.ylabel("Humidity")
plt.show()

