
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
    <hou.ObjNode of type geo at /obj/sphere_object1>

hou.node(' と打った後に少し待つと、ノードパスの補完候補が表示されます。
メソッドやモジュール名と同様に補完入力が可能です。

.. image:: _static/images/node.png


選択しているノードを取得する
----------------------------

現在 UI 上で選択しているノードのオブジェクトを取得するには、 hou.selectedNodes 関数を使用します。
この館数を実行すると、選択しているノードオブジェクトが返されます。

.. code-block:: python

    >>> nodes = hou.selectedNodes()
    >>> nodes
    (<hou.ObjNode of type geo at /obj/sphere_object1>,)

selectedNodes の結果を for 文で反復処理することで、一つ一つのノードに対して処理を行えます。

.. code-block:: python

    >>> for node in nodes:
    ...     print node.name()
    ...
    sphere_object1


Node のパラメータ
=================

Under construntion


Node を辿る
===========

ノードオブジェクトからノードに対する入力と出力を辿ることができます。

:download:`このサンプルシーン <_static/scenes/blend.hipnc>` には、 box, sphere, blend のノードがあります。

このシーンの中の blend ノードから、入力ノードを取得するには、ノードの inputs メソッドを使用します。

.. code-block:: python

    >>> blend = hou.node('/obj/blend1')
    >>> blend.inputs()
    (<hou.ObjNode of type geo at /obj/box_object1>, <hou.ObjNode of type geo at /obj/sphere_object1>)


また、 box ノードから出力先ノードを取得するには、 ノードの outputs メソッドを使用します。

.. code-block:: python

    >>> box = hou.node('/obj/box_object1')
    >>> box.outputs()
    (<hou.ObjNode of type blend at /obj/blend1>,)


それぞれのメソッドの結果は、ノードオブジェクトのタプルなので、同様の処理を再帰的に行うことも可能です。
