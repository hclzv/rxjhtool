from pywinauto import Application
app = Application(backend="win32").connect(title_re=".*Notepad*")
dlg = app.window(title_re=".*Notepad.*")
# 找到编辑框控件
edit = dlg.Edit

# 设置文本
edit.set_edit_text("Hello pywinauto!")  # 背景发送，不依赖焦点

# 或追加文字
edit.type_keys(" More text", with_spaces=True)


# 找到编辑框控件
edit = dlg.Edit

# # 设置文本
# edit.set_edit_text("Hello pywinauto!")  # 背景发送，不依赖焦点

# # 或追加文字
# edit.type_keys(" More text", with_spaces=True)

edit.type_keys("^v")
