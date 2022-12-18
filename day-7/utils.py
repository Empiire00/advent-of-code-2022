from abc import abstractmethod, ABCMeta


class Node(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = None
        self.size = None
        self.parent = None

    @abstractmethod
    def get_size(self):
        raise NotImplementedError("get_size() not implemented")

    def get_children(self):
        return self.children

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def get_name(self):
        return self.name


class DirectoryNode(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name
        self.children = []

    def get_size(self):
        self.size = sum(child.get_size() for child in self.children)
        return self.size


class FileNode(Node):

    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self.size = size
        self.children = None

    def get_size(self):
        return self.size


def read_file(filename):
    with open(filename, 'r') as f:
        out = f.readlines()
        return [line.strip() for line in out]


def get_next_command(lines: list[str], start: int) -> int:
    for i, line in enumerate(lines[start + 1:]):
        if line.startswith('$'):
            return i + start + 1
    # no more commands found
    return len(lines)


def get_command_pairs(lines: list[str]) -> list[(str, list[str])]:
    commands = []
    command_end = 0
    while command_end < len(lines):
        command_start = command_end
        command_end = get_next_command(lines, command_start)
        command = lines[command_start]
        output = lines[command_start + 1:command_end]
        commands.append((command, output))
    return commands


def parse_directory_output_line(output_line: str) -> DirectoryNode:
    name = output_line.split(' ')[-1]
    return DirectoryNode(name)


def parse_file_output_line(output_line: str) -> FileNode:
    size, name = output_line.split(' ')
    return FileNode(name, int(size))


def parse_cd_command(command: str) -> str or False:
    destination = command.split(' ')[-1]
    if destination == '..':
        return False
    return destination


def parse_commands(commands: list[str, list[str]]) -> Node:
    root = DirectoryNode('/')
    current_node = root
    for command, output in commands[1:]:
        if command.startswith('$ ls'):
            children = []
            # create nodes for each file or directory
            for output_line in output:
                if output_line.startswith('d'):
                    # directory
                    children.append(parse_directory_output_line(output_line))
                else:
                    # file
                    # parse file size and name
                    children.append(parse_file_output_line(output_line))
            for child in children:
                current_node.add_child(child)
        elif command.startswith('$ cd'):
            # change directory
            destination = parse_cd_command(command)
            if destination:
                # change to directory
                for child in current_node.get_children():
                    if child.name == destination:
                        current_node = child
                        break
                else:
                    raise ValueError(f'No such directory: {destination}')
            else:
                current_node = current_node.get_parent()
    return root


def visualize_tree(node: Node, indent: int = 0) -> None:
    start = '\t' * indent
    # if file node, print size
    if isinstance(node, FileNode):
        print(f'{start} {node.get_size()} {node.get_name()}')
    elif isinstance(node, DirectoryNode):
        print(f'{start} dir {node.get_name()}')
    if node.children:
        for child in node.children:
            visualize_tree(child, indent + 1)
