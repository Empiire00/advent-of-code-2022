from utils import *


def main():
    inp = read_file('input.txt')
    commands = get_command_pairs(inp)
    root_node = parse_commands(commands)
    # update directory sizes
    root_node.get_size()
    # recursively go through the tree and get all directories using bfs
    directories = []
    node = root_node
    queue = [node]
    while queue:
        node = queue.pop(0)
        if isinstance(node, DirectoryNode):
            directories.append(node)
            queue.extend(node.get_children())

    sum_of_dir_sizes = sum([di.get_size() for di in directories if di.get_size() < 100000])
    print(f'Total size of directories smaller than 100000: {sum_of_dir_sizes}')
    visualize_tree(root_node)


if __name__ == '__main__':
    main()
