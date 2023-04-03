from Class.CreateMineMap import CreateMineMap
from Class.CreateFindMineGUI import FindMineGUI
from PyQt5.QtWidgets import QApplication
import sys

FIND_MINE = CreateMineMap(GAME_DIFFICULTY_LEVEL = 1)
MINE_MAP_ATTRIBUTION = FIND_MINE.MineMapAttribute(RT = True)
FIND_MINE.CreateMap()
FIND_MINE.CreateMineAndHint()


APP = QApplication(sys.argv)
EX = FindMineGUI(TITLE_NAME = "FindMine-1.0", FIND_MINE = FIND_MINE, DEBUG = True)#MINE_MAP = FIND_MINE.ReturnMineMap())
sys.exit(APP.exec_())#GUI 유지 및 유저 인풋 반을을 위한 이벤트 루프 생성 코드


#지뢰 부분 UI까지 구현 완료
#지뢰 부분 UI의 레이아웃을 갱신할 방법을 찾아야함
#추가++++
#현재 셀의 X좌표의 마지막 인덱스에서 +1을 할경우 처음 인덱스의 값을 가져와 연산을 진행하는 오류 발생


