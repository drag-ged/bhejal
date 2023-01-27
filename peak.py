import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import json
import base64
from io import BytesIO

df = pd.read_excel('epicatechin data.xlsx')
data = df['I_current (Micro Amp)']
data = np.array(data)
local_maxima = argrelextrema(data, np.greater)

plt.plot(data,label = 'I_current (Micro Amp)')

plt.plot(local_maxima[0], data[local_maxima],'ro',label = 'local maxima')

plt.xlabel ('Data Points')
plt.ylabel ('I_current (Micro Amp)')
plt.legend()

buf = BytesIO()
#plt.savefig(buf,format='png')
buf.seek(0)
#plt.savefig('hi.png')

image_based64 = base64.b64encode(buf.getvalue()).decode('utf-8')

print(image_based64)

output_data = {'local_maxima' : local_maxima[0].tolist(),'image':image_based64}

with open("local_maxima.json","w") as f:
    json.dump(output_data,f)