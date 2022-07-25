import badger2040
from badger_ui.base import Widget, WidgetMixin
from badger_ui.util import Image, Offset, Size


class UnitWidget(Widget):
  def __init__(
      self, parent: WidgetMixin, size: Size, value: int, image: Image, selected: bool,
      offset: Offset = None,
  ):
    super().__init__(parent, size, offset)

    self.value = value
    self.image = image
    self.selected = selected
    self.text_scale = 1.5

  def on_button(self, pressed: dict[int, bool]) -> bool:
    if pressed[badger2040.BUTTON_UP]:
      self.value += 1
      return True

    elif pressed[badger2040.BUTTON_DOWN]:
      self.value = max(self.value - 1, 0)
      return True

    return super().on_button(pressed)

  def render(self):
    self.display.pen(0)
    self.display.thickness(2)

    value_text = f'{self.value}'
    height = self.size.height
    width = self.size.width

    value_width = self.display.measure_text(value_text, scale=self.text_scale)
    image_width = self.image.width
    center_x = (width // 2)
    image_height = self.image.height
    self.display.text(
        value_text,
        self.display_offset.x + center_x - ((value_width + image_width) // 2),
        self.display_offset.y + (height // 2),
        scale=self.text_scale,
    )
    self.image.draw(
        self.display,
        Offset(
            x=self.display_offset.x + center_x + ((value_width + image_width) // 2) - image_width,
            y=self.display_offset.y + (height // 2) - (image_height // 2),
        )
    )
    if self.selected:
      self.display.line(
          self.display_offset.x + center_x - ((value_width + image_width) // 2),
          self.display_offset.y + (height // 2) + (image_height // 2),
          self.display_offset.x + center_x + ((value_width + image_width) // 2),
          self.display_offset.y + (height // 2) + (image_height // 2),
      )


class ClickUnitWidget(UnitWidget):
  def on_button(self, pressed: dict[int, bool]) -> bool:
    if pressed[badger2040.BUTTON_UP]:
      self.value += 1
      return True

    elif pressed[badger2040.BUTTON_DOWN]:
      self.value -= 1
      if self.value < 0:
        self.value = 4
      return True

    return super().on_button(pressed)
