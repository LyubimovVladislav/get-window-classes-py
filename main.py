import win32gui

def get_window_class_names():
    class_names = []

    def enum_callback(hwnd, _):
        class_name = win32gui.GetClassName(hwnd)
        class_names.append(class_name)
        return True

    win32gui.EnumWindows(enum_callback, None)
    return class_names


class_names = get_window_class_names()
for class_name in class_names:
    print(class_name)

