# import abstract base class
import abc


class Operation(object, metaclass=abc.ABCMeta):
    def __init__(self, registers, args) -> None:
        self.registers = registers
        self.args = args

    @abc.abstractmethod
    def execute(self) -> any:
        raise NotImplementedError(
            "Subclass must implement abstract method execute()")


class Register:
    def __init__(self, value=0) -> None:
        self.value = value

    def get(self) -> int:
        return self.value

    def set(self, value) -> None:
        self.value = value


class CPUInstruction(object, metaclass=abc.ABCMeta):

    def __init__(self, registers: list[Register], args) -> None:
        self.registers = registers
        self.args = args
        self.operations: list[Operation] = []

    def step(self):
        if len(self.operations) > 0:
            operation = self.operations.pop(0)
            operation.execute()
        else:
            print("No operations left")

    def isFinished(self) -> bool:
        return len(self.operations) == 0

    def getDescription(self) -> str:
        return f"{self.__class__.__name__} {self.args}"


class CPU:
    def __init__(self, registers: list[Register]) -> None:
        self.registers = registers
        self.instructions: list[CPUInstruction] = []
        self.counter = 0
        self.instructionCounter = 0

    #
    def step(self):
        if len(self.instructions) > 0:
            instruction = self.instructions[0]
            instruction.step()
            self.counter += 1
            if (instruction.isFinished()):
                self.instructions.pop(0)
                self.instructionCounter += 1
                # print(
                #     f"Instruction {self.instructionCounter} finished after Step {self.counter}: {instruction.getDescription()}")
                # self.step()

        else:
            print("No instructions left")

    def getRegisters(self) -> list[Register]:
        return self.registers

    def addInstruction(self, instr: CPUInstruction):
        self.instructions.append(instr)

    def addInstructions(self, instr: list[CPUInstruction]):
        self.instructions.extend(instr)

    def stepAll(self):
        while len(self.instructions) > 0:
            self.step()


class NoOperation(Operation):
    def execute(self):
        pass


class AddOperation(Operation):
    def execute(self):
        numberToAdd = int(self.args[0])
        curRegister = self.registers[0]
        curRegister.set(curRegister.get() + numberToAdd)


class AddInstruction(CPUInstruction):
    def __init__(self, registers, args) -> None:
        super().__init__(registers, args)
        self.operations.append(NoOperation(None, []))
        self.operations.append(AddOperation(self.registers, [self.args]))


class NoOperationInstruction(CPUInstruction):
    def __init__(self, registers, args) -> None:
        super().__init__(registers, args)
        self.operations.append(NoOperation(None, []))
