# The Commentary Box (CommBox)

Modern day cricket is fast. So, reporting live commentary in textual form on various sports websites like CricBuzz becomes difficult. Here, we try to solve this issue.

This system uses **accelerometer** and **gyroscope** readings recorded from a **sensor** on a **wrist band** worn by the batsman, to **classify the shot played** with good accuracy.

This project got **awarded** the **[Best Academic Demo Award](http://www.comsnets.org/awards.html)** in International Conference on Communication Systems and Networks (**COMSNETS 2017**) for the paper titled, "*CommBox*: Utilizing Sensors for Real-Time Cricket Shot Identification and Commentary Generation"

Have a look at the video demo attached for details.

# Approach

We used MetaWear CPRO, a coin sized sensor provided by Mbient Lab.

1. The sensor is worn with a wrist band by the bastman and continuously records accelerometer and gyroscope data.

2. A smartphone is place in the pocket of the batsman which records the sound level in its surroundings

3. As the ball hits the bat, the sound level produced crosses a high threshold and the sensor data from few milliseconds before and after the "hit" are sent to a server.

4. The server then forms features from this data and runs a multi-class classifier to identify the shot played by the batsman and the corresponding commentary is played on the speaker.

# Results

- For identification of 3 distinct shots, 'PULL', 'STRAIGHT DRIVE' and 'CUT', we get ~96 % accuracy.
- On including 2 confusing shots as well, we get ~90 % accuracy.

More details on the approach and results can be seen from the research paper attached.