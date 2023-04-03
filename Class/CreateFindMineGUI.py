import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QGridLayout, QLineEdit, QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton
from tkinter import *
from CreateMineMap import CreateMineMap



class INTERNAL_FUNC:
    @staticmethod
    def ReturnMaxLength(MAP):
        MINE_MAP = MAP
        MAX_Y_LENGTH = MINE_MAP.__len__()
        MAX_X_LENGTH = MINE_MAP[0].__len__()

        return [MAX_Y_LENGTH, MAX_X_LENGTH]

    @staticmethod
    def ReturnCellData(CURRENT_CELL):
        """
        :param CURRENT_CELL:
        :return: CURRENT_CELL_DATA = {"TYPE" : "MINE" / "WARN" / "SAFE", "COVER" : bool}
        """

        CURRENT_CELL_VALUE = CURRENT_CELL[0]
        CURRENT_CELL_COVER_TF = CURRENT_CELL[1]

        if type(CURRENT_CELL_VALUE) == int and CURRENT_CELL_VALUE >= 1:
            CURRENT_CELL_VALUE_TYPE = "WARN"

        elif CURRENT_CELL_VALUE is True:
            CURRENT_CELL_VALUE_TYPE = "MINE"

        else:
            CURRENT_CELL_VALUE_TYPE = "SAFE"

        CURRENT_CELL_DATA = {
            "TYPE": CURRENT_CELL_VALUE_TYPE,
            "COVER": CURRENT_CELL_COVER_TF
        }

        return CURRENT_CELL_DATA


class FindMineGUI_OLD(QWidget):
    def __init__(self, TITLE_NAME, FIND_MINE, WINDOW_SIZE = [500, 500], WINDOW_POS = "CENTER", DEBUG = False):
        self.TITLE = str(TITLE_NAME)
        self.WINDOW_SIZE = WINDOW_SIZE
        self.WINDOW_POS = WINDOW_POS
        self.FIND_MINE = FIND_MINE
        self.MINE_MAP = self.FIND_MINE.ReturnMineMap()
        self.DEBUG = DEBUG
        self.LAYOUT = None

        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.TITLE)
        self.resize(self.WINDOW_SIZE[0], self.WINDOW_SIZE[1])
        self.SetWindowPos(WINDOW_POS = self.WINDOW_POS)
        # self.setLayout(self.LAYOUT if self.LAYOUT is not None else self.ReturnLayout() )
        self.SetLayout()
        self.show()


    def SetLayout(self):
        MAIN_LAYOUT = QVBoxLayout()
        INTERNAL_LAYOUT = QHBoxLayout()
        MINE_MAP_LAYOUT = QGridLayout()
        for CELL_Y in range(self.MINE_MAP.__len__()):
            for CELL_X in range(self.MINE_MAP[CELL_Y].__len__()):
                CELL_POS = [CELL_Y, CELL_X]
                MINE_MAP_BUTTON_WIDGET = self.CreateButton(POS = CELL_POS)
                MINE_MAP_LAYOUT.addWidget(MINE_MAP_BUTTON_WIDGET, CELL_Y, CELL_X)
        MAIN_LAYOUT.addLayout(MINE_MAP_LAYOUT)
        # return MAIN_LAYOUT
        self.setLayout(MAIN_LAYOUT)



    def CreateButton(self, POS):
        MINE_MAP_BUTTON_WIDGET = QPushButton(self)
        if self.DEBUG:
            CELL = self.MINE_MAP[POS[0]][POS[1]][0]
            CELL_COVER_TF = self.MINE_MAP[POS[0]][POS[1]][1]
            MINE_MAP_BUTTON_WIDGET.setText(f"{CELL},{CELL_COVER_TF}")
        MINE_MAP_BUTTON_WIDGET.setCheckable(True)
        MINE_MAP_BUTTON_WIDGET.setEnabled(self.MINE_MAP[POS[0]][POS[1]][1])
        MINE_MAP_BUTTON_WIDGET.clicked.connect(partial(self.ButtonEventHandler, POS))

        return MINE_MAP_BUTTON_WIDGET

    def ButtonEventHandler(self, POS):
        if self.DEBUG:
            CELL = self.MINE_MAP[POS[0]][POS[1]]
            print(f"========디버깅========\nCELL_POS : X={POS[1]} Y={POS[0]}\nCELL_VALUE : {CELL[0]}\nCELL_COVER_TF : {CELL[1]}\n")
        self.FIND_MINE.RemoveCellCover(USER_INPUT_CELL_LIST = [POS])
        self.MINE_MAP = self.FIND_MINE.MINE_MAP
        self.SetLayout()

    def EditClickedButton(self, DATA, DEBUG = False):

        POS = DATA[0]
        BUTTON = DATA[1]
        # print(f"BEFORE CHANGE = {self.MINE_MAP[POS[0]][POS[1]][1]}")
        self.MINE_MAP[POS[0]][POS[1]][1] = False
        # print(f"AFTER CHANGE = {self.MINE_MAP[POS[0]][POS[1]][1]}")
        BUTTON.setEnabled(False)


        if DEBUG:
            CELL = self.MINE_MAP[POS[0]][POS[1]]
            print(f"========디버깅========\nCELL_POS : X={POS[1]} Y={POS[0]}\nCELL_VALUE : {CELL[0]}\nCELL_COVER_TF : {CELL[1]}\n")






    def SetWindowPos(self, WINDOW_POS):
        if str(WINDOW_POS).upper() == "CENTER":
            QR = self.frameGeometry()
            CURRENT_WINDOW_CENTER_POS = QDesktopWidget().availableGeometry().center()
            QR.moveCenter(CURRENT_WINDOW_CENTER_POS)
            self.move(QR.topLeft())


class FindMineGUI:
    def __init__(self, MASTER, FIND_MINE = None, DEBUG = False):
        self.MASTER = MASTER
        self.FIND_MINE = self.TestMine(DEBUG = DEBUG) if (DEBUG is True) and (FIND_MINE is None) else FIND_MINE 
        self.MINE_MAP = self.FIND_MINE.MINE_MAP
        self.FRAME_LIST = []
        # self.BUTTON_TYPE_LIST = ["SAFE", "WARN", "MINE"]

    @staticmethod
    def TestMine(DEBUG):
        TEST_MINE = CreateMineMap(GAME_DIFFICULTY_LEVEL = 1, DEBUG = DEBUG)
        TEST_MINE.MineMapAttribute()
        TEST_MINE.CreateMap()
        TEST_MINE.CreateMineAndHint()
        return TEST_MINE

    def ButtonClickEvnetHandler(self, BUTTON_POS):
        CELL = self.MINE_MAP[BUTTON_POS[0]][BUTTON_POS[1]]

        BUTTON_DATA = INTERNAL_FUNC.ReturnCellData(CURRENT_CELL = CELL)
        BUTTON_TYPE = BUTTON_DATA["TYPE"]
        BUTTON_COVER = BUTTON_DATA["COVER"]

        if BUTTON_COVER is True: #BUTTON_COVER가 True일 경우에만 이벤트 처리 진행
            if BUTTON_TYPE == "SAFE":
                RT = self.FIND_MINE.RemoveCellCover(USER_INPUT_CELL_LIST = [BUTTON_POS])
                print(RT)

    def CreateMineMap_Frame(self):
        for _ in range(3):
            FRAME = Frame(self.MASTER)
            FRAME.pack()
            self.FRAME_LIST.append(FRAME)

        LENGTH_LIST = INTERNAL_FUNC.ReturnMaxLength(self.MINE_MAP)
        MAX_Y_LENGTH = LENGTH_LIST[0]
        MAX_X_LENGTH = LENGTH_LIST[1]

        for Y_NUM in range(MAX_Y_LENGTH):
            for X_NUM in range(MAX_X_LENGTH):
                CELL = self.MINE_MAP[Y_NUM][X_NUM]

                CELL_VALUE = CELL[0]
                CELL_COVER_TF = CELL[1]

                if CELL_COVER_TF is True:
                    MINE_BUTTON = Button(self.FRAME_LIST[0], text = f"   ")
                    MINE_BUTTON.grid(row = Y_NUM, column = X_NUM)

    def CreateMineMap_Canvas(self):
        pass

    

if __name__ == "__main__":
    MASTER_UI = Tk()
    FindMine_GUI = FindMineGUI(MASTER = MASTER_UI, DEBUG = True)
    # FindMine_GUI.CreateFrame()
    FindMine_GUI.CreateMineMap_Frame()
    MASTER_UI.mainloop()


