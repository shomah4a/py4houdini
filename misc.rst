
==========
その他色々
==========

hscript との連携
================

Houdini のシーンに対する操作は、 Python だけでほぼ完結しますが、たまに Python 側にインタフェイスが提供されていない機能があります。
そのような場合は hscript のコマンドを Python から呼び出して使います。

Python から hscript を実行するには

.. function:: hou.hscript(command)

を使用します。

hscript 関数に hscript として実行できる文字列を渡すと、実行した結果が二要素のタプルとして返されます。

タプルの一番目の要素はコマンドを実行した結果の標準出力の文字列、二番目の要素は標準エラーの文字列です。

使い方は以下の通りです。

.. code-block:: python

    >>> hou.hscript('echo hello, houdini')
    ('hello, houdini\r\n', '')
    >>> hou.hscript('unknowncommand')
    ('', 'Unknown command: unknowncommand\r\n')



Python 単体での実行
===================

Under Construction




