Garcia, Jedidia Shekainah P.
BSIT 3-1

SwimSafe AI – Drowning Detection Alert System

This system is designed to help prevent drowning incidents by combining AI video analysis with a real-time wireless alarm.
SwimSafe AI is an innovative smart drowning detection and alert system designed to enhance swimming pool safety by combining modern computer vision with IoT technology. Using a live video feed from a camera, the system continuously analyzes swimming activity in real-time through a pre-trained AI model hosted on Roboflow. This AI model detects signs of possible drowning by recognizing unusual or risky behaviors in the water. When a potential drowning event is identified, the system instantly sends an alert signal over Wi-Fi to an ESP32 microcontroller.
The ESP32 then activates a loud, pulsing buzzer and flashes a connected LED light to draw immediate attention to the emergency, ensuring that people nearby can respond quickly. A simple web interface allows users to monitor the live video feed and review a history of past detections to track incidents and improve safety measures. By combining real-time detection with an immediate physical alarm, SwimSafe AI shows how accessible AI and IoT tools can be used together to help prevent accidents and save lives around pools and similar environments.
Key Features:
•	Real-time video-based drowning detection (Roboflow AI model)
•	Local web interface with live feed and incident history of captured drowning images
•	Wireless alarm triggering using ESP32 with WiFi
•	Audible and visual alerts for immediate response
User Interface:
    
How does it work?
1.	A video camera monitors the pool area.
2.	The video feed is analyzed using a YOLOv8 object detection model hosted on Roboflow.
3.	The Flask server handles the video stream and inference requests and logs detection events to a database for history tracking.
4.	When a drowning condition is detected, the Flask server sends a request to the ESP32 via Wi-Fi.
5.	The ESP32 receives the request and triggers an alarm: the buzzer beeps in short bursts while the LED flashes to get attention.
6.	A web interface shows live detection and a history page to review past alerts for monitoring and improvement.
Other applications of the technology used:
•	Computer Vision: Similar detection models can be adapted for fall detection for elderly care, fire or smoke detection in buildings, or intruder detection for home security.
•	IoT Automation: The Wi-Fi-controlled ESP32 can also be used for smart home automation, like controlling lights, doors, or appliances remotely.
•	Safety Systems: The same architecture can be extended for factory worker safety monitoring, machine malfunction alerts, or traffic surveillance.
Circuit Diagram:
 

Components Used:
Component	Function
ESP32 Dev Board	The main microcontroller — connects to Wi-Fi, hosts the web server, and controls outputs based on received HTTP requests.
LED (1 pc)	Visual indicator — flashes to signal an active alarm condition.
Current Limiting Resistor	Protects the LED from excessive current (typically 220–330 Ω).
Passive Buzzer	Provides audible alarm — makes a beeping sound when triggered.
Breadboard	A prototyping board to easily connect components without soldering.
Jumper Wires	Used to make connections between the ESP32, the LED, the resistor, and the buzzer on the breadboard.
USB Cable	Provides power to the ESP32 and uploads code from your computer.

Photo Documentation:
 	 
