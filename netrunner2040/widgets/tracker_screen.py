from collections import namedtuple

import badger2040
from badger_ui.base import Widget, WidgetMixin
from badger_ui.util import Image, Offset, Size

from .unit import ClickUnitWidget, UnitWidget


class TrackerScreen(Widget):
  def __init__(self, parent: WidgetMixin, size: Size, offset: Offset = None):
    super().__init__(parent, size, offset)

    self.selected_index = 0
    self.units: list[UnitWidget] = []

    click_image = Image('netrunner2040/assets/click.bin', 32, 32)
    click_image.load()
    self.units.append(ClickUnitWidget(
      self,
      Size(self.size.width // 3, self.size.height),
      4,
      click_image,
      self.selected_index == 0,
      offset=Offset(0, 0),
    ))

    mu_image = Image('netrunner2040/assets/mu.bin', 32, 32)
    mu_image.load()
    self.units.append(UnitWidget(
      self,
      Size(self.size.width // 3, self.size.height),
      4,
      mu_image,
      self.selected_index == 2,
      offset=Offset(size.width // 3, 0),
    ))

    credit_image = Image('netrunner2040/assets/credit.bin', 32, 32)
    credit_image.load()
    self.units.append(UnitWidget(
      self,
      Size(self.size.width // 3, self.size.height),
      5,
      credit_image,
      self.selected_index == 1,
      offset=Offset(size.width // 3 * 2, 0),
    ))

  def on_button(self, pressed: dict[int, bool]):
    if pressed[badger2040.BUTTON_A]:
      self.set_selected(0)
      return True

    elif pressed[badger2040.BUTTON_B]:
      self.set_selected(1)
      return True

    elif pressed[badger2040.BUTTON_C]:
      self.set_selected(2)
      return True

    elif pressed[badger2040.BUTTON_UP]:
      return self.units[self.selected_index].on_button(pressed)

    elif pressed[badger2040.BUTTON_DOWN]:
      return self.units[self.selected_index].on_button(pressed)

    return super().on_button(pressed)
  
  def set_selected(self, select: int):
    self.selected_index = select
    for i, unit in enumerate(self.units):
      unit.selected = (i == select)

  def render(self):
    super().render()

    for unit in self.units:
      unit.render()
