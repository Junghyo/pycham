'''
Created on 2017-07-21 17:09

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 package
 
 module : *.py
 package : module의 집합
 
 일반적으로 new package를 생성하면  __init__.py 존재
 (3.3 ver 이후부터는 init파일이 없어도 package 인식 가능)
"""

"""
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
"""
# 1. echo 모듈을 import하여 실행하는 방법
import game.sound.echo
game.sound.echo.echo_test()

# 2. echo 모듈이 있는 디렉터리까지를 from ... import하여 실행하는 방법
from game.sound import echo
echo.echo_test()

# 3. echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법
from game.sound.echo import echo_test
echo_test()

# relative package
# graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을
# 사용하고 싶다면 어떻게 해야 할까?
# render.py
# from game.sound.echo import echo_test
from game.graphic.render import render_test
render_test()

# .. – 부모 디렉터리
# . – 현재 디렉터리