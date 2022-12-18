from utils import *


def main():
    inp = read_file('input.txt')
    commands = get_command_pairs(inp)
    root_node = parse_commands(commands)
    # update directory sizes
    root_node.get_size()

    directories = []
    node = root_node
    queue = [node]
    while queue:
        node = queue.pop(0)
        if isinstance(node, DirectoryNode):
            directories.append(node)
            queue.extend(node.get_children())

    free_space = 70000000 - root_node.get_size()
    space_to_free = 30000000 - free_space

    possible_deletion_candidates = [d for d in directories if d.get_size() >= space_to_free]
    possible_deletion_candidates.sort(key=lambda d: d.get_size())

    print(f'The update requires freeing up {space_to_free}')
    print(f'Freeing up {possible_deletion_candidates[0].get_name()} will free up {possible_deletion_candidates[0].get_size()}')
    visualize_tree(root_node)


if __name__ == '__main__':
    main()
