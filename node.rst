
===========
Node の操作
===========

Node オブジェクト
=================

Houdini のシーン上に存在するすべての要素(ジオメトリ・カメラ・マテリアル・画像等々)はすべてノードとして扱われています。
hou モジュールでは、すべてのオブジェクトをノード単位で扱えます。

以下は /obj/sphere_object1 のノードを取得する例です。

.. code-block:: python

    >>> n = hou.node('/obj/sphere_object1')
    >>> n
    <hou.ObjNode of type get at /obj/sphere_object1>

hou.node(' と打った後に少し待つと、ノードパスの補完候補が表示されます。
メソッドやモジュール名と同様に補完入力が可能です。

.. image:: _static/images/node.png


