'''
Created on 2017-07-24 17:53

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 unittest

01. 먼저 unittest 모듈을 import 한 후,

02. "unittest.TestCase"로부터 파생된 사용자 테스트 클래스를 만든다.

03. 테스트 클래스 안에 "test" 로 시작하는 테스트 메서드를 생성한다.
    테스드 메서드에서는 일반적으로 테스트하고자 하는 함수나 메서드를 호출하고
    그 결과값을 self.assert*() 메서드를 사용하여 확인한다
    (assertEqual, assertTrue, assertFalse, assertRaises, assertRegex
        등 다양한 assert 메서들을 사용할 수 있다).

04. 테스트 클래스가 완성되었으면, unittest.main()을 호출하여 테스트를 실행시킨다.

"""

import unittest
import unitOperation


# class Mytest(unittest.TestCase):
#     def test_add(self):
#         u = unitOperation.add(20, 10)
#         self.assertEqual(u, 30)
#
#     def test_minus(self):
#         u = unitOperation.minus(20, 10)
#         self.assertEqual(u, 10)
#
#
# if __name__ == '__main__':
#     unittest.main()


import unittest
import os
import unitFile

class Mytest2(unittest.TestCase):
    testfile = "text.txt"

    # Fixture
    def setUp(self):
        f = open(Mytest2.testfile, "w")
        f.write("1234567890")
        f.close()

    def tearDown(self):
        try:
            os.remove(Mytest2.testfile)
        except:
            pass

    def test_filelen(self):
        leng = unitFile.filelen(Mytest2.testfile)
        self.assertEqual(leng, 10)

    def test_countinfile(self):
        cnt = unitFile.countinfile(Mytest2.testfile, "0")
        self.assertEqual(cnt, 1)

if __name__ == '__main__':
    unittest.main()

# Mytest2 라는 유닛 테스트 클래스는
# test_filelen(), test_countinfile() 두 개의 테스트 메서드를 가지고 있다.
# 이들 각각의 테스트 메서드가 실행되기 전에 항상 setUp() 메서드가 실행되어 테스트 파일을 생성하고,
# 테스트 실행후 tearDown() 메서드가 실행하여 사용한 테스트 파일을 지우게 된다.