import badger2040
from badger_ui.base import App

from .tracker_screen import TrackerScreen


class MyApp(App):
  def __init__(self):
    super().__init__()

    self.child = TrackerScreen()
