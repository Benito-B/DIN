from tkinter import *
from tkinter import ttk


def setbind(w: Tk, pulsed: str, x: int) -> None:
    w.bind(pulsed, lambda e: fsm.chState(str(x)))
    w.bind(x, lambda e: fsm.chState(str(x)))


#FRAMEWORK
window = Tk()
window.rowconfigure(0, weight=1, minsize=20)
window.rowconfigure(1, weight=5)
window.columnconfigure(0, weight=1)
window.bind('<Key>', lambda e: print(e.keysym))
for i in range(10):
    k = '<KP_' + str(i) + '>'
    setbind(window, k, i)
window.bind('<BackSpace>', lambda e: fsm.chState('C'))
window.bind('<Return>', lambda e: fsm.chState("="))
window.bind('<KP_Enter>', lambda e: fsm.chState("="))
window.bind('<KP_Add>', lambda e: fsm.chState('+'))
window.bind('<KP_Subtract>', lambda e: fsm.chState('-'))
window.bind('<KP_Multiply>', lambda e: fsm.chState('*'))
window.bind('<KP_Divide>', lambda e: fsm.chState('/'))
window.bind('<KP_Decimal>', lambda e: fsm.chState("."))
window.bind('<period>', lambda e: fsm.chState("."))

# MODEL
screen = StringVar()

# VIEW
def buildButton(frame, key, r, c):
    s = ttk.Style()
    s.configure('custom.TButton', font=('verdana', 11), padx=10, pady=1, width=2, height=2)
    ttk.Button(frame, text=key, style='custom.TButton', command=lambda: fsm.chState(key))\
        .grid(row=r, column=c, sticky="nswe")


s = ttk.Style()
s.configure('custom.TLabel', font=('verdana', 12))
label = ttk.Label(window, textvariable=screen, style='custom.TLabel')
label.grid(row=0, column=0, sticky="nswe")
frame = ttk.Frame(window)
frame.grid(row=1, column=0, sticky="nswe")
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
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

    def __clear(self):
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