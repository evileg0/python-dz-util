import flet as ft
from funker import *

def main(page: ft.Page):
    page.title = "File sysyem tool"
    page.theme_mode = ft.ThemeMode.DARK

    # Переменные для путей
    copy_fpath = ft.Ref[ft.TextField]()
    copy_folder_path = ft.Ref[ft.TextField]()
    del_fpath = ft.Ref[ft.TextField]()

    # Выбор файла
    def pick_copy_folder_result(e: ft.FilePickerResultEvent):
        if e.path:
            copy_folder_path.current.value = e.path
            page.update()

    def picker_file_result(tf: ft.TextField):
        def on_result(e: ft.FilePickerResultEvent):
            if e.files:
                tf.current.value = ", ".join([file.path for file in e.files])
                page.update()

        return on_result

    # Пикеры
    file_picker = ft.FilePicker(on_result=picker_file_result(copy_fpath))
    folder_picker = ft.FilePicker(on_result=pick_copy_folder_result)
    del_file_picker = ft.FilePicker(on_result=picker_file_result(del_fpath))
    page.overlay.extend([file_picker, folder_picker,del_file_picker])

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
                                    on_click=lambda _: file_picker.pick_files(
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
                                ft.TextField(ref=copy_folder_path, hint_text="Папка назвачения", read_only=True, expand=True),
                                ft.ElevatedButton(
                                    "Выбрать папку",
                                    icon=ft.Icons.FOLDER_OPEN,
                                    on_click=lambda _: folder_picker.get_directory_path()
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
                content=ft.Container(
                    content=ft.Text("Генерация файлов"),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ),
        ],
        expand=True
    )

    page.add(tab_control)

# Запускаем приложение
if __name__ == "__main__":
    ft.app(target=main)