# -*- coding: utf-8 -*-

import threading
import time
import Queue

"""
线程池包含以下模块
1，包含一个任务队列与结果队列，使用python现在的Queue
2，包含一个状态控制对象
3，包含一个线程池管理对象
"""


class threadPoolState:
    """
    线程池状态控制对象，用于线程池管理来控制线程
    """

    def __init__(self):
        # 保存线程池中可以允许的最大的线程数量
        self.__maxThreadSize = 10
        # 当前运行的线程数量
        self.__currentThreadCount = 0
        # 线程池控制状态，表示期望线程池转变的状态
        # 值可以是(0：运行，1：暂停，2：停止，3：终止)
        # 状态<2>表示需要停止线程池工作，但允许有一定的延迟，即允许线程完成当前正在工作的任务后结束
        # 状态<3>表示紧急停止线程池工作，线程在收到此状态时应该立即停止工作并结束线程
        self.__expectThreadPoolState = 0
        # 当前线程池处于的工作状态
        # 值可以是(0：运行，1：暂停，2：结束)
        # 注意：使用2或3状态来停止线程池时，线程池的工作都是2
        self.__currentThreadPoolState = 2
        # 线程计数锁
        self.__countMutex = threading.Lock()
        # 线程状态锁
        self.__stateMutex = threading.Lock()

    def setMaxThreadSize(self, size):
        """
        设置线程池的最大线程数量
        成功:True,失败:False
        """
        if not isinstance(size, (int, long)):
            return False
        self.__maxThreadSize = size
        return True

    def getMaxThreadSize(self):
        """
        获取线程池最大允许的线程数量
        """
        return self.__maxThreadSize

    def getRunThreadSize(self):
        """
        获取当前正在工作的线程数量
        """
        return self.__currentThreadCount

    def addThreadCount(self):
        """
        增加一个线程数量计数，表示新创建了一个线程
        """
        self.__countMutex.acquire()
        self.__currentThreadCount += 1
        self.__countMutex.release()
        return True

    def subThreadCount(self):
        """
        减少一个线程数量计数，表示有一个线程退出
        """
        self.__countMutex.acquire()
        self.__currentThreadCount -= 1
        self.__countMutex.release()
        return True

    def getThreadPoolAction(self):
        """
        获取线程池期望下一步改变的状态，也可以认为是线程池的下一步动作
        """
        return self.__expectThreadPoolState

    def getThreadPoolState(self):
        """
        获取线程池当前工作的状态
        """
        return self.__currentThreadPoolState

    def setThreadPoolAction(self, action):
        """
        设置线程池的状态，用于控制线程池的工作
        """
        if not isinstance(action, (int, long)):
            return False
        if action < 0 or action > 3:
            return False
        self.__stateMutex.acquire()
        self.__expectThreadPoolState = action
        self.__stateMutex.release()
        return True

    def amendThreadPoolState(self, state):
        """
        修正当前线程的工作状态，只能用于线程池管理对象，禁止工作线程修改此标志
        """
        if not isinstance(state, (int, long)):
            return False
        if state < 0 or state > 3:
            return False
        self.__currentThreadPoolState = state
        return True


class tState:
    """
    此对象专用于传递到工作线程中，用于控制工作线程的工作
    """

    def __init__(self, state):
        # 保存线程池状态管理对象
        self.__threadPoolState = None
        if isinstance(state, threadPoolState):
            self.__threadPoolState = state

    def getAction(self):
        """
        获取线程下一步需要操作的状态
        """
        if not self.__threadPoolState:
            return False
        return self.__threadPoolState.getThreadPoolAction()

    def getMaxThreadSize(self):
        """
        获取最大允许的线程数量
        """
        if not self.__threadPoolState:
            return False
        return self.__threadPoolState.getMaxThreadSize()

    def getRunThreadSize(self):
        """
        获取当前正在工作的线程数量
        """
        if not self.__threadPoolState:
            return False
        return self.__threadPoolState.getRunThreadSize()

    def release(self):
        """
        在工作线程结束时需要调用此函数来释放线程并减少线程计数
        """
        if not self.__threadPoolState:
            return False
        return self.__threadPoolState.subThreadCount()


class workThread(threading.Thread):
    """
    工作线程，用于做具体工作
    """

    def __init__(self, data):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        # data格式是{"taskQueue":obj , "resultQueue":obj , "runState":obj , "workCall":call}
        # 包含一个任务队列，结果队列，状态控制对象，工作回调函数地址
        self.__data = data
        self.start()

    def run(self):
        runState = self.__data["runState"]
        workCall = self.__data["workCall"]
        while True:
            # 首先检查状态
            state = runState.getAction()
            if state == 1:
                # 暂停
                time.sleep(0.3)
                continue
            elif state == 2 or state == 3:
                # 停止
                break

            # 当当前运行的线程数量超过最大数量时就结束线程
            if runState.getRunThreadSize() > runState.getMaxThreadSize():
                break

            # 不存在回调或任务为空就不执行
            if not workCall or self.__data["taskQueue"].empty():
                time.sleep(0.3)
                continue
            # 获取一个任务
            try:
                tempTask = self.__data["taskQueue"].get(False)
            except:
                time.sleep(0.3)
                continue
            # 调用回调来执行任务，如果返回False表示任务运行失败，此时结果将不会保存到结果队列中
            try:
                tempR = workCall(self.__data["runState"], tempTask)
            except Exception, e:
                print "threadPool workError:(%s)has been ignored" % e
                time.sleep(0.3)
                continue
            if not tempR:
                time.sleep(0.3)
                continue
            # 如果任务执行成功就将结果保存到结果队列中
            self.__data["resultQueue"].put(tempR)
        # 当线程结束时
        runState.release()


class threadPoolManage:
    """
    线程池管理对象
    """

    def __init__(self, workCall=None):
        """

        :rtype: object
        """
        self.__taskQueue = Queue.Queue()
        self.__resultQueue = Queue.Queue()
        self.__threadPoolState = threadPoolState()
        # 线程池工作回调函数
        # 回调函数的格式必须是call(runStateObj , task)
        # 如果任务运行出错call函数必须返回False，如果任务运行成功就直接返回任务数据
        self.__workCall = workCall
        self.__stateServer = None

    def setWorkCall(self, workCall):
        self.__workCall = workCall
        return True

    def clear(self):
        """
        清空队列
        """
        if self.__threadPoolState.getThreadPoolState() != 2:
            # 工作中不能清空队列
            return False
        self.__taskQueue.queue.clear()
        self.__resultQueue.queue.clear()
        return True

    def start(self):
        """
        启动线程池，如果已经启动将不能再启动
        """
        if self.__threadPoolState.getThreadPoolState() != 2:
            # 不能重复启动
            return False
        # 在启动前先还原状态
        self.__threadPoolState.setThreadPoolAction(0)
        # 启动状态监视线程
        self.__stateServer = threading.Thread(target=self.__threadPoolStateControlServer, args=())
        self.__stateServer.setDaemon(True)
        self.__stateServer.start()
        # 判断线程池是否启动成功
        startIndex = 0
        while startIndex < 15:
            if self.__threadPoolState.getThreadPoolState() == 2:
                startIndex += 1
                time.sleep(0.3)
            else:
                break
        if startIndex >= 15:
            # 如果启动失败
            self.__threadPoolState.setThreadPoolAction(3)
            return False
        return True

    def __threadPoolStateControlServer(self):
        """
        线程池状态控制服务，用于监视线程池的状态，与控制线程池的数量与结束
        """
        while True:
            # 首先检查状态
            state = self.__threadPoolState.getThreadPoolAction()
            if state == 1:
                # 暂停
                self.__threadPoolState.amendThreadPoolState(1)
                time.sleep(0.3)
                continue
            elif state == 2 or state == 3:
                # 等待线程全部结束
                if self.__threadPoolState.getRunThreadSize() != 0:
                    time.sleep(0.3)
                    continue
                else:
                    self.__threadPoolState.amendThreadPoolState(2)
                    break
            # 运行状态
            self.__threadPoolState.amendThreadPoolState(0)
            # 创建线程
            if self.__threadPoolState.getRunThreadSize() < self.__threadPoolState.getMaxThreadSize():
                workThread({"taskQueue": self.__taskQueue, "resultQueue": self.__resultQueue,
                            "runState": tState(self.__threadPoolState), "workCall": self.__workCall})
                self.__threadPoolState.addThreadCount()
                continue
            # 正常运行时
            time.sleep(0.3)

    def setMaxThreadSize(self, size):
        """
        设置最大线程数量
        """
        return self.__threadPoolState.setMaxThreadSize(size)

    def getMaxThreadSize(self):
        """
        获取允许的最大线程数量
        """
        return self.__threadPoolState.getMaxThreadSize()

    def getWorkThreadSize(self):
        """
        获取当前工作中的线程数量
        """
        return self.__threadPoolState.getRunThreadSize()

    def getThreadPoolRunState(self):
        """
        获取线程池当前运行的状态(0：运行，1，暂停，2，结束)
        """
        return self.__threadPoolState.getThreadPoolState()

    def run(self):
        """
        将线程池的工作设置为运行状态，成功返回True，失败返回False
        """
        if self.__threadPoolState.getThreadPoolState() == 2:
            return False
        return self.__threadPoolState.setThreadPoolAction(0)

    def pause(self):
        """
        将线程池的工作设置为暂停状态，成功返回True，失败返回False
        """
        if self.__threadPoolState.getThreadPoolState() == 2:
            return False
        return self.__threadPoolState.setThreadPoolAction(1)

    def stop(self):
        """
        将线程池的工作设置为停止状态，成功返回True，失败返回False
        """
        if self.__threadPoolState.getThreadPoolState() == 2:
            return False
        return self.__threadPoolState.setThreadPoolAction(2)

    def urgentStop(self):
        """
        将线程池的工作设置为紧急停止状态，成功返回True，失败返回False
        """
        if self.__threadPoolState.getThreadPoolState() == 2:
            return False
        return self.__threadPoolState.setThreadPoolAction(3)

    def addTask(self, task):
        """
        向任务队列增加一个任务
        """
        self.__taskQueue.put(task)
        return True

    def getResult(self):
        """
        向结果队列中获取一个结果，如果队列为空或获取失败将返回False
        """
        if self.__resultQueue.empty():
            return False
        try:
            r = self.__resultQueue.get(False)
        except:
            return False
        return r

    def getTaskSize(self):
        """
        获取任务队列中的任务数量
        """
        return self.__taskQueue.qsize()

    def getResultSize(self):
        """
        获取结果队列中的结果数量
        """
        return self.__resultQueue.qsize()