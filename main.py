import twitter_API
import cities
import owm_data
import schedule
import time

def main():
    city1, city2, city3 = cities.getThreeCities()

    w1= owm_data.getCurrentWeatherData(city1[1], city1[2])
    w2= owm_data.getCurrentWeatherData(city2[1], city2[2])
    w3= owm_data.getCurrentWeatherData(city3[1], city3[2])

    line1 = f"{w1[0]} in {city1[0]}, {city1[3]}, with a temperature of {w1[1]}°C"
    line2 = f"{w2[0]} in {city2[0]}, {city2[3]}, with a temperature of {w2[1]}°C"
    line3 = f"{w3[0]} in {city3[0]}, {city3[3]}, with a temperature of {w3[1]}°C"

    post_string = line1+"\n\n"+line2+"\n\n"+line3

    twitter_API.Post(post_string)

# schedule.every(10).minutes.do(main)

# while __name__ == '__main__':
#     schedule.run_pending()
#     time.sleep(300)

main()