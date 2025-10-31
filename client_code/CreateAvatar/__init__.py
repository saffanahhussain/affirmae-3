from ._anvil_designer import CreateAvatarTemplate
from anvil import *
import anvil.server


class CreateAvatar(CreateAvatarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    pass

  def draw_fairy(self):
    canvas = self.fairy_canvas
    canvas.clear()

    self.Fairy_Wing.items = [
    ("Blue Wings", "Fairy Wing") 

      

# Draw it on the canvas
self.fairy_body_canvas.draw_image("theme:fairy_body.png", 50, 50)

# Draw wings
    canvas.draw_image(f"/_/theme/{self.wing_dropdown.selected_value}.png", 50, 50)

# Draw outfit
    canvas.draw_image(f"/_/theme/{self.outfit_dropdown.selected_value}.png", 50, 50)
