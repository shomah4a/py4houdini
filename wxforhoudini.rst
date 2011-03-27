
==============================
wxPython を使用しての GUI 作成
==============================

イベントループの統合
====================

wxPython を Houdini 上で利用する場合は、 Houdini の GUI イベントループの上で wxPython のイベントループを動かさなければいけません。

`Houdini のドキュメント <http://www.sidefx.com/docs/houdini11.0/hom/cookbook/wxPython/>`_ にはそのためのサンプルコードが載っています。
ただし、これはウィンドウが複数作られることを考慮していないようなので、それらを考慮した別バージョンを作成しました。

:download:`wxhoudini.py <python/wxhoudini.py>` をダウンロードして、パスが通った場所においてください。

.. literalinclude:: python/wxhoudini.py


これを使って GUI を作る場合は、以下のようにします。


.. code-block:: python

    import wxhoudini
    import wx

    frame = wx.Frame(None)
    wxhoudini.register_window(frame)


使用する際に気をつけなければいけない点がいくつかあります。

* wx モジュールより前に wxhoudini モジュールを読み込む

  * wxhoudini モジュール内部で wx モジュールへのパスを通しているため
  * wx の初期化処理を wxhoudini インポート時に行っているため

* wx で作成したウィンドウは wxhoudini.register_window を使用して登録する

  * イベントループの統合と統合解除を行うため

* Python Shell からは使用せず、 Shelf に登録して実行する

  * Python Shell は Houdini UI とは別スレッドで動いている
  * そのため、 Python Shell から wx の UI を作成すると、イベントが渡ってこなくなる






