class create_new_empty_node:
    def __init__(self, user_input):
        self.right = None
        self.left = None
        self.data = user_input


class Solution:
    def add_baby_node_to_one_branch_of_given_node_and_return_the_given_node(self, node, user_input):
        if node == None:
            return create_new_empty_node(user_input)
        else:
            if user_input <= node.data:
                new_baby_node = self.add_baby_node_to_one_branch_of_given_node_and_return_the_given_node(node.left, user_input)
                node.left = new_baby_node
            else:
                new_baby_node = self.add_baby_node_to_one_branch_of_given_node_and_return_the_given_node(node.right, user_input)
                node.right = new_baby_node
            return node

    def level_order(self, full_tree):
        queue = []
        if full_tree == None:
            return
        queue.append(full_tree)

        while(len(queue) != 0):
            node = queue[0]
            print(node.data, end= ' ')
            queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)





if __name__ in '__main__':
    T = int(input())
    my_class = Solution()
    full_tree = None
    for i in range(T):
        user_input = int(input())
        full_tree = my_class.add_baby_node_to_one_branch_of_given_node_and_return_the_given_node(full_tree, user_input)
    my_class.level_order(full_tree)
