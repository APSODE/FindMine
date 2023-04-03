import os
import csv
from Class.CreateMineMap import CreateMineMap
# print(os.path.exists(".\\Class\\MineConfig"))
# print(CreateMineMap.DirTest(".\\Class\\MineConfig"))

# TEST = CreateMineMap(GAME_DIFFICULTY_LEVEL = 1)
# TEST.MineMapAttribute() #지뢰 맵 속성 설정(가로/세로)
# TEST.CreateMap()
# TEST.CreateMineAndHint()
# MINE_MAP = TEST.ReturnMineMap()
# # TEST.CreateMineHint() #
#
#
# # print(TEST.MINE_MAP)
# # print(f"MINE_COUNT = {TEST.CountMine(TEST.MINE_MAP)}")
#
# # MINE_MAP = TEST.WriteHint()
#
# with open("MINE_MAP_1.csv", "w", newline = "") as OPEN_FILE:
#     WRITE_FILE = csv.writer(OPEN_FILE)
#     WRITE_FILE.writerows(MINE_MAP)
#
# # TEST.RemoveSafeCellBlind(USER_INPUT_CELL_POS = [10, 10])
# TEST.RemoveCellCover(USER_INPUT_CELL_LIST = [[10, 10]])
MINE_MAP = [[[True, False], [1, True], [1, True], [True, True], [2, True], [1, True], [2, True], [True, True], [2, True], [True, True], [2, True], [True, True], [2, True], [True, True], [1, True], [1, True]], [[1, True], [1, True], [1, True], [1, True], [2, True], [True, True], [2, True], [1, True], [3, True], [2, True], [3, True], [1, True], [2, True], [1, True], [1, True], [1, True]], [[None, True], [1, True], [1, True], [1, True], [1, True], [2, True], [2, True], [1, True], [1, True], [True, True], [1, True], [None, True], [None, True], [1, True], [1, True], [1, True]], [[None, True], [1, True], [True, True], [1, True], [None, True], [1, True], [True, True], [2, True], [2, True], [3, True], [2, True], [2, True], [1, True], [2, True], [True, True], [1, True]], [[None, True], [2, True], [2, True], [3, True], [1, True], [3, True], [2, True], [3, True], [True, True], [2, True], [True, True], [2, True], [True, True], [3, True], [2, True], [2, True]], [[None, True], [1, True], [True, True], [2, True], [True, True], [2, True], [True, True], [2, True], [2, True], [3, True], [2, True], [2, True], [1, True], [2, True], [True, True], [1, True]], [[1, True], [2, True], [2, True], [3, True], [2, True], [3, True], [2, True], [2, True], [2, True], [True, True], [2, True], [1, True], [2, True], [2, True], [2, True], [1, True]], [[1, True], [True, True], [1, True], [1, True], [True, True], [1, True], [1, True], [True, True], [3, True], [2, True], [3, True], [True, True], [2, True], [True, True], [1, True], [None, True]], [[1, True], [1, True], [1, True], [2, True], [2, True], [2, True], [1, True], [1, True], [2, True], [True, True], [3, True], [2, True], [3, True], [1, True], [1, True], [None, True]], [[None, True], [1, True], [1, True], [2, True], [True, True], [1, True], [None, True], [None, True], [1, True], [1, True], [2, True], [True, True], [1, True], [1, True], [1, True], [1, True]], [[1, True], [2, True], [True, True], [2, True], [1, True], [1, True], [None, True], [1, True], [1, True], [2, True], [2, True], [2, True], [1, True], [1, True], [True, True], [2, True]], [[True, True], [2, True], [1, True], [1, True], [None, True], [1, True], [1, True], [2, True], [True, True], [2, True], [True, True], [1, True], [None, True], [2, True], [2, True], [3, True]], [[2, True], [2, True], [1, True], [None, True], [None, True], [1, True], [True, True], [2, True], [1, True], [3, True], [2, True], [3, True], [1, True], [2, True], [True, True], [2, True]], [[1, True], [True, True], [1, True], [None, True], [1, True], [2, True], [3, True], [2, True], [1, True], [1, True], [True, True], [2, True], [True, True], [3, True], [2, True], [2, True]], [[1, True], [1, True], [1, True], [None, True], [1, True], [True, True], [2, True], [True, True], [1, True], [1, True], [1, True], [2, True], [1, True], [2, True], [True, True], [1, True]], [[None, True], [None, True], [None, True], [None, True], [1, True], [1, True], [2, True], [1, True], [1, True], [None, True], [None, True], [None, True], [None, True], [1, True], [1, True], [1, True]]]
with open("MINE_MAP_2.csv", "w", newline = "") as OPEN_FILE:
    WRITE_FILE = csv.writer(OPEN_FILE)
    WRITE_FILE.writerows(MINE_MAP)

ERROR_COUNT = 0

for CELL_Y in range(MINE_MAP.__len__()):
    for CELL_X in range(MINE_MAP[CELL_Y].__len__()):
        CELL = MINE_MAP[CELL_Y][CELL_X][0]
        CELL_COVER_TF = MINE_MAP[CELL_Y][CELL_X][1]
        if CELL is True and CELL_COVER_TF is False:
            print("오류발견")
            print(f"CELL_Y_POS = {CELL_Y}")
            print(f"CELL_X_POS = {CELL_Y}")
            print(f"CELL_VALUE = {CELL}")
            print(f"CELL_COVER = {CELL_COVER_TF}")
            ERROR_COUNT += 1

if ERROR_COUNT == 0:
    print("오류 없음")

else:
    print("위의 오류 정보 확인하시오")



# MINE_MAP_STR = ""
# for Y in MINE_MAP:
#     MINE_MAP_STR += (str(Y) + "\n")
# print(f"MINE_MAP_STR = {MINE_MAP_STR}")
# for Y in HINT_LOCATION_LIST:
#     HINT_LOCATION_LIST_STR += (str(Y) + "\n")
#
# print(f"HINT_LOCATION_LIST = {HINT_LOCATION_LIST_STR}")
