class Tree:
    def __init__(self, node_pairs):
        root_node = Node('COM')
        root_node.set_parent(None)
        root_node.set_depth(0)

        self._tree_dict = {'COM': root_node}

        for node_pair in node_pairs:
            node = Node(node_pair[1])
            node.set_parent(node_pair[0])
            self._tree_dict[node_pair[1]] = node

        for node in self._tree_dict.values():
            self._set_depth(node)

    def _set_depth(self, node):
        if node.get_depth() >= 0:
            return

        parent_node = self._tree_dict[node.get_parent()]

        if parent_node.get_depth() < 0:
            self._set_depth(parent_node)

        node.set_depth(parent_node.get_depth() + 1)

    def get_total_tree_depth(self):
        return sum([node.get_depth() for node in self._tree_dict.values()])

    def get_branch(self, node_name):
        parent_name = self._tree_dict[node_name].get_parent()

        if not parent_name:
            return [node_name]

        branch = self.get_branch(parent_name)
        branch.append(node_name)

        return branch


class Node:
    def __init__(self, name):
        self._name = name
        self._parent = None
        self._depth = float('-inf')

    def set_depth(self, depth):
        self._depth = depth

    def get_depth(self):
        return self._depth

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_name(self):
        return self._name


def main():
    input_file = '../inputs/06.txt'

    with open(input_file, 'r') as fh:
        orbits = [tuple(line.strip().split(')')) for line in fh.readlines()]

    orbit_tree = Tree(orbits)

    part_1 = orbit_tree.get_total_tree_depth()

    print(f"The solution to part 1 is {part_1}.")

    you_branch = orbit_tree.get_branch('YOU')
    san_branch = orbit_tree.get_branch('SAN')

    common_branch = [node[0] for node in
                     zip(you_branch, san_branch)
                     if node[0] == node[1]]

    you_transfers = len(you_branch) - len(common_branch) - 1
    san_transfers = len(san_branch) - len(common_branch) - 1

    part_2 = you_transfers + san_transfers

    print(f"The solution to part 2 is {part_2}.")


if __name__ == '__main__':
    main()
