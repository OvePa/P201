"""
any
The any built-in accepts an iterable and will return True if any element in
the given iterable is True.
"""
print(any([0, 0, 0, 1]))
# ----------
widget_one = ""
widget_two = ""
widget_three = "button"
widgets_exist = any([widget_one, widget_two, widget_three])
print(widgets_exist)
