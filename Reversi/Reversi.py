#! /usr/bin/env python
#coding: utf-8
import Tkinter as Tk
import ttk
import ReversiCommon as rc
import ReversiBoard as rb
import os
import sys

# 環境変数の設定
os.environ['DISPLAY'] = ':0.0'

#変数
GridSize = 50 #1マスの大きさ
PieceSize = GridSize - 8 #1コマの大きさ
Offset = 2 #canvasのふちとのオフセット
BoardColor = '#008000' #ボードの色（緑）
HiliteColor = '#00a000' #ハイライト時のボードの色（薄緑）
PlayerColors = ('#008000', '#000000', '#ffffff') #コマの色（緑、黒、白）
PlayerNames = ('', 'Black', 'White') #プレイヤー名
MoveDelay = 1000 #AI用の遅延


class Reversi:
	class Square:
		def __init__(self,x,y):
			self.x, self.y = x, y #xy座標位置を保持
			self.player = 0 #そのマスにあるコマのplayerを保持
			self.squareId = 0 #マスのCanvasID
			self.pieceId = 0 #コマのCanvasID

	def __init__(self):
		"""盤面描画とメニュー表示を行う"""
		#GUI描画用のフレーム
		self.frame = Tk.Frame()
		#ウィンドウ名
		self.frame.master.wm_title('Reversi')
		#盤面描画
		size = rc.SIZE * GridSize
		self.canvas = Tk.Canvas(self.frame, width=size, height=size) #盤面の大きさ指定
		self.canvas.pack() #上から配置
		"""スタートボタンの配置"""
		self.menuFrame = Tk.Frame(self.frame) #frameを親にしてmenuFrameを生成
		#expand:親が大きくなったときそれにあわせるかどうか（Tk.Y/N）、
		#fill:空いているスペースを埋めるかどうか(Tk.X:横,Tk.Y:縦,Tk.BOTH:両方)
		self.menuFrame.pack(expand=Tk.Y,fill=Tk.X) 
		self.newGamebutton = Tk.Button(self.menuFrame,text='New Game',command=self.newGame)
		#side:どの方向からつめていくかを指定：Tk.TOP(default):上から,Tk.LEFT:左から,Tk.RIGHT:右から,Tk.BOTTOM:下から)
		#padx:外側の横の隙間、縦はpady,内側はipadx,ipady
		self.newGamebutton.pack(side=Tk.LEFT,padx=5)
		Tk.Label(self.menuFrame).pack(side=Tk.LEFT,expand=Tk.Y,fill=Tk.X)
		"""playerのAI設定"""
		self.strategies = {} #名前：その名前の関数の辞書オブジェクト作成
		optionMenuArgs = [self.menuFrame,0,"Player"]
		for s in strategies:
			name = s.getName()
			optionMenuArgs.append(name)
			self.strategies[name] = s
		self.strategyVars = [0] #ダミー作成(playerは１と２だから)
		for n in range(1,3):#Playernamesで名前があるのは１，２
			#anchor:配置可能なスペースに余裕があるとき、どこに配置するかを指定
			#デフォルトはTk.CENTER:中央,Tk.W:左,Tk.E:右,Tk.N:上,Tk.S:下,Tk.NW:左上,Tk.SW:左下,Tk.NE:右上,Tk.SE:右下
			label = Tk.Label(self.menuFrame, anchor=Tk.E, text='%s:' % PlayerNames[n])
			label.pack(side=Tk.LEFT,padx=10)
			var = Tk.StringVar() #頻繁に値が変わるものを指定
			var.set('Player')
			var.trace('w', self.strategyMenuCallback) #sstrategy~に上書き
			self.strategyVars.append(var)
			optionMenuArgs[1] = var
			menu = apply(Tk.OptionMenu,optionMenuArgs)
			menu.pack(side=Tk.LEFT)
		"""現在のステータスを表示するためのエリア"""
		#relief:周りの形を指定(Tk.FLAT(default),Tk.RAISED,Tk.SUNKENN,Tk.GROOVE,Tk.RIDGE)
		self.status = Tk.Label(self.frame,relief=Tk.SUNKEN,anchor=Tk.W)
		self.status.pack(expand=Tk.Y,fil=Tk.X)
		self.frame.pack() #大本のframeを配置

		"""盤面の追跡"""
		self.squares = {} #盤面を[x,y]で保持
		self.enabledSpaces = () #おける位置を返す
		for x in range(rc.SIZE):
			for y in range(rc.SIZE):
				square = self.squares[x,y] = Reversi.Square(x,y) #squaresそれぞれがSquareクラスを持つ
				x0 = x * GridSize + Offset
				y0 = y * GridSize + Offset
				#[x0,y0],[x0+GS,y0+GS]を対角にする四角を描画
				square.squareId = self.canvas.create_rectangle(x0,y0,x0+GridSize,y0+GridSize,
					fill=BoardColor)

		#遅延用のID（AIで働く）
		self.afterId = 0
		
		#ゲーム開始
		self.newGame()

	def play(self):
		"""ゲームを行う"""
		self.frame.mainloop()

	def postStatus(self,text):
		"""現在の状況をポスト"""
		self.status['text'] = text

	def strategyMenuCallback(self,*args):
		"""AIを変えたときに呼び出す"""
		self.updateBoard()

	def newGame(self):
		"""初期化して始める"""
		for s in self.squares.values():
			if s.pieceId:
				self.canvas.delete(s.pieceId)
				s.pieceId = 0

		"""再描画"""
		self.state = rb.ReversiBoard()
		self.updateBoard()

	def updateBoard(self):
		"""遅延やめる"""
		if self.afterId:
			self.frame.after_cancel(self.afterId)
			self.afterId = 0
		"""置ける場所のリセット"""
		self._disableSpaces()
		"""canvas再設定"""
		board = self.state.getPieces()
		for x in range(rc.SIZE):
			for y in range(rc.SIZE):
				#self.squares[x,y] = self.state.getPieceColor(x,y)
				square = self.squares[x,y] #= Reversi.Square(x,y)
				color = self.state.getPieceColor(x,y)
				if square.pieceId:
					#色が変わってたら塗りなおす（ひっくり返す）
					if square.player != color:
						self.canvas.itemconfigure(square.pieceId,fill=PlayerColors[color],
							outline=PlayerColors[color])
				else:
					#ない場所にこまを置く
					#x,y = pos
					x0 = x * GridSize + Offset + 4
					y0 = y * GridSize + Offset + 4
					if color != 0:
						square.pieceId = self.canvas.create_oval(x0,y0,x0+PieceSize,y0+PieceSize,
							fill=PlayerColors[color], outline=PlayerColors[color])

		#現在の状態を確認
		player = self.state.getPlayer()
		
		#ゲームオーバーの確認
		if rc.is_game_set(board):
			self.gameOver()
			return
		
		#パス（置けないとき）の処理
		if self.state.checkpass():
			#passのときのテキスト
			passedText = PlayerNames[player] + ' must pass - '
			#プレイヤー交代
			player = self.state.change_turn()
		else:
			#pass出来ないので出力無し
			passedText = ''

		
		self.postStatus(passedText + PlayerNames[self.state.getPlayer()] + "'s Turn")
		self.enabledSpaces = rc.get_puttable_points(self.state.board, self.state.turn)
		self._enableSpaces()

		#print "updateBoard OK"

	def _enableSpaces(self):
		"""置けるマスの表示（Playerのときだけ）"""
		for [x,y] in self.enabledSpaces:
			id = self.squares[x,y].squareId
			#押されたときにselectSpaceを実行
			self.canvas.tag_bind(id, '<ButtonPress>',
				lambda e, s=self, x=x, y=y, : s.selectSpace(x,y))
			#カーソルが重なったときに色をハイライト
			self.canvas.tag_bind(id, '<Enter>',
				lambda e, c=self.canvas, id=id: c.itemconfigure(id, fill=HiliteColor))
			#カーソルが離れたときに色を戻す
			self.canvas.tag_bind(id, '<Leave>',
				lambda e, c=self.canvas, id=id: c.itemconfigure(id, fill=BoardColor))

	def _disableSpaces(self):
		"""置けない場所は処理しないようにする"""
		for [x,y] in self.enabledSpaces:
			if x == -1:
				break
			id = self.squares[x,y].squareId
			self.canvas.tag_unbind(id, '<ButtonPress>')
			self.canvas.tag_unbind(id, '<Enter>')
			self.canvas.tag_unbind(id, '<Leave>')
			self.canvas.itemconfigure(id, fill=BoardColor)
		self.enabledSpaces = ()

	def selectSpace(self,x,y):
		"""置けるマスをクリックしたときに実行"""
		self.state.put_stone(self.state.turn,x,y)
		board = self.state.getPieces()
		turn = self.state.getTrun()
		self.state = rb.ReversiBoard(board,turn)
		self.updateBoard()

	def gameOver(self):
		"""終わったらコマ数を数えて結果出力"""
		count = [0,0] 
		count[0] = rc.get_score(self.state.board,rc.BLACK)
		count[1] = rc.get_score(self.state.board,rc.WHITE)
		self.postStatus('Game Over, %s: %d - %s: %d' \
			%(PlayerNames[1], count[0], PlayerNames[2], count[1]))


		
if __name__ == "__main__":
	strategies = ()
	app = Reversi()
	app.play()