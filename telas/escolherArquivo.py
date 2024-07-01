from kaki.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivymd.uix.button import MDRaisedButton


class FileChooserPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Selecione um Arquivo"
        self.size_hint = (0.9, 0.9)
        self.content = BoxLayout(orientation="vertical")

        self.file_chooser = FileChooserListView()
        self.content.add_widget(self.file_chooser)

        btn_layout = BoxLayout(size_hint_y=None, height='50dp')
        select_button = MDRaisedButton(text="Selecionar", on_release=self.select_file)
        cancel_button = MDRaisedButton(text="Cancelar", on_release=self.dismiss)
        btn_layout.add_widget(select_button)
        btn_layout.add_widget(cancel_button)
        self.content.add_widget(btn_layout)

    def select_file(self, *args):
        selected = self.file_chooser.selection
        if selected:
            self.app.root.ids.file_path_label.text = f"Selecionado: {selected[0]}"
            self.dismiss()
