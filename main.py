import dearpygui.dearpygui as dpg

#程序入口，启动
dpg.create_context()
dpg.create_viewport(title='GetMusic!', width=300, height=300, decorated= True)


#注册字体
with dpg.font_registry():
    with dpg.font("Asset/font.ttf",25, tag="myFont"):
         dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
         dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
        #  dpg.add_font_range(0x4e00, 0x9fa5)

with dpg.window(tag="Base_window") as Base_window:
    dpg.bind_item_font(Base_window, "myFont")
    dpg.add_button(label='点击获取标题!',callback=getMusic)
    
# with dpg.window(label="音乐"):
#     dpg.add_text("Hello, world")
#     dpg.add_button(label="Save")
#     dpg.add_input_text(label="string", default_value="Quick brown fox")
#     dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.set_viewport_large_icon("Asset/app.ico")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Base_window",True)
dpg.start_dearpygui()
dpg.destroy_context()