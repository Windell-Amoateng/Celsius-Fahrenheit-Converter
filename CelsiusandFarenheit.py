# Starting Celsius Temp
start_temp = int(input("What is the starting Celsius temperature? "))

# Ending Celsius Temp
end_temp = int(input("What is the ending Celsius temperature? "))

# Global variable or constant for Farenheit
fahrenheit = 0.0

# Creation of table to hold temps
print("Celsius\t\tFahrenheit")
print("-----------------------")

# Display Celsius and Fahrenheit Temps
for celsiusDegree in range(start_temp, end_temp+1):
    fahrenheit = ((9 * celsiusDegree) / 5) + 32
    print(celsiusDegree, '\t\t', fahrenheit)