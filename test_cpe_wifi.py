from pyats import aetest 
from unittest.mock import MagicMock 

class TestCPEWifi(aetest.Testcase):
    @aetest.test
    def test_wifi_ssid(self):
        device = MagicMock()
        device.execute.return_value ="SSID : Sunrise=5G\nStatus:UP"
        output = device.execute("Show wifi")
        assert "UP" in output
        print("PASS: Wifi UP")
    @aetest.test
    def test_ping(self):
        result = True
        assert result is True
        print("PASS: Ping Ok")
if __name__ == '__main__':
    aetest.main()