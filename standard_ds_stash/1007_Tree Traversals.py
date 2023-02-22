import time


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class BinaryTree:
    # for now, we can directly set the root to an already created tree
    # insertion and deletion can be done on BSTs and not here on BTs
    def __init__(self, root):
        self.root = root

    def inorder_recursive(self):
        print('Inorder is: ', end='')
        self.inorder_recursive_helper(self.root)
        print()

    def inorder_recursive_helper(self, node):
        if node is not None:
            self.inorder_recursive_helper(node.left)
            print(node.val, end=', ')
            self.inorder_recursive_helper(node.right)

    def inorder_iterative(self):
        stack = [[self.root, False]]

        while stack:
            if not stack[-1][1]:
                if stack[-1][0].left is not None:
                    stack.append([stack[-1][0].left, False])
                else:
                    stack[-1][1] = True
            else:
                node = stack[-1][0]
                print(node.val, end=', ')
                stack.pop()
                if stack:
                    stack[-1][1] = True
                if node.right is not None:
                    stack.append([node.right, False])

        print()

    # Without extra stack space
    def inorder_iterative_better(self):
        curr = self.root
        stack = []

        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            print(curr.val, end=', ')
            curr = curr.right


if __name__ == '__main__':
    root_node = TreeNode(10, TreeNode(7, TreeNode(6), TreeNode(8)), TreeNode(12, TreeNode(11), TreeNode(13)))

    BinaryTree(root_node).inorder_iterative_better()
