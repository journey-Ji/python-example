#5-3studying package

#way to play module 1
import game.sound.echo
game.sound.echo.echo_test()

#way to play module 2
from game.sound import echo
echo.echo_test()

#way to play module 3
from game.sound.echo import echo_test
echo_test()
print('\n')
#not valuable way
'''
import game
game.sound.echo.echo_test()
'''
#위의 예제는 오류가 난다. import game을 수행하면 game 디렉터리의 모듈 또는 __init__.py에 정의한 것만 참조 가능

#not valuable way 2
'''
import game.sound.echo.echo_test
'''
#import에서 마지막부분인 echo_test는 함수이기 때문에 오류가 난다.
#import의 마지막 부분은 항상 모듈 또는 패키지여야 한다

#__init__.py의 용도 : 해당 디렉터리가 패키지의 일부임을 알려주는 역할
print('__init__.py의 용도') 
'''
from game.sound import *
echo.echo_test()
'''
#위 예제는 오류가 발생한다. *을 사용하여 import할 때에는, __init__.py파일에 __all__변수를 설정하고 
# import할 수 있는 모듈을 정의해주어야 하기 때문이다.
#우리는 아직 정의해주지 않아서 오류가 났다.

from game.sound import*
echo.echo_test()
print('\n')

#나 혼자 코딩 : *을 사용하여 render.py파일 안의 render_test함수를 사용해 보시오.
'''
from game.graphic import *
render.render_test()
print('\n')
'''

#relative 패키지
#render 모듈 내에서 echo모듈의 사용
print('render 모듈 내에서 echo모듈의 사용')
from game.graphic.render import render_test
render_test()
print('\n')




