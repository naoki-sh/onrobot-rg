# onrobot-rg

Controller for OnRobot RG2 and RG6 grippers.

# Requirements

- Python 3.7.3
  - pymodbus==2.5.3

# Installation

	$ git clone git@github.com:takuya-ki/onrobot-rg.git; cd onrobot-rg
	$ pip install -r requirements.txt

# Usage

1. Connect the cable between Compute Box and Tool Changer.
2. Connect an ethernet cable between Compute Box and your computer.
3. Execute demo script as below  
	`$ python src/demo.py --ip 192.168.1.1 --port 502 --gripper rg2`  
	`$ python src/demo.py --ip 192.168.1.1 --port 502 --gripper rg6`

<img src="img/rg6_2x.gif" height="200">  

# Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
