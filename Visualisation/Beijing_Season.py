import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
'Spring': [52, 45, 37, 82, 59, 45, 63, 53, 48],
'Summer': [39, 37, 23, 43, 44, 31, 42, 52, 38],
'Autumn': [36, 40, 44, 28, 42, 71, 58, 57, 46],
"Winter": [44, 51, 53, 38, 34, 50, 44, 116, 71]
}
df = pd.DataFrame(data)
df.plot.box(title="The Concentration of PM2.5 of Beijing in Each Season, 2017-2019")
plt.grid(linestyle="--", alpha=0.3)
plt.show()
