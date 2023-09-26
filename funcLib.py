import numpy as np
import math

def triangle(t,frequency):
    return np.tan(np.sin(t*2*np.pi*frequency))
def sineSum(t,frequency):
    res = 0
    for i in range(100):
        res= res+np.sin((i+frequency)*(t-2*i)*2*np.pi)
    return res
def sine(t,frequency):
    return np.sin(t*frequency*2*np.pi)
def func1(t,frequency):
    return 7 * np.sin(np.sin(2 * np.pi * frequency * t)*t)
def func2(t,frequency):
    return 10 * np.tan(np.sin(2 * np.pi * frequency * t))
def func3(t,frequency):
    return np.sin(10*t)*7 * np.arctan(np.sin(np.sin(2 * np.pi * frequency * t)*t))
def func4(t,frequency):
    return 4 * (np.sin(frequency*2*np.pi*t)+np.sin((frequency-4)*2*np.pi*t))
def func5(t,frequency):
    return 4  * np.sin(np.exp(t))
def blaster(t,frequency):
    return 4 *np.sin((t*frequency*2*np.pi)*10/np.exp(frequency*t/10))