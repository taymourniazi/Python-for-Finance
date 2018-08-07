import traits.api as trapi
import traitsui.api as trui
import numpy as np

class short_rate(trapi.HasTraits):
    name = trapi.Str
    rate = trapi.Float
    time_list = trapi.Array(dtype=np.float, shape=(1, 5))
    disc_list = trapi.Array(dtype=np.float, shape=(1, 5))
    update = trapi.Button
    def _update_fired(self):
        self.disc_list = np.exp(-self.rate * self.time_list)
    v = trui.View(trui.Group(trui.Item(name = 'name'),
                             trui.Item(name='rate'),
                             trui.Item(name='time_list',
                                       label='Insert Time List Here'),
                             trui.Item('update', show_label=False),
                             trui.Item(name='disc_list',
                                       label='Press Update for Factors'),
                             show_border=True, label='Calculate Discount Factors'),
                  buttons = [trui.OKButton, trui.CancelButton],
                  resizable = True)

sr = short_rate()
sr.configure_traits()