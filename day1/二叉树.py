class Node:  # 节点
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:  # 二叉树
    def __init__(self):
        self.root = None
        self.help_queue = []

    def level_build_tree(self, node: Node):
        """
        按层次构建二叉树
        :param node:
        :return:
        """
        if not self.root:  # 如果树为空，则直接插入根节点
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if not self.help_queue[0].lchild:  # 如果左子树为空，则插入左子树
                self.help_queue[0].lchild = node
            else:
                self.help_queue[0].rchild = node  # 插入右子树
                del self.help_queue[0]  # 当前父亲满了，出队

    def pre_order(self, curr_node: Node):
        """
        先序遍历
        :param curr_node:
        :return:
        """
        if curr_node:
            print(curr_node.elem, end=' ')
            self.pre_order(curr_node.lchild)
            self.pre_order(curr_node.rchild)

    def in_order(self, curr_node: Node):
        """
        中序遍历
        :param curr_node:
        :return:
        """
        if curr_node:
            self.in_order(curr_node.lchild)
            print(curr_node.elem, end=' ')
            self.in_order(curr_node.rchild)

    def post_order(self, curr_node: Node):
        """
        后序遍历
        :param curr_node:
        :return:
        """
        if curr_node:
            self.post_order(curr_node.lchild)
            self.post_order(curr_node.rchild)
            print(curr_node.elem, end=' ')

    def level_order(self, curr_node: Node):
        """
        层次遍历
        :param curr_node:
        :return:
        """
        help_queue = []
        help_queue.append(self.root)  # 根节点入队
        while help_queue:
            out_node = help_queue.pop(0)
            print(out_node.elem, end=' ')  # 打印出队节点
            if out_node.lchild:
                help_queue.append(out_node.lchild)
            if out_node.rchild:
                help_queue.append(out_node.rchild)


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        new_node = Node(i)  # 创建节点
        tree.level_build_tree(new_node)  # 插入节点

    print("先序遍历：", end='')
    tree.pre_order(tree.root)  # 先序遍历
    print("\n中序遍历：", end='')
    tree.in_order(tree.root)  # 中序遍历
    print("\n后序遍历：", end='')
    tree.post_order(tree.root)  # 后序遍历
    print("\n层次遍历：", end='')
    tree.level_order(tree.root)  # 层次遍历
