import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
import json
import base64
from io import BytesIO

df = pd.read_csv('forward_peak.csv')
data = df['I_current (Micro Amp)']
data = np.array(data)
peaks = find_peaks(data,threshold=3)
local_maxima = argrelextrema(data, np.greater)
# print(data[local_maxima[0]])
# print(data[peaks[0]])
plt.plot(data,label = 'I_current (Micro Amp)')
plt.plot(local_maxima[0], data[local_maxima],'ro',label = 'local maxima')

plt.plot(peaks[0],data[peaks[0]],'bo',label = 'peak')
plt.xlabel ('Data Points')
plt.ylabel ('I_current (Micro Amp)')
plt.legend()

print("local maximas : ")
print(data[local_maxima[0]])

print("peaks : ")
print(data[peaks[0]])
buf = BytesIO()
plt.savefig(buf,format='png')
buf.seek(0)
plt.savefig('hi.png')
plt.show()
image_based64 = base64.b64encode(buf.getvalue()).decode('utf-8')

#print(image_based64)

output_data = {'local_maxima' : local_maxima[0].tolist(), 'peaks' : peaks[0].tolist(),'image':image_based64}
print(output_data)
with open("local_maxima.json","w") as f:
    json.dump(output_data,f)
