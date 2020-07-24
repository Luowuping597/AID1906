"""
    linklist.py
    功能：实现单链表的构建和功能操作
    重点代码
"""


# 创建节点类
class Node:
    """
        思路：将自定义的类视为节点的生成类，实例对象中
            包含数据部分和指向下一个切点的next
    """

    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 循环下一个节点关系

# 链表操作
class LinkList:
    """
        单链表
        思路：单链表类，生成对象可以进行增删改查操作
            具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
            初始化链表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        p = self.head  # p 作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        """
            遍历链表
        """
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next  # p向后移动

    # 判断链表为空
    def is_empty(self):
        """
         判断链表为空
        :return: 空-->True
        """
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        """
            清空链表
        """
        self.head.next = None

    # 尾部插入节点
    def append(self, val):
        """
            尾部插入节点(链表这样插入效率不高)
        :param val:要插入的数据
        """
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_insert(self, val):
        """
            头部插入 （效率高）
        :param val:  要插入的数据
        """
        node = Node(val)  # 生成节点
        node.next = self.head.next  # 新节点连接下一个节点
        self.head.next = node  # 插入节点

    # 指定插入位置
    def insert(self, index, val):
        """
            指定插入位置
        :param index: 要插入的位置
        :param val: 要插入的数据
        """
        p = self.head
        for i in range(index):
            if p.next is None:  # 超出已有链表的最大范围
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点
    def remove(self, val):
        """
            删除节点
        :param val: 指定数据
        """
        p = self.head
        # 结束循环必然两个条件其1为假
        # while p.next is not None and p.next.val != val:
        while p.next and p.next.val != val:
            p = p.next

        if p.next is None:
            raise ValueError("delete(val) val not in linklist")
        else:
            p.next = p.next.next

    # 获取某个节点值
    def get_index(self, index):
        if index < 0:
            raise IndexError("list index out range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("list index out range")
            p = p.next
        return p.val





if __name__ == "__main__":
    l1 = LinkList()
    l1.init_list([1, 3, 5, 7, 9])
    l2 = LinkList()
    l2.init_list([2, 4, 6, 8, 10])
    # l.append(100)
    # l.head_insert(1000)
    # l.insert(100, 5)
    # l.remove(11111)
    # print(l1.get_index(2))
    l1.show()
    print("="*20)
    l2.show()
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            copy = p.next
            p.next = q
            p = p.next

            q = copy
    p.next = q

    l1.show()



