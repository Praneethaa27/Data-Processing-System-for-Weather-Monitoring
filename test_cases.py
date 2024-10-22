# test_cases.py

import unittest
from data_processing import kelvin_to_celsius, calculate_daily_aggregates

class TestWeatherSystem(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(273.15), 0)  # Test freezing point
        self.assertEqual(kelvin_to_celsius(298.15), 25) # Test room temperature

    def test_daily_aggregates(self):
        test_data = [
            {'temp_celsius': 25, 'weather_condition': 'Clear'},
            {'temp_celsius': 30, 'weather_condition': 'Clouds'},
            {'temp_celsius': 27, 'weather_condition': 'Clear'}
        ]
        result = calculate_daily_aggregates(test_data)
        self.assertEqual(result['average_temp'], 27.33)
        self.assertEqual(result['max_temp'], 30)
        self.assertEqual(result['min_temp'], 25)
        self.assertEqual(result['dominant_condition'], 'Clear')

if __name__ == '__main__':
    unittest.main()
