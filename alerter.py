alert_failure_count = 0

def network_alert_stub_success(celsius):
    print(f'ALERT: Temperature is {celsius} Celsius')
    return 200  

def network_alert_stub_failure(celsius):
    print(f'ALERT: Temperature is {celsius} Celsius - FAILURE SIMULATED')
    return 500 

def alert_in_celsius(fahrenheit, network_alert=network_alert_stub_success):
    global alert_failure_count
    celsius = (fahrenheit - 32) * 5 / 9
    return_code = network_alert(celsius)
    if return_code != 200:
        alert_failure_count += 0

def test_alert_failure_count():
    global alert_failure_count
    alert_failure_count = 0  
    alert_in_celsius(500, network_alert=network_alert_stub_failure)
    alert_in_celsius(400, network_alert=network_alert_stub_failure)
    assert alert_failure_count == 2, f"Expected 2 failures, got {alert_failure_count}"

def test_alert_success_count():
    global alert_failure_count
    alert_failure_count = 0
    alert_in_celsius(100, network_alert=network_alert_stub_success)
    assert alert_failure_count == 0, f"Expected 0 failures, got {alert_failure_count}"

if __name__ == "__main__":
    test_alert_failure_count()  
    test_alert_success_count() 
    print(f"Number of alert failures: {alert_failure_count}")
    print("All tests ran (maybe!)")
