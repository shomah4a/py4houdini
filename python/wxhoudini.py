#-*- coding:utf-8 -*-

# c: にある Python のパスを追加
import site
path = 'c:/Python26/Lib/site-packages'
site.addsitedir(path)

import wx
import hou

app = wx.PySimpleApp()

window_count = 0

main_loop = None


def make_callback():

    evt_loop = wx.EventLoop()

    def event_callback():
        
        while evt_loop.Pending():
            evt_loop.Dispatch()
            app.ProcessPendingEvents()

    wx.EventLoop.SetActive(evt_loop)

    return event_callback



def incref():
    '''
    window が追加されたときに呼ばれる
    '''

    global window_count, main_loop
    
    if window_count == 0:
        callback = make_callback()
        hou.ui.addEventLoopCallback(callback)
        main_loop = callback

    window_count += 1



def decref():
    '''
    window がなくなったときに呼ばれる
    '''

    global window_count

    window_count -= 1

    if window_count:
        return

    main_loop()
    hou.ui.removeEventLoopCallback(main_loop)



def register_window(window):
    '''
    window を登録する
    '''
    
    def on_close(evt):

        if hasattr(window, 'onClose'):
            window.onClose(evt)

        window.Show(False)
        window.Destroy()

        decref()


    window.Bind(wx.EVT_CLOSE, on_close)

    incref()


def test():
    frame = wx.Frame(None)

    register_window(frame)
    frame.Show()

            
        
