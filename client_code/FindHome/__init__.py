from ._anvil_designer import FindHomeTemplate
from anvil import *


class FindHome(FindHomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
