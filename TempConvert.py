#TempConvert.py
#Name: Gustavo Vargas
#Date: 02/12/2026
#Assignment: Temp Convert


def main():
  #Prompt the user for a Fahrenheit temperature
  Farenheit = input("What is the temperature Farenheit?: ")
  Farenheit = int(Farenheit)
  #Convert that temperature to celsius, rounding to 1 decimal percision
  Celsius = (Farenheit - 32) * (5/9)
  Celsius = round(Celsius, 1)
  #Output converted temperature.

  print(Farenheit, "degrees Farenheit is ", Celsius , "degrees celsius.")
if __name__ == '__main__':
  main()
