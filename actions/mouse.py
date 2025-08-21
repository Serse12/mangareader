def on_mouse_wheel(event, canvas):
    # On Windows, event.delta is typically 120 or -120
    # On Linux, event.delta can be 120 or -120, or event.num can be 4 or 5
    if event.num == 5 or event.delta == -120:
        canvas.yview_scroll(1, "units")
    elif event.num == 4 or event.delta == 120:
        canvas.yview_scroll(-1, "units")
