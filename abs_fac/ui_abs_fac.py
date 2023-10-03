# Abstract Factory
class UIFactory:
    def create_button(self):
        pass

    def create_dialog(self):
        pass

# Concrete Factory 1: Windows Factory
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_dialog(self):
        return WindowsDialog()

# Concrete Factory 2: macOS Factory
class MacOSFactory(UIFactory):
    def create_button(self):
        return MacOSButton()

    def create_dialog(self):
        return MacOSDialog()

# Abstract Product: Button
class Button:
    def paint(self):
        pass

# Concrete Product 1: Windows Button
class WindowsButton(Button):
    def paint(self):
        return "Windows style button"

# Concrete Product 2: MacOS Button
class MacOSButton(Button):
    def paint(self):
        return "MacOS style button"

# Abstract Product: Dialog
class Dialog:
    def render(self):
        pass

# Concrete Product 1: Windows Dialog
class WindowsDialog(Dialog):
    def render(self):
        return "Windows style dialog"

# Concrete Product 2: MacOS Dialog
class MacOSDialog(Dialog):
    def render(self):
        return "MacOS style dialog"

# Client
def create_ui(factory):
    button = factory.create_button()
    dialog = factory.create_dialog()
    return button, dialog

# Usage
windows_ui = create_ui(WindowsFactory())
macos_ui = create_ui(MacOSFactory())

print(windows_ui[0].paint())  # Output: Windows style button
print(windows_ui[1].render())  # Output: Windows style dialog

print(macos_ui[0].paint())     # Output: MacOS style button
print(macos_ui[1].render())    # Output: MacOS style dialog
