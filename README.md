# WeatherOnEarth

# The aim of this project is to automatically post regular twitter posts detailing the weather conditions in 3 random cities every hour.

The program makes use of:
- The Twitter/ X API
- The OpenWeatherMap API
- A Google cloud virtual machine, and its Cron scheduling capabilities
- The requests module
- A large CSV data source

First the program selects 3 random cities from the large data source, and pulls out their latitude, longitude, city name and country name
The program then uses the co-ordinate values along with a GET request to retrive weather data from OpenWeatherMap in JSON format
The data is then parsed and some key data are pulled out and built into a text string
The text string is finally posted to Twitter

This program makes use of Cron scheduling on a Google Cloud VM in order to allow it to run automatically every hour.

The tweets are posted to an account called @WeatherOnEarth on X.com, which is still up and running as of 13/11/2024

## OpenWeatherMap API
OpenWeatherMap are an organisation that provides weather data to consumers, in the case of my program by making requests to its API. A simple GET request containing my api key and the required latitude and longitude sent using the requests module returns a response containing weather data at that location. The program sorts through this response and picks out the required bits of data.

## X API
Programs that use X's API to access and make actions from an X account must be connected to a project/ app created in the X developer portal. Each app has 5 codes that are needed to perform different actions on the associated X account. The API key and API secret are like the username and password of their respective X project. The only time you see these 2 codes in is whilst generating them, after this they remain hidden. The bearer token is used to authenticate each individual request made to the Twitter API for your account, whilst the access token and access secret allow projects on other X accounts to perform actions from your X account. 

In order to make a tweet on the X platform, you need to authenticate yourself as the developer of a project on an X account. The easiest way to do this in Python is with the Tweepy module. To connect to the X API as an authenticated client I simply created an instance of Tweepy's Client class and passed in all of my tokens as parameters. From this point I was then able to use the client to make requests to X's API, using the methods defined in Tweepy's Client class. 

## Google Cloud
![image](https://github.com/user-attachments/assets/2b07c05a-ff03-4081-afe8-3fdb177c9892)
![Screenshot 2024-11-14 121432](https://github.com/user-attachments/assets/814df066-a909-4577-aa7c-3c09e1bca404)
![Screenshot 2024-11-14 121454](https://github.com/user-attachments/assets/e70d3a8e-c297-4047-b1a4-2ccbad90ce7f)

I wanted this program to run 24/7, and post a tweet containing the weather data pulled from OpenWeatherMap every 15 minutes. If the program only ran locally, I would need to leave my laptop on with the program constantly running, which would drain battery and possibly interfere with other programs I wanted to run. The solution I arrived at was to run the program on a server in the cloud, through an e2-micro VM running Debian Bookworm on Google Cloud. I then opened up Secure Shell from the VM instance's page, and after downloading miniconda3 and then uploading my project folder to the VM, I was ready to run the program in the Cloud. The final step was to set up a CRON schedule using the 'crontab -e' command that ran the main.py file on the VM every hour.
