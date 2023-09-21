import dearpygui.dearpygui as dpg
import utils as utils
import ctypes, sys

#启动获取管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False







if __name__ == "__main__":
    if is_admin():
        #程序入口，启动
        dpg.create_context()
        dpg.configure_app(manual_callback_management=True)
        dpg.create_viewport(title='GetMusic!', width=300, height=300, decorated= True)
        #注册字体
        dpg.set_viewport_large_icon("Asset/app.ico")
        with dpg.font_registry():
            with dpg.font("Asset/font.ttf",25, tag="myFont"):
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
                #  dpg.add_font_range(0x4e00, 0x9fa5)
        #监听按钮事件
        #设定软件左上角的图标
        
        
        def btn_callback():
            utils.getMusic()
        with dpg.window(tag="Base_window") as Base_window:
            dpg.bind_item_font(Base_window, "myFont")
            getBtn = dpg.add_button(label='点击获取标题!', tag="getMusicBtn")
            with dpg.item_handler_registry(tag='btn_handler') as handler:
                dpg.add_item_clicked_handler(callback = btn_callback)
            dpg.bind_item_handler_registry("getMusicBtn", "btn_handler")

            
        #viewpoint 入口
        
        dpg.show_viewport()


        #主线程循环
        while   dpg.is_dearpygui_running():
                jobs = dpg.get_callback_queue() # 获取
                dpg.run_callbacks(jobs) # 运行
                dpg.render_dearpygui_frame()

        #设定使用主窗口
        
        dpg.setup_dearpygui()
        
        dpg.set_primary_window("Base_window",True)
        dpg.start_dearpygui()
        dpg.destroy_context()
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
