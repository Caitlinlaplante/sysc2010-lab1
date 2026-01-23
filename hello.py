import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Caitlin Laplante 101187525
#Part 5
#Part 5.1
t = np.arange(0, 1, 1/500)
data = 5*np.sin(2*np.pi*10*t) #sine function


plt.plot(t,data)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show() #plot the signal

#Part 5.2
t = np.arange(0, 1, 1/500)
data = 5*np.sin(2*np.pi*10*t) #sine function
noise = 0.25*np.random.randn(len(t)) #noise function
signal = data + noise #signal with noise


plt.plot(t,signal)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show() #plot the signal

#Part 5.3
t = np.arange(0,120*60, 60)
temp = 36.0 + np.random.uniform(-0.5, 0.5, 120) #uniform temperature signal

df = pd.DataFrame({"Time (s)": t, "Temperature (°C)": temp}) #Creating title for csv file

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
df = pd.read_csv("env_temp_humidity_clean.csv") #reads csv file
print("First 5 rows:") #takes the first 5 rows
print(df.head())

print("\nData types:")#shows columns data types
print(df.columns)

print("\nData types:")#shows data types
print(df.dtypes)

#6.4.3
print("\nMissing values per column:") #shows any missing values
print(df.isnull().sum())

print("\nMin / Max values:") #shows the min and max of the values in each columns
print(df[["temperature_C", "humidity_pct"]].agg(["min", "max"]))

#Plots time vs. temperature
plt.figure()
plt.plot(df["timestamp"],df["temperature_C"])
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.show()

#Plots time vs. humidity
plt.figure()
plt.plot(df["timestamp"],df["humidity_pct"])
plt.xlabel("Time")
plt.ylabel("Humidity")
plt.show()

