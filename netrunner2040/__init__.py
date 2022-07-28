import badger2040

from netrunner2040.widgets.app import MyApp


def start():
  display = badger2040.Badger2040()
  display.update_speed(badger2040.UPDATE_TURBO)

  app = MyApp(display=display)
  app.run()

