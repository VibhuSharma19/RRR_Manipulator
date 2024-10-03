/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

Servo servo;

void servo_cb(const std_msgs::String& msg){
  String pos = msg.data;
  if (pos=="wrong"){
      servo.write(90); //set servo angle, should be from 0-180  
      digitalWrite(13, LOW);//toggle led
  }  
  else if (pos=="correct"){
      servo.write(30);
      digitalWrite(13, LOW);
  }
  else{ 
      servo.write(60);
      digitalWrite(13, HIGH);
  }
  
}


ros::Subscriber<std_msgs::String> sub("Inspection_result", servo_cb);

void setup(){
  pinMode(13, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
  
  servo.attach(9); //attach it to pin 9
}

void loop(){
  nh.spinOnce();
  delay(1);
}
