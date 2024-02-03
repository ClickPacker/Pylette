from pylett.messages import *

style = CreateStyle(text_color='red', style_modifiers=['bold'], background_color='black', indent=True)

print(style.print_message('123'))