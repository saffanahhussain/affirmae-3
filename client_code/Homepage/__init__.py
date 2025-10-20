from ._anvil_designer import HomepageTemplate
from anvil import *


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Create_Avatar_Link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('CreateAvatar')

  def Find_Home_Link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('FindHome')

  
  
