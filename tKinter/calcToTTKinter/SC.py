from tkinter import *
from tkinter import ttk
#FRAMEWORK
window = Tk()

# MODEL
screen = StringVar()

# VIEW
def buildButton(frame, key, r, c):
    buttonOptions = {'font': ('verdana', 12)}
    buttonOptions['padx'] = 10
    buttonOptions['pady'] = 1
    buttonOptions['width'] =1
    buttonOptions['height'] = 2
    buttonOptions['text'] = key
    buttonOptions['command'] = lambda: fsm.chState(key)
    Button(frame, buttonOptions ).grid(row=r, column=c)

label = Label(window, textvariable=screen)
label.pack()
frame = Frame(window)
frame.pack()
for r in range(3):
    for c in range(1, 4):
        key = str(r * 3 + c)
        buildButton(frame, key, 3 - r - 1, c - 1)
buildButton(frame, '0', 3, 0)
buildButton(frame, '.', 3, 1)
buildButton(frame, '=', 3, 2)
buildButton(frame, '/', 0, 3)
buildButton(frame, '*', 1, 3)
buildButton(frame, '-', 2, 3)
buildButton(frame, '+', 3, 3)
buildButton(frame, 'Ms', 0, 4)
buildButton(frame, 'Mr', 1, 4)
buildButton(frame, 'Mc', 2, 4)
buildButton(frame, 'C', 3, 4)

# CONTROLLER
class FSM():
    fsmGraph = list()
    # State 0
    fsmGraph.append({'0-9':{'s':0, 't':lambda s: FSM.__addSymbol(s)},
                     '.':{'s':1, 't':lambda s: FSM.__addDot(s)},
                     'C':{'s':0, 't':lambda s: FSM.__clear(s)},
                     '=':{'s':0, 't':lambda s: FSM.__calc(s)},
                     'Ms':{'s':0, 't':lambda s: FSM.__memoryW(s)},
                     'Mr':{'s':2, 't':lambda s: FSM.__memoryR(s)},
                     'Mc':{'s':0, 't':lambda s: FSM.__memoryC(s)},
                     'ops': {'s': 0, 't': lambda s: FSM.__setOp(s)}})
    # State 1
    fsmGraph.append({'0-9':{'s':1, 't':lambda s: FSM.__addSymbol(s)},
                     '.': {'s':1, 't':lambda s: None},
                     'C':{'s':0, 't':lambda s: FSM.__clear(s)},
                     '=': {'s': 0, 't':lambda s: FSM.__calc(s)},
                     'Ms':{'s':1, 't':lambda s: FSM.__memoryW(s)},
                     'Mr':{'s':2, 't':lambda s: FSM.__memoryR(s)},
                     'Mc':{'s':1, 't':lambda s: FSM.__memoryC(s)},
                     'ops': {'s': 0, 't': lambda s: FSM.__setOp(s)}})
    # State 2
    fsmGraph.append({'0-9':{'s':0, 't':lambda s: FSM.__addSymbol(s)},
                     '.':{'s':1, 't':lambda s: FSM.__addSymbol(s)},
                     'C':{'s':0, 't':lambda s: FSM.__clear(s)},
                     '=':{'s':0, 't':lambda s: FSM.__calc(s)},
                     'Ms':{'s':0, 't':lambda s: FSM.__memoryW(s)},
                     'Mr':{'s':2, 't':lambda s: FSM.__memoryR(s)},
                     'Mc':{'s':0, 't':lambda s: FSM.__memoryC(s)},
                     'ops': {'s': 0, 't': lambda s: FSM.__setOp(s)}})

    def __init__(self, screen:StringVar)->None:
        self.currState = 0
        self.keyPressed = None
        self.memory = None
        self.op1 = '0'
        self.op2 = None
        self.op = None
        self.myScreen = screen
        self.myScreen.set('0')
        self.clearScreen = False
        FSM.__debug(self)

    def __debug(self):
        print('####################################')
        print('State:',self.currState)
        print('key pressed:', self.keyPressed)
        print('op1:', self.op1)
        print('op2:', self.op2)
        print('op:', self.op)
        print('clear screen:', self.clearScreen)
        print('memory:', self.memory)

    def chState(self, key:str):
        self.keyPressed = key
        if key in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            key = '0-9'
        elif key in {'/', '*', '+', '-'}:
            key = 'ops'
        task = FSM.fsmGraph[self.currState][key]['t']
        if FSM.fsmGraph[self.currState][key]['s'] >= 0:
            self.currState = FSM.fsmGraph[self.currState][key]['s']
        else:
            pass
        task(self)
        # FSM.__debug(self)

    def __addSymbol(self):
        if self.clearScreen:
            self.myScreen.set(0)
            self.clearScreen = False
        if self.myScreen.get() == '0':
            self.myScreen.set(self.keyPressed)
            return
        self.myScreen.set(self.myScreen.get() + self.keyPressed)

    def __addDot(self):
        if self.clearScreen:
            FSM.__clear(self, self.myScreen)
        if self.myScreen.get() == '0':
            self.myScreen.set('0.')
            return
        self.myScreen.set(self.myScreen.get() + self.keyPressed)

    def __clear(self, screen: StringVar):
        self.currState = 0
        self.keyPressed = None
        self.memory = None
        self.op1 = '0'
        self.op2 = None
        self.op = None
        self.myScreen.set('0')
        self.clearScreen = False

    def __memoryW(self):
        self.memory = self.myScreen.get()
        self.clearScreen = True

    def __memoryR(self):
        if self.memory != None:
            self.myScreen.set(self.memory)
            self.clearScreen = True

    def __memoryC(self):
        self.memory = None

    def __setOp(self):
        self.op1 = self.myScreen.get()
        self.op = self.keyPressed
        self.clearScreen = True

    def __calc(self):
        if self.op != None:
            self.op2 = self.myScreen.get()
            if ('.' in self.op1) or ('.' in self.op2):
                op1 = float(self.op1)
                op2 = float(self.op2)
            else:
                op1 = int(self.op1)
                op2 = int(self.op2)
            if self.op == '/':
                if op2 != 0:
                    self.op2 = str(op1 / op2)
                else:
                    self.op2 = "Division by zero"
            if self.op == '*':
                self.op2 = str(op1 * op2)
            if self.op == '+':
                self.op2 = str(op1 + op2)
            if self.op == '-':
                self.op2 = str(op1 - op2)
            self.myScreen.set(self.op2)
            self.clearScreen = True
fsm = FSM(screen)

#FRAMEWORK
window.mainloop()