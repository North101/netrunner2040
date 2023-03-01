root_dir = '/'.join(__file__.rsplit('/')[:-1])
assets_dir = f'{root_dir}/assets'

def start():
  from netrunner2040.widgets.app import MyApp

  app = MyApp()
  app.run()
