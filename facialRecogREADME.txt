DESCRIPTION:
	In this project, I use Arduino and python in vs code along with Google's teachable machine to detect whether or not my face is on captured 	webcam video. The program sends Arduino either "B" if the face in the webcam is recognized by the program, or "R" if the face is unrecognized by 	the program. Once Arduino receives one of these 2 signals, it sends the input through an if statement. If the input is "R", then the program 	will turn the blue LED buzzer off if it is on and will trigger the red LED buzzer to turn on. Likewise, if the input is "B", then the program 	will turn the red LED buzzer off if it is on and will trigger the blue LED buzzer to turn on. This project acts as a very simple facial 	recognition security system and could be improved upon to accept multiple different faces as recognized.

INSTRUCTIONS:
	This project starts by running the Arduino program. After running the program, check the Serial Monitor and ensure the output "Arduino is ready, 	waiting for input." is there. After this, close the serial monitor and switch over to vs code.

	In vs code, run the program and wait a few moments for Arduino to prepare and for your webcam to be automatically opened. The blue buzzer on the 	Arduino board blinks twice right before the webcam opens.

	Once the webcam turns on, the vs code will immediately and repeatedly output either "Recognized!" or "Unrecognized!" along with the 	corresponding class in the teachable machine model and the confidence level at which the program estimates the webcam capture to be. It also 	sends Arduino either "R" or "B".

	Once Arduino receive "R" or "B" from vs code, it will trigger the corresponding LED buzzer and deactivate the other one.

	Finally, press 'Q' to end the program.