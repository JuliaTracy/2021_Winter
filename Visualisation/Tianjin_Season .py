import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
'Spring': [70, 64, 41, 75, 44, 38, 54, 49, 41],
'Summer': [42, 41, 26, 40, 38, 29, 46, 52, 37],
'Autumn': [54, 62, 53, 30, 44, 79, 41, 50, 51],
"Winter": [61, 81, 78, 53, 60, 53, 69, 109, 85]
}
df = pd.DataFrame(data)
df.plot.box(title="The Concentration of PM2.5 of Tianjin in Each Season, 2017-2019")
plt.grid(linestyle="--", alpha=0.3)
plt.show()
