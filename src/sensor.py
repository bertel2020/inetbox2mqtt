from tools import PIN_MAP

# Auto-discovery-function of home-assistant (HA)
HA_MODEL  = 'inetbox'
HA_SWV    = 'V02'
HA_STOPIC = 'service/magnetic_sensor/'


class magnetic_sensor:

    HA_MS_CONFIG = {
        "magnetic_sensor_1":     ['homeassistant/sensor/magnetic_sensor_1/config', '{"name": "magnetic_sensor_1", "model": "' + HA_MODEL + '", "sw_version":"' + HA_SWV + '", "device_class": "None", "unit_of_measurement": "None", "state_topic": "' + HA_STOPIC + 'magnetic_sensor_1"}'],
        "magnetic_sensor_2":     ['homeassistant/sensor/magnetic_sensor_2/config', '{"name": "magnetic_sensor_2", "model": "' + HA_MODEL + '", "sw_version":"' + HA_SWV + '", "device_class": "None", "unit_of_measurement": "None", "state_topic": "' + HA_STOPIC + 'magnetic_sensor_2"}'],
        }
    
    # dict for MS: in, pin, inverted
    MS_CONFIG = {
        "magnetic_sensor_1": "magnetic_sensor_1_pin",
        "magnetic_sensor_2": "magnetic_sensor_2_pin",
        }
    
    status = {}

    # build up status and initialize GPIO
    def __init__(self, pin):
        self.pin = pin
        v = PIN_MAP.get_status(self.pin)


    def loop(self):
        v = PIN_MAP.get_status(self.pin)
        if v:
            self.v = "Open"
        else:
            self.v = "Closed"
                        


# Status-Dump - with False, it sends all status-values
# with True it sends only a list of changed values - but reset the chance-flag
    def get_all(self):
        #print("MS1 Status:", self.v)
        return {"status": self.v}

