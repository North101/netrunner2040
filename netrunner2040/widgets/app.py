import badger2040
from badger_ui.base import App

from .tracker_screen import TrackerScreen


class MyApp(App):
  def __init__(self, display: badger2040.Badger2040):
    super().__init__(display=display)

    self.child = TrackerScreen()
