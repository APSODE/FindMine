import random
import sys
from Class.JSON_RW_TOOL.RW_JSON import READ_WRITE

sys.setrecursionlimit(1000000)

class INTERNAL_FUNC:
    @staticmethod
    def CompareTypeAndValue(VAR_1, VAR_2):
        return True if VAR_1 == VAR_2 and type(VAR_1) == type(VAR_2) else False

class CreateMineMap:
    """
    CreateMineMap = Multi-Dimensional List
    """
    def __init__(self, GAME_DIFFICULTY_LEVEL, DEBUG = False):
        self.DEBUG = DEBUG
        self.GAME_DIFFICULTY_LEVEL = GAME_DIFFICULTY_LEVEL if GAME_DIFFICULTY_LEVEL <= 3 else 3
        self.MINE_MAP_ATTRIBUTE = None
        self.MINE_MAP = list()
        self.MINE_HINT_MAP = None
        self.CONFIG_DIR = ".\\Class\\MineConfig\\MineConfig.json"
        self.MINE_CELL_LIST = []
        self.HINT_CELL_LIST = []
        self.SAFE_CELL_LIST = []

    def MineMapAttribute(self, RT = False):
        GAME_DIFFICULTY_LEVEL = self.GAME_DIFFICULTY_LEVEL

        if GAME_DIFFICULTY_LEVEL == 0:
            self.MINE_MAP_ATTRIBUTE = [8, 8] #[가로, 세로]
        elif GAME_DIFFICULTY_LEVEL == 1:
            self.MINE_MAP_ATTRIBUTE = [16, 16]
        elif GAME_DIFFICULTY_LEVEL == 2:
            self.MINE_MAP_ATTRIBUTE = [30, 16]
        elif GAME_DIFFICULTY_LEVEL == 3:
            self.MINE_MAP_ATTRIBUTE = [30, 24]

        if RT:
            return self.MINE_MAP_ATTRIBUTE
        else:
            pass

    def CreateMap(self):
        MINE_MAP_X_LENGTH = self.MINE_MAP_ATTRIBUTE[0]
        MINE_MAP_Y_LENGTH = self.MINE_MAP_ATTRIBUTE[1]
        MINE_MAP = self.MINE_MAP

        for MINE_MAP_CELL_Y_NUM in range(MINE_MAP_X_LENGTH):
            MINE_MAP.append(list())
            for MINE_MAP_CELL_X_NUM in range(MINE_MAP_Y_LENGTH):
                MINE_MAP[MINE_MAP_CELL_Y_NUM].append([None, True])

    def CreateMineAndHint(self):
        MINE_MAP = self.MINE_MAP
        CONFIG_DATA = READ_WRITE.READ_JSON(FILE_DIR = self.CONFIG_DIR if self.DEBUG is False else ".\\MineConfig\\MineConfig.json")
        MINE_COUNT_LIMIT = CONFIG_DATA["MineCount"][f"{self.GAME_DIFFICULTY_LEVEL}"]
        MINE_COUNT = 0
        LOOP_TF = True

        MAX_Y_LENGTH = len(MINE_MAP) - 1
        MAX_X_LENGTH = len(MINE_MAP[0]) - 1
        while LOOP_TF:
            # print(MINE_COUNT < MINE_COUNT_LIMIT)
            for Y_NUM in range(MAX_Y_LENGTH):
                for X_NUM in range(MAX_X_LENGTH):
                    CELL = MINE_MAP[Y_NUM][X_NUM][0]
                    if CELL is None and MINE_COUNT < MINE_COUNT_LIMIT:
                        if random.randint(1, 10) <= 1:
                            self.MINE_MAP[Y_NUM][X_NUM][0] = True
                            self.MINE_CELL_LIST.append([Y_NUM, X_NUM])
                            MINE_COUNT += 1
                            INDEX_MODIFY_OPERATOR = [[-1, -1], [-1, 0], [-1, 1],
                                                      [0, -1], [0, 1],
                                                      [1, -1], [1, 0], [1, 1]]
                            for OPERATOR in INDEX_MODIFY_OPERATOR:
                                HINT_LOCATION_Y = Y_NUM + OPERATOR[0]
                                HINT_LOCATION_X = X_NUM + OPERATOR[1]

                                # 힌트가 표시될 셀은 행렬 속에 위치해 있고 각 셀의 인덱스 번호가 최대 크기를 넘거나 0보다 작은 경우는 힌트를 추가 하지 않는다.
                                if (True if 0 <= HINT_LOCATION_Y <= MAX_Y_LENGTH else False) and (True if 0 <= HINT_LOCATION_X <= MAX_X_LENGTH else False):
                                    HINT_CELL = MINE_MAP[HINT_LOCATION_Y][HINT_LOCATION_X][0]
                                    # 힌트가 표시될 셀은 None일 경우 1로 변경한다. 그리고 힌트셀 위치에 지뢰가 위치하여 있을 경우 그 값은 True인데 True는 파이썬에서 1과 동일 취급하므로 is not을 사용하여 필터링을 겨쳐야한다.
                                    if HINT_CELL is None:
                                        self.MINE_MAP[HINT_LOCATION_Y][HINT_LOCATION_X][0] = 1
                                        self.HINT_CELL_LIST.append([HINT_LOCATION_Y, HINT_LOCATION_X])

                                    elif HINT_CELL is not None:
                                        if self.DEBUG:
                                            print(f"==========HINT_CELL==========\nHINT_CELL_VALUE = {HINT_CELL}\nMINE_CELL_POS = [Y = {Y_NUM}, X = {X_NUM}]\nHINT_CELL_POS = [HINT_CELL_Y = {HINT_LOCATION_Y}, HINT_CELL_X = {HINT_LOCATION_X}]")


                                        if HINT_CELL is not True and HINT_CELL >= 1:
                                            self.MINE_MAP[HINT_LOCATION_Y][HINT_LOCATION_X][0] += 1
                                            self.HINT_CELL_LIST.append([HINT_LOCATION_Y, HINT_LOCATION_X])

                                        elif HINT_CELL is True:
                                            pass

                                else:
                                    pass
                        else:
                            self.SAFE_CELL_LIST.append([Y_NUM, X_NUM])

                    else:
                        pass

            if MINE_COUNT >= MINE_COUNT_LIMIT:
                LOOP_TF = False
        # return self.MINE_MAP

    def RemoveSafeCellBlind(self, USER_INPUT_CELL_POS, USER_PREVIOUS_CELL_POS = None):
        """
        :param USER_INPUT_CELL_POS:\nUSER_INPUT_CELL ==> [Y, X]
        :return:
        """
        MINE_MAP = self.MINE_MAP

        MAX_Y_LENGTH = len(MINE_MAP) - 1
        MAX_X_LENGTH = len(MINE_MAP[0]) - 1

        USER_INPUT_CELL_Y = USER_INPUT_CELL_POS[0]
        USER_INPUT_CELL_X = USER_INPUT_CELL_POS[1]

        AROUND_CELL_LIST = []

        INDEX_MODIFY_OPERATOR = [[-1, -1], [-1, 0], [-1, 1],
                                 [0, -1], [0, 1],
                                 [1, -1], [1, 0], [1, 1]]

        USER_INPUT_CELL = MINE_MAP[USER_INPUT_CELL_Y][USER_INPUT_CELL_X][0]
        if USER_INPUT_CELL is None:
            for OPERATOR in INDEX_MODIFY_OPERATOR:
                AROUND_CELL_Y = USER_INPUT_CELL_Y + OPERATOR[0]
                AROUND_CELL_X = USER_INPUT_CELL_X + OPERATOR[1]

                if True if 0 <= AROUND_CELL_Y <= MAX_Y_LENGTH else False and True if 0 <= AROUND_CELL_X <= MAX_X_LENGTH else False:
                    # AROUND_CELL = [AROUND_CELL_Y, AROUND_CELL_X]
                    AROUND_CELL = MINE_MAP[AROUND_CELL_Y][AROUND_CELL_X][0]

                    if AROUND_CELL is None:
                        self.MINE_MAP[AROUND_CELL_Y][AROUND_CELL_X][1] = False
                        AROUND_CELL_LIST.append([AROUND_CELL_Y, AROUND_CELL_X])

                    elif AROUND_CELL is not None and AROUND_CELL is not True and type(AROUND_CELL) == int:
                        self.MINE_MAP[AROUND_CELL_Y][AROUND_CELL_X][1] = False

                    elif AROUND_CELL is True:
                        self.MINE_MAP[AROUND_CELL_Y][AROUND_CELL_X][1] = False
                        print("GAME OVER")

        #유저가 입력한 칸이 힌트 칸의 조건에 부합 한다면 재귀 호출은 진행하지 않아야한다.
        elif USER_INPUT_CELL is not True and type(USER_INPUT_CELL) == int:
            self.MINE_MAP[USER_INPUT_CELL_Y][USER_INPUT_CELL_X][1] = False

        if USER_INPUT_CELL_POS in AROUND_CELL_LIST:
            AROUND_CELL_LIST.remove(USER_INPUT_CELL_POS)
        else:
            pass


        # 위에서 검증된 셀들이 포함된 리스트에 원소가 존재하지 않는다면 재귀호출 중지
        if len(AROUND_CELL_LIST) == 0:
            pass

        else:
            for CELL_POS in AROUND_CELL_LIST:
                print("함수 재귀 호출 성공")
                self.RemoveSafeCellBlind(USER_INPUT_CELL_POS = CELL_POS, USER_PREVIOUS_CELL_POS = USER_INPUT_CELL_POS)

    def RemoveCellCover(self, USER_INPUT_CELL_LIST):
        MINE_MAP = self.MINE_MAP
        # MAX_Y_LENGTH = MINE_MAP.__len__() - 1
        # MAX_X_LENGTH = MINE_MAP[0].__len__() - 1
        INDEX_MODIFY_OPERATOR = [[-1, -1], [-1, 0], [-1, 1],
                                 [0, -1], [0, 1],
                                 [1, -1], [1, 0], [1, 1]]
        AROUND_CELL_LIST = []
        for USER_INPUT_CELL in USER_INPUT_CELL_LIST:
            INPUT_CELL_COVER_TF = MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][1] is True
            if INPUT_CELL_COVER_TF is True:
                if MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][0] is None:
                    CELL_VERIFICATION = self.CellAddressVerify(INPUT_CELL_POS = USER_INPUT_CELL)
                    if self.DEBUG is True:
                        print(f"CELL_VERIFICATION = {CELL_VERIFICATION}")

                    if CELL_VERIFICATION:
                        AROUND_CELL = MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][0]
                        AROUND_CELL_COVER_TF = MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][1]

                        if self.DEBUG is True:
                            print("조건식 1 작동")

                        if AROUND_CELL is None and AROUND_CELL_COVER_TF is True:
                            if self.DEBUG is True:
                                print("조건식 1-1 작동")

                            self.MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][1] = False
                            for OPERATOR in INDEX_MODIFY_OPERATOR:
                                MODIFIED_AROUND_CELL_POS = [USER_INPUT_CELL[0] + OPERATOR[0], USER_INPUT_CELL[1] + OPERATOR[1]]
                                if self.CellAddressVerify(INPUT_CELL_POS = MODIFIED_AROUND_CELL_POS):
                                    AROUND_CELL_LIST.append(MODIFIED_AROUND_CELL_POS)

                        elif (type(AROUND_CELL) == int and AROUND_CELL > 0) and AROUND_CELL_COVER_TF is True:
                            if self.DEBUG is True:
                                print("조건식 1-2 작동")
                            self.MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][1] = False



                elif type(MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][0]) == int and MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][0] > 0:
                    if self.DEBUG is True:
                        print(f"조건식 2 작동 (힌트칸) ==> CELL_POS = {USER_INPUT_CELL[0], USER_INPUT_CELL[1]}, CELL_VALUE = {MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][0]}")
                    self.MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][1] = False
                    # return True

                elif MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][0] is True:
                    if self.DEBUG is True:
                        print("조건식 3 작동 (지뢰칸)")
                    self.MINE_MAP[USER_INPUT_CELL[0]][USER_INPUT_CELL[1]][1] = False
                # return False

            elif INPUT_CELL_COVER_TF is False:
                if self.DEBUG is True:
                    print("조건식 4 작동")

        if AROUND_CELL_LIST.__len__() == 0:
            return True

        elif AROUND_CELL_LIST.__len__() > 0:
            if self.DEBUG is True:
                print(f"AROUND_CELL_LIST = {AROUND_CELL_LIST}")
            self.RemoveCellCover(USER_INPUT_CELL_LIST = AROUND_CELL_LIST)

    def CellAddressVerify(self, INPUT_CELL_POS):
        MINE_MAP = self.MINE_MAP
        MAX_Y_LENGTH = MINE_MAP.__len__() - 1
        MAX_X_LENGTH = MINE_MAP[0].__len__() - 1

        return True if 0 <= INPUT_CELL_POS[0] <= MAX_Y_LENGTH and 0 <= INPUT_CELL_POS[1] <= MAX_X_LENGTH else False

    def RefreshMineMap(self, MINE_MAP):
        self.MINE_MAP = MINE_MAP

    def ReturnMineMap(self):
        return self.MINE_MAP

    @staticmethod
    def ReturnMaxLength(MAP):
        MINE_MAP = MAP
        MAX_Y_LENGTH = MINE_MAP.__len__()
        MAX_X_LENGTH = MINE_MAP[0].__len__()

        return [MAX_Y_LENGTH, MAX_X_LENGTH]




    #==========================================필요 없음==========================================#

    def CreateMineHint(self):
        MINE_MAP = self.MINE_MAP

        MAX_Y_LENGTH = len(MINE_MAP) - 1
        MAX_X_LENGTH = len(MINE_MAP[0]) - 1

        MINE_LIST = []
        HINT_LOCATION = []
        for Y_NUM in range(len(MINE_MAP)):
            for X_NUM in range(len(MINE_MAP[Y_NUM])):
                CELL = MINE_MAP[Y_NUM][X_NUM]
                if CELL:
                    MINE_LIST.append([Y_NUM, X_NUM])
                else:
                    pass

        for MINE_LOCATION in MINE_LIST:
            CELL_PER_MINE_LOCATION = []
            INDEX_CORRECT_Y = 1 if 0 < MINE_LOCATION[0] < MAX_Y_LENGTH else 0
            INDEX_CORRECT_X = 1 if 0 < MINE_LOCATION[1] < MAX_X_LENGTH else 0

            INDEX_CORRECT_OPERATOR = [[-1, -1], [-1, 0], [-1, 1],
                                      [0, -1], [0, 1],
                                      [1, -1], [1, 0], [1, 1]]
            for CALCULATION in INDEX_CORRECT_OPERATOR:
                CELL_LOCATION = [
                    MINE_LOCATION[0] + (CALCULATION[0] * INDEX_CORRECT_Y),
                    MINE_LOCATION[1] + (CALCULATION[1] * INDEX_CORRECT_X)
                ]
                if CELL_LOCATION not in CELL_PER_MINE_LOCATION:
                    CELL_PER_MINE_LOCATION.append(CELL_LOCATION)
                else:
                    pass


            HINT_LOCATION += CELL_PER_MINE_LOCATION
        self.MINE_HINT_MAP = HINT_LOCATION

    def WriteHint(self):
        HINT_MAP = self.MINE_HINT_MAP
        for HINT_LOCATION in HINT_MAP:
            MINE_MAP = self.MINE_MAP
            if MINE_MAP[HINT_LOCATION[0]][HINT_LOCATION[1]] is None and MINE_MAP[HINT_LOCATION[0]][HINT_LOCATION[1]] is not True:
                self.MINE_MAP[HINT_LOCATION[0]][HINT_LOCATION[1]] = 1
            elif MINE_MAP[HINT_LOCATION[0]][HINT_LOCATION[1]] >= 1 and MINE_MAP[HINT_LOCATION[0]][HINT_LOCATION[1]] is not True:
                self.MINE_MAP[HINT_LOCATION[0]][HINT_LOCATION[1]] += 1
            else:
                pass
        return self.MINE_MAP

    # ==========================================필요 없음==========================================#


    @staticmethod
    def CountMine(MINE_MAP):
        COUNT = 0
        for Y_NUM in range(len(MINE_MAP)):
            for X_NUM in range(len(MINE_MAP[Y_NUM])):
                CELL = MINE_MAP[Y_NUM][X_NUM]
                if CELL is True:
                    COUNT += 1
        # print(f"COUNT = {COUNT}")
        return COUNT



if __name__ == "__main__":
    pass

