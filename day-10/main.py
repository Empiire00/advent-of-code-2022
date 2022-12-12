# import cpu global
from cpu import *


def readFromFile(filename: str) -> list:
    with open(filename) as f:
        content = f.readlines()
        # map removes \n
        return list(map(lambda s: s.strip(), content))


def parseInstruction(rawInstruction: str, registers: list[Register]) -> CPUInstruction:
    parts = rawInstruction.split(" ")
    # switch case words[0]
    match parts[0].upper():
        case "ADDX":
            return AddInstruction(registers, parts[1])
        case "NOOP":
            return NoOperationInstruction(registers, [])


def main():
    register1 = Register(1)
    registerList = [register1]
    cpu = CPU(registers=registerList)
    fileContent = readFromFile("input.txt")
    instructions: list[CPUInstruction] = [parseInstruction(line, registerList)
                                          for line in fileContent]
    # add instructions to cpu
    cpu.addInstructions(instructions)

    # step and get register values at steps 20, 60, 100, 140, 180, 220
    sum = 0
    for i in range(222):
        if cpu.counter + 1 in [20, 60, 100, 140, 180, 220]:
            signalStrength = cpu.getRegisters()[0].get() * (cpu.counter + 1)
            sum += signalStrength
            print(f"Step {cpu.counter}: {cpu.getRegisters()[0].get()}")
        cpu.step()
        # print(f"Step {cpu.counter}: {cpu.getRegisters()[0].get()}")

    print(f"Sum: {sum}")


if __name__ == '__main__':
    main()
