import pandas as pd

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:95% !important; }</style>"))


housing = pd.read_csv("../data/names/City_MedianRentalPrice_1Bedroom.csv")
