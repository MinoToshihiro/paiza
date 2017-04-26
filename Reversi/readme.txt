内容
Reversi.py
・mainのファイル
・TkinterでGUI表示を行う
・Cygwinから実行する場合は事前に
$ startxwin &
でCygwin/X server 0.0を立てておく必要がある
・操作のたびにupdateBoard()を行い、描画の更新を行う

ReversiBoard.py
・盤面とプレイヤー情報を保持するクラス
・正直Reversi内に組み込んでも良かった

ReversiCommon.py
・石を置いたときにひっくり返せるか、またそれらをひっくり返すといった処理の関数をまとめた
・8方向別々で冗長になってしまったが、8方向のベクトルを用意して処理した方がすっきりすると思う

参考にしたサイト
http://webpages.charter.net/erburley/Reversi-index.html
http://magayengineer.hatenablog.com/entry/2016/03/24/233152

