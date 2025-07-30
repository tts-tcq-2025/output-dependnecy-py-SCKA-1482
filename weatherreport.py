def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def sensorStubHighPrecipLowWind():
    return {
        'temperatureInC': 50,
        'precipitation': 70,  # > 60
        'humidity': 40,
        'windSpeedKMPH': 40   # < 50
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if readings['temperatureInC'] > 25:
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather

def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert "rain" in weather, "Expected 'rain' in weather report"

def testHighPrecipitationLowWind():
    weather = report(sensorStubHighPrecipLowWind)
    print(weather)
    assert "rain" in weather, "Expected 'rain' in weather report when precipitation is high"

if __name__ == '__main__':
    testRainy()
    testHighPrecipitationLowWind()  
    print("All is well (maybe!)")

