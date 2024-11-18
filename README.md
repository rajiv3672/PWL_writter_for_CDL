

## I made this code for writting pwl sequence for a CDL file.



This code asks for,
1. Rise time's unit,
2. Rise time,
3. Fall time's unit,
4. Fall time,
5. The unit for time. This related to the widths of the pulses,
6. It will aslo ask for high level and low level values for the pulse, also the unit for the voltages,
7. It will ask for the source's name,
8. Name of the ports,
9. And then it will start to take the pairs when the pulses are high.

An user only have to input the values when the pulse is high, the code will calculate the times for low levels.
I hope you find it useful.   

***Here is a demo:*** This will happen after running the code.

        f=femto,
     p=pico,
     n=nano,
     u=micro,
     m=mili,
     s=socond
     The inputs are NOT case sensitive.
    
    Enter the UNIT for rise time:p
    Input is valid
    Input the rise time:100
    Enter the UNIT for fall time:p
    Input is valid
    
    Input the fall time:100
    Enter the UNIT for time of the pulse:n
    Input is valid
    Input the umit for the voltage.
     V for volt, m for milivolt.
    m
    Input the High level value for the PWL:800
    Input the Low level value for the PWL:0
    Input the instance's name:V0
    Input the +ve port's name:Y
    Input the -ve port's name:VSS
    Enter he time pairs for the duration when the signal is high.
    The code will automatically calculate the low time duration.
    Pair 1, high time 1:
    Ener E or e to stop
    0
    Pair 1, high time 2:
    25
    Pair 2, high time 1:
    Ener E or e to stop
    29
    Pair 2, high time 2:
    36
    Pair 3, high time 1:
    Ener E or e to stop
    54
    Pair 3, high time 2:
    60
    Pair 4, high time 1:
    Ener E or e to stop
    80
    Pair 4, high time 2:
    90
    Pair 5, high time 1:
    Ener E or e to stop
    99
    Pair 5, high time 2:
    100
    Pair 6, high time 1:
    Ener E or e to stop
    e
    V0 Y VSS PWL 0.0 0.8 2.5000000000000002e-08 0.8 2.5100000000000003e-08 0.0 2.89e-08 0.0 2.9e-08 0.8 3.6000000000000005e-08 0.8 3.6100000000000006e-08 0.0 5.39e-08 0.0 5.4e-08 0.8 6.000000000000001e-08 0.8 6.01e-08 0.0 7.990000000000001e-08 0.0 8e-08 0.8 9.000000000000001e-08 0.8 9.01e-08 0.0 9.89e-08 0.0 TD=0
