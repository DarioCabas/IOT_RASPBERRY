[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->

<br />
<p align="center">
  <a href="https://github.com/DarioCabas/ROS_Webpage">
    <img src="https://www.flaticon.es/svg/vstatic/svg/4568/4568780.svg?token=exp=1619830500~hmac=c2eca656132848bd4d10f4846dd2fe31" alt="Logo" width="150" height="80"
  </a>
</p>

# IOT TEMPERATURE, PRESSURE AND HUMIDITY 

_This is a short description about the content of my project. In this project I read three sensors one of temperature, another of humidity and finally one of pressure. We can talk about this sensors in the next lines. So this values of variables measured are send to the cloud, and we can see this data in the cloud of thingspeak that provide MATLAB for IOT Analytics, you can see all the information in the server and read that information if we need it. In another hand we can write this values also in a CSV file that we can save in a SDcard_

## Getting Started🚀


_These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See_ **_Deployment_** _for notes on how to deploy the project ._


## Prerequisites:clipboard:

_The hardware that you need is:_ 

```
  Raspberry Pi
```
<p align="center">
    <img src="https://www.redeszone.net/app/uploads-redeszone.net/2019/05/Raspberry-Pi-Zero-con-GPIO.jpg" alt="Logo">

</p>

```
  Barometric Pressure Sensor BMP085
```
<p align="center">
    <img width="400" height="300" src="https://cdn-shop.adafruit.com/1200x900/391-00.jpg" alt="Logo">

</p>

```
Temperature and humidity sensor - DHT22
```
<p align="center">
    <img width="300" height="200" src="https://cdn-shop.adafruit.com/1200x900/385-00.jpg" alt="Logo">

</p>

_The software that you need is:_ 

```
  -Raspbian
```
```
  -Libraries for use the BMP085 and DHT22
```
```
  -ThingSpeak
```

### Installing🔧

#### Clone

- _Clone this repo to your local machine using_ `https://github.com/DarioCabas/IOT_RASPBERRY`

- _If you need more information about how install raspbian in the raspberry, follow the next link:_
<p align="center">
    <a href="https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started/1">Raspbian</a>
</p>

#### Enabled I2C 

- _In the raspberry you need enable the I2C communication to use the BMP085 sensor that use this protocol, you can do the next steps:_
- _In the command window you put the next command line:_

```
  sudo raspi-config
```
 _You can see the next window:_
 
 <p align="center">
    <img width="600" height="300" src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2014/08/rc_cmd_main_interfacing.png" alt="Logo">
</p>

_Select the line in red and you can see the I2C option that you need enabled:_

 <p align="center">
    <img width="600" height="300" src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2014/11/rc_cmd_interfacing_i2c.png" alt="Logo">
</p>

_Enter in Yes_
 <p align="center">
    <img width="400" height="300" src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2014/11/rc_cmd_i2c_1.png" alt="Logo">
</p>

_Enter in OK_
 <p align="center">
    <img width="400" height="300" src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2014/11/rc_cmd_i2c_2.png" alt="Logo">
</p>

_And Finally you reboot the system:_
 <p align="center">
    <img width="400" height=300" src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2014/08/rc_cmd_reboot.png" alt="Logo">
</p>

## Running the tests ⚙️

**Sensors connected to the raspberry**
 <p align="center">
    <img width="650" height="400" src="img/raspberry.jpg" alt="Logo">
</p>


**Running prom.py**
 <p align="center">
    <img width="800" height="500" src="img/data.jpeg" alt="Logo">
</p>

**CSV file with the data**
 <p align="center">
    <img width="400" height="400" src="img/Captura.PNG" alt="Logo">
</p>


**ThingSpeak**
 <p align="center">
    <img width="800" height="500" src="img/thing.jpeg" alt="Logo">
</p>


## Deployment📦

_For the crontan that we use to run the envio.py file, you can access to this with the following line:_


```
  crontab -e
```

_And in this project I use in the linux environment the next line for run the envio.py in the crontab_

```
  */5 * * * * cd Desktop && /usr/bin/python envio.py
```


## Built With🛠️

* [Python](https://www.python.org/) - Language
* [Raspberry Pi](https://www.raspberrypi.org/) - Credit-card sized computer
* [ThingSpeak](https://thingspeak.com/) - Data collection in the cloud


## Authors✒️

* **Dario Cabascango** - *Initial work* - [IOT_RASPBERRY](https://github.com/DarioCabas)


## License📄

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**


## Contact:e-mail: 

#### Feel free to contact me!

_Dario Cabascango_  - _hz-hertzio@hotmail.com_ 

_Project Link:_ _[https://github.com/DarioCabas/IOT_RASPBERRY](https://github.com/DarioCabas/IOT_RASPBERRY)_


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DarioCabas/IOT_RASPBERRY.svg?style=flat-square
[contributors-url]: https://github.com/DarioCabas/IOT_RASPBERRY/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DarioCabas/IOT_RASPBERRY.svg?style=flat-square
[forks-url]: https://github.com/DarioCabas/IOT_RASPBERRY/network/members
[stars-shield]: https://img.shields.io/github/stars/DarioCabas/IOT_RASPBERRY.svg?style=flat-square
[stars-url]: https://github.com/DarioCabas/IOT_RASPBERRY/stargazers
[issues-shield]: https://img.shields.io/github/issues/DarioCabas/IOT_RASPBERRY.svg?style=flat-square
[issues-url]: https://github.com/DarioCabas/IOT_RASPBERRY/issues
[license-shield]: https://img.shields.io/github/license/DarioCabas/IOT_RASPBERRY.svg?style=flat-square
[license-url]: https://github.com/DarioCabas/IOT_RASPBERRY/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dario-cabascango-9724431a3


