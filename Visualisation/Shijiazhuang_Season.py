import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
'Spring': [62, 52, 34, 98, 57, 47, 79, 53, 56],
'Summer': [55, 59, 50, 39, 40, 33, 39, 37, 27],
'Autumn': [35, 51, 72, 37, 61, 100, 66, 80, 78],
"Winter": [200, 139, 93, 112, 95, 89, 145, 121, 83]
}
df = pd.DataFrame(data)
df.plot.box(title="The Concentration of PM2.5 of Shijiazhuang in Each Season, 2017-2019")
plt.grid(linestyle="--", alpha=0.3)
plt.show()
