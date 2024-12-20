import viktor as vkt
import pandas as pd
import plotly.graph_objects as go


class Parametrization(vkt.Parametrization):
    explain = vkt.Text("""
# Get started with VIKTOR and ETABS
After learning the basics of VIKTOR you are now ready to create your first ETABS app🚀

Follow the step-by-step instructions in the [documentation](https://docs.viktor.ai/docs/tutorials/etabs-getting-started/?utm_source=etabs-getting-started).                                     

""")


class Controller(vkt.Controller):
    parametrization = Parametrization
