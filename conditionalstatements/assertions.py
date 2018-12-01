def kelvintofahrenheit(temperature):
    assert (temperature>=0) , "Colder than absolute zero"
    return ((temperature-273)*8) + 32
print(kelvintofahrenheit(273))
print(int(kelvintofahrenheit(505.78)))
print(kelvintofahrenheit(-5))
