from tools import PIN_MAP

# Auto-discovery-function of home-assistant (HA)
HA_MODEL  = 'inetbox'
HA_SWV    = 'V02'
HA_STOPIC = 'service/adc/status/'


class adc_voltage:

    HA_ADC_CONFIG = {
        "adc_1_voltage":     ['homeassistant/sensor/adc_1_voltage/config', '{"name": "adc_1_voltage", "model": "' + HA_MODEL + '", "sw_version":"' + HA_SWV + '", "device_class": "None", "unit_of_measurement": "V", "state_topic": "' + HA_STOPIC + 'adc_1_voltage"}'],
        "adc_2_voltage":     ['homeassistant/sensor/adc_2_voltage/config', '{"name": "adc_2_voltage", "model": "' + HA_MODEL + '", "sw_version":"' + HA_SWV + '", "device_class": "None", "unit_of_measurement": "V", "state_topic": "' + HA_STOPIC + 'adc_2_voltage"}'],
        }

    
    # dict for ADC: in, pin, inverted
    ADC_CONFIG = {
        "adc_1": "adc_1_pin",
        "adc_2": "adc_2_pin",
        }
    
    status = {}

    # build up status and initialize GPIO
    def __init__(self, pin):
        self.pin = pin
        v = PIN_MAP.get_adc(pin)


    def loop(self):
        v = PIN_MAP.get_adc(self.pin)
        if v:
            self.v = v
        else:
            self.v = "NA"
        #print("Voltage: " + self.v + "V")
                                

# Status-Dump - with False, it sends all status-values
# with True it sends only a list of changed values - but reset the chance-flag
    def get_all(self):
        #print("ADC Voltage:", self.v)
        return {"voltage": self.v}
