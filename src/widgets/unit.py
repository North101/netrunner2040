import badger2040w
from badger_ui.base import App, Widget
from badger_ui.util import Image, Offset, Size


class UnitWidget(Widget):
  def __init__(self, value: int, image: Image, selected: bool):
    self.value = value
    self.image = image
    self.selected = selected
    self.text_scale = 1.5

  def on_button(self, app: App, pressed: dict[int, bool]) -> bool:
    if pressed[badger2040w.BUTTON_UP]:
      self.value += 1
      return True

    elif pressed[badger2040w.BUTTON_DOWN]:
      self.value = max(self.value - 1, 0)
      return True

    return super().on_button(app, pressed)

  def render(self, app: 'App', size: Size, offset: Offset):
    app.display.set_pen(0)
    app.display.set_thickness(2)

    value_text = f'{self.value}'
    height = size.height
    width = size.width

    value_width = app.display.measure_text(value_text, scale=self.text_scale)
    image_width = self.image.width
    center_x = (width // 2)
    image_height = self.image.height
    app.display.text(
        value_text,
        offset.x + center_x - ((value_width + image_width) // 2),
        offset.y + (height // 2),
        scale=self.text_scale,
    )
    self.image.draw(
        app.display,
        Offset(
            x=offset.x + center_x + ((value_width + image_width) // 2) - image_width,
            y=offset.y + (height // 2) - (image_height // 2),
        )
    )
    if self.selected:
      app.display.line(
          offset.x + center_x - ((value_width + image_width) // 2),
          offset.y + (height // 2) + (image_height // 2),
          offset.x + center_x + ((value_width + image_width) // 2),
          offset.y + (height // 2) + (image_height // 2),
      )


class ClickUnitWidget(UnitWidget):
  def on_button(self, app: App, pressed: dict[int, bool]) -> bool:
    if pressed[badger2040w.BUTTON_UP]:
      self.value += 1
      return True

    elif pressed[badger2040w.BUTTON_DOWN]:
      self.value -= 1
      if self.value < 0:
        self.value = 4
      return True

    return super().on_button(app, pressed)
