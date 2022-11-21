import badger2040
from badger_ui.base import App, Widget
from badger_ui.row import Row
from badger_ui.sized import SizedBox
from badger_ui.util import Image, Offset, Size

from netrunner2040 import assets_dir
from .unit import ClickUnitWidget, UnitWidget


class TrackerScreen(Widget):
  def __init__(self):
    self.selected_index = 0
    self.values = [
        4,
        4,
        5,
    ]

    self.images = [
        Image(f'{assets_dir}/click.bin', 32, 32),
        Image(f'{assets_dir}/mu.bin', 32, 32),
        Image(f'{assets_dir}/credit.bin', 32, 32),
    ]
    for image in self.images:
      image.load()

  def on_button(self, app: App, pressed: dict[int, bool]):
    if pressed[badger2040.BUTTON_A]:
      self.selected_index = 0
      return True

    elif pressed[badger2040.BUTTON_B]:
      self.selected_index = 1
      return True

    elif pressed[badger2040.BUTTON_C]:
      self.selected_index = 2
      return True

    elif pressed[badger2040.BUTTON_UP]:
      self.values[self.selected_index] += 1
      return True

    elif pressed[badger2040.BUTTON_DOWN]:
      if self.selected_index == 0:
        self.values[self.selected_index] -= 1
        if self.values[self.selected_index] < 0:
          self.values[self.selected_index] = 4
      else:
        self.values[self.selected_index] = max(self.values[self.selected_index] - 1, 0)
      return True

    return super().on_button(app, pressed)

  def render(self, app: 'App', size: Size, offset: Offset):
    Row(children=[
        SizedBox(
            child=UnitWidget(
                value,
                self.images[i],
                self.selected_index == i,
            ),
            size=Size(size.width // 3, size.height),
        )
        for i, value in enumerate(self.values)
    ]).render(app, size, offset)
