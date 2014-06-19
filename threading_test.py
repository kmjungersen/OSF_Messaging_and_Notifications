from twisted.internet import reactor, threads
import time

def aSillyBlockingMethodOne(x):
    time.sleep(2)
    print x

def aSillyBlockingMethodTwo(x):
    print x
    print time.time() - t

# run both methods sequentially in a thread
commands = [(aSillyBlockingMethodOne, ["Calling First"], {})]
commands.append((aSillyBlockingMethodTwo, ["And the second"], {}))
threads.callMultipleInThread(commands)

t = time.time()

reactor.run()
