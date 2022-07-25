import badger2040
from badger_ui import App
from badger_ui.util import Offset, Size

from .tracker_screen import TrackerScreen


class MyApp(App):
  def __init__(
      self,
      display: badger2040.Badger2040,
      size=Size(width=badger2040.WIDTH, height=badger2040.HEIGHT),
      clear_color: int = 15,
      offset: Offset = None,
  ):
    super().__init__(display=display, size=size, clear_color=clear_color, offset=offset)

    self.screen = TrackerScreen(
        parent=self,
        size=self.size,
    )

  def on_button(self, pressed: dict[int, bool]):
    return self.screen.on_button(pressed)

  def render(self):
    self.screen.render()
