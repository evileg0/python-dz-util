import flet as ft
from funker import *

def main(page: ft.Page):
    page.title = "File sysyem tool"
    page.theme_mode = ft.ThemeMode.DARK

    # Переменные для путей
    copy_fpath = ft.Ref[ft.TextField]()
    copy_folder_path = ft.Ref[ft.TextField]()
    del_fpath = ft.Ref[ft.TextField]()
    gen_folder_path = ft.Ref[ft.TextField]()
    gen_slider_text = ft.Ref[ft.Text]()
    gen_slider = ft.Ref[ft.Slider]()

    # Выбор файла
    def pick_folder_result(tf: ft.TextField):
        def on_result(e: ft.FilePickerResultEvent):
            if e.path:
                tf.current.value = e.path
                page.update()

        return on_result

    def picker_file_result(tf: ft.TextField):
        def on_result(e: ft.FilePickerResultEvent):
            if e.files:
                tf.current.value = ", ".join([file.path for file in e.files])
                page.update()

        return on_result

    def on_gen_slider_change(e):
        gen_slider_text.current.value = f"Текущее значение: {int(float(e.control.value))}"
        page.update()

    # Пикеры
    copy_file_picker = ft.FilePicker(on_result=picker_file_result(copy_fpath))
    copy_folder_picker = ft.FilePicker(on_result=pick_folder_result(copy_folder_path))
    del_file_picker = ft.FilePicker(on_result=picker_file_result(del_fpath))
    gen_folder_picker = ft.FilePicker(on_result=pick_folder_result(gen_folder_path))
    page.overlay.extend([copy_file_picker, copy_folder_picker, del_file_picker, gen_folder_picker])

    # Табы
    tab_control = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Копирование",
                content=ft.Column(
                    [
                        ft.Text("Выберите файл:", size=14),
                        ft.Row(
                            [
                                ft.TextField(ref=copy_fpath, hint_text="Файл", read_only=True, expand=True),
                                ft.ElevatedButton(
                                    "Выбрать файл",
                                    icon=ft.Icons.FILE_OPEN_ROUNDED,
                                    on_click=lambda _: copy_file_picker.pick_files(
                                        allow_multiple=False,
                                        allowed_extensions=["*"]
                                    )
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.Text("Выберите папку назначения:", size=14),
                        ft.Row(
                            [
                                ft.TextField(ref=copy_folder_path, hint_text="Папка назначения", read_only=True, expand=True),
                                ft.ElevatedButton(
                                    "Выбрать папку",
                                    icon=ft.Icons.FOLDER_OPEN,
                                    on_click=lambda _: copy_folder_picker.get_directory_path()
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.ElevatedButton(
                            "Копировать",
                            icon=ft.Icons.COPY ,
                            on_click=lambda _: copy_file(copy_fpath.current.value, copy_folder_path.current.value)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),
            ft.Tab(
                text="Удаление",
                content=ft.Column(
                    [
                        ft.Text("Выберите файл:", size=14),
                        ft.Row(
                            [
                                ft.TextField(ref=del_fpath, hint_text="Файл", read_only=True, expand=True),
                                ft.ElevatedButton(
                                    "Выбрать файл",
                                    icon=ft.Icons.FILE_OPEN_ROUNDED,
                                    on_click=lambda _: del_file_picker.pick_files(
                                        allow_multiple=False,
                                        allowed_extensions=["*"]
                                    )
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.ElevatedButton(
                            "Удалить",
                            icon=ft.Icons.DELETE ,
                            on_click=lambda _: delete_file(del_fpath.current.value)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),
            ft.Tab(
                text="Подсчет",
                content=ft.Container(
                    content=ft.Text("Подсчет файлов в папке"),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ),
            ft.Tab(
                text="Поиск",
                content=ft.Container(
                    content=ft.Text("Поиск фалов"),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ),
            ft.Tab(
                text="Дата",
                content=ft.Container(
                    content=ft.Text("Добавление даты к имени файлов"),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ),
            ft.Tab(
                text="Генерация",
                content=ft.Column(
                    [
                        ft.Text("Выберите папку для генерации файлов:", size=14),
                        ft.Row(
                            [
                                ft.TextField(ref=gen_folder_path, hint_text="Папка назначения", read_only=True, expand=True),
                                ft.ElevatedButton(
                                    "Выбрать папку",
                                    icon=ft.Icons.FOLDER_OPEN,
                                    on_click=lambda _: gen_folder_picker.get_directory_path()
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.Text("Количество папок для генерации:", size=14),
                        ft.Slider(ref=gen_slider, value=1, min=1, max=100, divisions=99, label="{value}", on_change=on_gen_slider_change),
                        ft.Text(ref=gen_slider_text, value="Текущее значение: 1", size=14),
                        ft.Divider(height=20, color="transparent"),
                        ft.ElevatedButton(
                            "Генерация",
                            icon=ft.Icons.COPY ,
                            on_click=lambda _: generate_data(gen_folder_path.current.value, int(gen_slider.current.value))
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),
        ],
        expand=True
    )

    page.add(tab_control)

# Запускаем приложение
if __name__ == "__main__":
    ft.app(target=main)