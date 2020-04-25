class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, root):
        q1 = []
        q2 = []
        res = ""
        q1.append(root)

        while True:
            while len(q1) != 0:
                tmp = q1.pop(0)
                if tmp is None:
                    res += "null,"
                else:
                    res += str(tmp.val) + ","
                    q2.append(tmp.left)
                    q2.append(tmp.right)
            if len(q2) == 0:
                break
            q1 = q2[:]
            q2 = []
        return res

    def deserialize(self, data):
        data_list = data[0:-1].split(',')   # [0:-1] eliminates the last ','

        mp1 = []
        mp2 = []
        head = None

        if data_list[0] != "null":
            mp1.append(Node(int(data_list[0])))
            head = mp1[0]
            i = 1
            while i < len(data_list):
                for node in mp1:
                    if node is not None:
                        if data_list[i] != "null":
                            node.left = Node(int(data_list[i]))
                        i += 1
                        mp2.append(node.left)

                        if data_list[i] != "null":
                            node.right = Node(int(data_list[i]))
                        i += 1
                        mp2.append(node.right)

                mp1 = mp2[:]
                mp2 = []

        return head
