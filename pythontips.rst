
=====================
Python での文字列操作
=====================

最近ではスクリプト言語は LL(Lightweight Language) と呼ばれることがあります。
Python をはじめとして Ruby, Scala, Lua, Squirrel, Perl, PHP などがそれに当たります。
軽量言語は、プログラマの負担を減らし、生産性を高めるための様々な機能を言語標準で持っていることがほとんどです。

ここでの軽量、とは C のような低級言語に対してより少ない記述で多くのことを記述できる、といった意味を持っています。

軽量言語の特徴がよく出てくるのが文字列処理です。 C 言語において文字列処理というものは、メモリのコピー操作を伴い、常にバッファオーバフローなどのバグを意識しながら書かなければいけないとても面倒なものです。
それに引き替え LL における文字列処理は、言語組み込みの文字列型を用い、四則演算を行う程度の手軽さで文字列を扱うことができるようになっています。

ここでは、軽量言語 Python においてよく使われる文字列操作の関数・メソッドを挙げています。


リテラル
========

raw 文字列
----------

Python における文字列定数を表現する方法には 2 種類あります。

まずは通常の文字列です。

.. code-block:: python

    >>> 'hello, python'
    'hello, python'


次に、 raw 文字列です。

.. code-block:: python

    >>> print 'test\ntest'
    test
    test
    >>> print r'test\ntest'
    test\ntest

一つ目の print 文では、test と test の間にある \n は改行文字として解釈され、改行が出力されています。
それに対して二つ目の print 文では、文字列リテラルの前に r が付けられており、途中の \n はそのまま \n という二文字として解釈されています。
この、文字列リテラルの前に r が着いている文字列を raw 文字列といいます。 raw 文字列の内部ではバックスラッシュによるエスケープ処理が行われず、バックスラッシュはバックスラッシュとして認識されます。


文字列演算
==========

Python では、文字列に対して + や * などによる演算を行えます。

.. code-block:: python

    >>> 'aaa' + 'bbb'
    'aaabbb'
    >>> 'aa' * 4
    'aaaaaaaa'

一つ目は文字列の連結です。これは特に説明する必要はないでしょう。
二つ目は文字列の繰り返しです。
'aa' * 4 とすることで、  'aa' を 4 回繰り返した文字列が生成されます。


文字列メソッド
==============

ここでは、代表的な文字列のメソッドを見ていきます。

Python ライブラリリファレンスでは

* `6.6 シーケンス型 <http://www.python.jp/doc/release/library/stdtypes.html#str-unicode-list-tuple-buffer-xrange>`_
* `6.6.1 文字列メソッド <http://www.python.jp/doc/release/library/stdtypes.html#string-methods>`_

あたりが該当します。


.. method:: str.replace(self, target, replaced)

    文字列を置換します。


.. code-block:: python

    >>> 'aaabbbaaa'.replace('aaa', 'ccc')
    'cccbbbccc'


.. method:: str.upper(self)

    大文字にします。

.. method:: str.lower(self)

    小文字化にします。

.. code-block:: python

    >>> 'aBa'.upper()
    'ABA'
    >>> 'Test'.lower()
    'test'


.. method:: str.split(self[, sep])

    指定した文字列で分割します。
    何も渡さない場合は空白文字で分割します。


.. code-block:: python

    >>> 'a b c'.split()
    ['a', 'b', 'c']
    >>> 'a,b,c'.split(',')
    ['a', 'b', 'c']


.. method:: str.lstrip(self)
.. method:: str.rstrip(self)
.. method:: str.strip(self)

    文字列の前または後または前後の空白文字を取り除きます。

.. code-block:: python

    >>> a = '  nnn   '
    >>> a.lstrip()
    'nnn   '
    >>> a.rstrip()
    '   nnn'
    >>> a.strip()
    'nnn'



パス操作関数
============

Python にはファイルパスなどの操作を簡単に行うための関数群が標準ライブラリに存在します。

* `os <http://www.python.jp/doc/release/library/os.html>`_
* `os.path <http://www.python.jp/doc/release/library/os.path.html>`_
* `glob <http://www.python.jp/doc/release/library/glob.html>`_

あたりのモジュールが該当します。

これらの関数は OS によってパスの区切り文字(/と\)を自動的に使い分けてくれるので、パスの操作はなるべくこれらの関数で行いましょう。


.. function:: os.path.join(*pathes)

パスを結合します。

.. code-block:: python

    >>> os.path.join('/aaa', 'ccc')
    '/aaa/ccc'
    >>> os.path.join('/aaa/bbb', 'ccc', 'ddd')
    '/aaa/bbb/ccc/ddd'


.. function:: os.path.basename(path)

パスからファイル名を抜き出します。

.. code-block:: python

    >>> os.path.basename('/home/dummy/test.py')
    'test.py'


.. function:: os.path.dirname(path)

パスからファイル名を取り除きます。

.. code-block:: python

    >>> os.path.dirname('/home/dummy/test.py')
    '/home/dummy'


.. function:: os.path.splitext(path)

ファイルパスと拡張子を分けます。

.. code-block:: python

    >>> os.path.splitext('/home/dummy/test.py')
    ['/home/dummy/test', '.py']


.. function:: os.path.exists(path)

ファイルの存在を確認します。


.. code-block:: python

    >>> os.path.exists('/home/dummy/test.py')
    True


.. function:: os.listdir(dirpath)

ディレクトリに存在するファイル名のリストを返します。

.. code-block:: python

    >>> os.listdir('/home/dummy')
    ['.bashrc', '.bashprofile', '.emacs.d', 'test.py', 'test.pyc']


.. function:: glob.glob(path)

ワイルドカードによるパス指定で存在するファイルのリストを返します。

.. code-block:: python

    >>> glob.glob('/home/dummy/*.py')
    ['/home/dummy/test.py']


