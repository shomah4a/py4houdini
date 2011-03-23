#-*- coding:utf-8 -*-

import hou


def move_objects(x, y, z):
    '''
    /obj 以下にある geo ノードを x, y, z だけ移動させます
    '''

    obj = hou.node('/obj')

    # 子供ノードについて全部処理
    for node in obj.children():

        # ノードタイプが geo ではないなら無視
        if node.type().name() != 'geo':
            continue

        # x 座標を移動
        tx = node.parm('tx')
        tx.set(tx.eval() + x)

        # y 座標を移動
        ty = node.parm('ty')
        ty.set(ty.eval() + y)

        # z 座標を移動
        tz = node.parm('tz')
        tz.set(tz.eval() + z)



