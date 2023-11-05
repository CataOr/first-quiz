################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city):
    temperatures = {
        "Quito": 22,
        "Sao Paulo": 17,
        "San Francisco": 16
    }
    return temperatures.get(city, "unknown")

    def get_city_weather(city):
        sky_conditions = {
            "Sao Paulo": "cloudy",
            "New York": "rainy"
        }

        temperature =get_city_temperature(city)
        sky_condition = sky_conditions.get(city, "unknown")

        return f"{temperature} degrees and {sky_condition}"    