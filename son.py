import threading
import os
def foo():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())

def skill_q():
    print('skill q!')

def skill_w():
    print('skill w!')

def skill_e():
    print('skill e!')

def skill_r():
    print('skill r!')

# if __name__ == '__main__':
#     print('process id', os.getpid())
#     thread1 = threading.Thread(target=foo).start()
#     thread2 = threading.Thread(target=foo).start()
#     thread3 = threading.Thread(target=foo).start()
# 세 개의 스레드는 모두 각기 다른 스레드지만, 모두 도일한 프로세스를 공유하고 있다.

if __name__ == '__main__':
    thread1 = threading.Thread(target=skill_q()).start()
    thread2 = threading.Thread(target=skill_w()).start()
    thread3 = threading.Thread(target=skill_e()).start()
    thread4 = threading.Thread(target=skill_r()).start()