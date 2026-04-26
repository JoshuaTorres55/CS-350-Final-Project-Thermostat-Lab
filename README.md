# CS 350 Embedded Systems Portfolio

## Project Description

This project focuses on building a working embedded smart thermostat system using a Raspberry Pi and multiple hardware components. The system combines a temperature sensor, GPIO-controlled LEDs, physical buttons, and UART communication to simulate a real embedded device. A state machine is used to manage system behavior across off, heating, and cooling modes based on real-time sensor input and user interaction.

The main goal of the project was to understand how hardware and software work together in an embedded system and how real-time data drives system decisions.

---

## Selected Artifacts

### 1. Temperature and Humidity Sensor Integration (6-3 Assignment)

This artifact shows my work integrating an I2C temperature and humidity sensor into the system. It demonstrates how I pulled real sensor data into the program and used it to influence system behavior. This was an important step in understanding how hardware sensors actually communicate with software in an embedded environment.

### 2. Smart Thermostat System (7-1 Final Project)

This artifact represents the full system implementation. It includes sensor input, LED output, button input, UART communication, and a state machine controlling the overall behavior. This project brings together all the hardware components into one working system that reacts to temperature changes and user input.

---

## Problem Being Solved

The goal was to build a functioning thermostat prototype that can read temperature, allow user adjustments, and respond by switching between heating and cooling states. It simulates how real embedded systems work in smart home devices where hardware inputs directly control system behavior.

---

## What I Did Well

One of the strongest parts of my work was getting the system logic to function correctly through a state machine. Once the states were structured properly, the system behavior became predictable and consistent.

I also eventually got all the hardware components working together, including sensors, LEDs, and buttons. When things did not work, I stayed with the problem and worked through it instead of restarting from scratch.

---

## Areas for Improvement

The biggest issue for me in this course was wiring and initial setup. I was catching up on assignments week by week, so I was often rushing to get things working. Because of that, my wiring was not always planned carefully, which led to a lot of confusion during debugging.

Most of my time ended up being spent figuring out whether problems were coming from hardware or code. I learned that better planning at the beginning would have saved a lot of time later.

I also did not create a proper state machine diagram, which would have helped document the system more clearly.

---

## Tools and Resources Used

I mainly used course materials and lab guides to understand how each component was supposed to work. When I got stuck, I relied heavily on trial and error and testing different setups until I could see what worked.

A big part of my learning process was what I would call “breaking it,” meaning I would test different configurations, see what failed, and use that to figure out the correct setup. This helped me understand the system at a deeper level instead of just following instructions.

---

## Transferable Skills

This project helped me build real skills in debugging hardware and software systems working together. I improved at isolating problems instead of guessing, especially when dealing with wiring issues.

I also gained experience working with state machines and understanding how structured logic controls system behavior. These skills apply directly to other embedded systems and software development work.

---

## Maintainability and Design

The system is organized around a state machine, which keeps the logic structured and easier to follow. Each part of the system has a clear role, including sensor input, user input, and output control.

Even though the initial build was messy due to rushed setup, the final code structure is readable and can be extended or modified without rewriting the entire system.

---

## Reflection

This project was more challenging than it looked at the beginning because small hardware mistakes caused larger system issues. I spent most of my time debugging wiring problems rather than writing code.

Even though it was frustrating at times, it helped me understand how real embedded systems behave when hardware and software interact. I also learned that slowing down and planning the physical setup is just as important as writing the code.

Overall, I finished the course with a better understanding of how embedded systems are actually built and how much patience and testing is required to make them work reliably.
