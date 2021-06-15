# VirtualPiano
I have created an virtual Piano with help of three modules in python
1. openCV
2. PyAutoGUI
3. mediapipe

Basic idea:
Detect the fingertips using the mediapipe model and based on the location of the fingertip, a key is pressed. This plays the corresponding tone on the piano. I've simulated this on  an online platform.
https://www.musicca.com/piano
Currently, my project works fine with this virtual piano but not with others on the web. I'll try to fix this issue and will soon come up with a solution.

To run the file:
1. install the python modules: PyAutoGUI <pip install PyAutoGUI>
                               openCV <pip install opencv-python>
                               mediapipe <pip install mediapipe>
2. Run onlinePiano.py file.
3. open https://www.musicca.com/piano
3. Bring your fingertips within the white keys on top of screen.
4. Enjoy!
