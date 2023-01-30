import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
import json
import base64
from io import BytesIO

df = pd.read_csv('sample_data.csv')
voltage = df['Step']
current = df['I_current (Micro Amp)']
voltage_data = np.array(voltage)
current_data = np.array(current)
peaks = find_peaks(current_data,distance=90,height=0)
local_maxima = argrelextrema(current_data, np.greater)
# print(current_data[local_maxima[0]])
# print(current_data[peaks[0]])
plt.plot(voltage,current,'g',label = 'voltammetric curve', )
plt.plot(voltage[local_maxima[0]], current[local_maxima[0]],'ro',label = 'local maxima')
plt.plot(voltage[peaks[0]],current[peaks[0]],'bo',label = 'peak')
plt.grid()
plt.xlabel ('Voltage')
plt.ylabel ('I_current (Micro Amp)')
plt.legend()

print("local maximas : ")
print(current_data[local_maxima[0]])

print("peaks : ")
print(current_data[peaks[0]])
buf = BytesIO()
plt.savefig(buf,format='png')
buf.seek(0)
plt.savefig('hi.png')
plt.show()
image_based64 = base64.b64encode(buf.getvalue()).decode('utf-8')

output_data = {'peaks' : current[peaks[0]].tolist(),'image':image_based64}
print(output_data)
with open("local_maxima.json","w") as f:
    json.dump(output_data,f)
