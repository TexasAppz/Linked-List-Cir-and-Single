# Course: CS261 - Data Structures
# Student Name: Jaime Garcia
# Assignment: Assigment 3
# Description: Your Very Own Linked List
# Description2: Circular Doubly Linked List


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """

        # cur = DLNode(value)
        # cur.next = self.sentinel.next
        # self.sentinel.next = cur

        cur = DLNode(value) # initialize a new link
        #new_link.data = data # set new_link data

        # if the list is empty we set both next and prev on the sentinel
        if self.sentinel.prev == self.sentinel:
            cur.prev = self.sentinel
            cur.next = self.sentinel.next
            self.sentinel.prev = cur
            self.sentinel.next = cur

        # if the list isn't empty we just set next on the sentinel
        else:
            cur.prev = self.sentinel
            cur.next = self.sentinel.next
            self.sentinel.next.prev = cur
            self.sentinel.next = cur

        return


    def add_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """

        cur = DLNode(value)
        #new_link.value = value

        if self.sentinel.prev == self.sentinel:
            cur.prev = self.sentinel
            cur.next = self.sentinel.next
            self.sentinel.prev = cur
            self.sentinel.next = cur


        else:
            cur.prev = self.sentinel.prev
            cur.next = self.sentinel
            self.sentinel.prev.next = cur
            self.sentinel.prev = cur

        return


    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0:
            raise CDLLException

        # iterate through list in search of node to insert new node after
        cur = self.sentinel
        count = 0
        while count != index:
            cur = cur.next
            count += 1
            if cur == self.sentinel:
                raise CDLLException

        # initialize new node and set next/prev properties
        new_node = DLNode(value)
        new_node.next = cur.next
        new_node.prev = cur

        # connect existing list to new_node
        cur.next = new_node
        new_node.next.prev = new_node


    def remove_front(self) -> None:
        """
        TODO: Write this implementation
        """

        if self.sentinel.next == self.sentinel:
            raise CDLLException()

        # remove node immediately following sentinel
        self.sentinel.next.next.prev = self.sentinel
        self.sentinel.next = self.sentinel.next.next


    def remove_back(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.sentinel.prev == self.sentinel:
            raise  CDLLException()

        if self.sentinel.prev == self.sentinel:
            return False

        else:
            self.sentinel.prev.prev.next = self.sentinel
            self.sentinel.prev = self.sentinel.prev.prev

        if self.sentinel.prev.prev.next  == None:
            raise CDLLException()

        return True


    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0:
            raise CDLLException

        if self.sentinel.prev == self.sentinel:
                raise CDLLException

        current = self.sentinel
        count = 0
        while count != index:
            current = current.next
            count += 1
            if current.next == self.sentinel:
                raise CDLLException

        current.next.next.prev = current
        current.next = current.next.next

    def get_front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException()

        if self.sentinel.next == self.sentinel:
            raise CDLLException()

        cur = self.sentinel.next

        return cur.value

    def get_back(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        cur = self.sentinel.prev
        return cur.value

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """

        if self.sentinel.next == self.sentinel:
            return False

        # iterate through list in search of node to remove
        node_to_remove = self.sentinel.next
        index = 0
        while node_to_remove.value != value and node_to_remove != self.sentinel:
            node_to_remove = node_to_remove.next
            index += 1

        # handle case where value was not found in node properties
        if node_to_remove == self.sentinel:
            return False

        # handle case where value was found node_to_remove needs removed
        self.remove_at_index(index)
        return True


        cur = cur.next
        return False


    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        count = 0
        current = self.sentinel
        while current.next != self.sentinel:
            current = current.next
            if current.value == value:
                count += 1
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException

        # handle case where index1 is out of range
        if index1 < 0 or index1 > self.length() - 1:
            raise CDLLException

        # handle case where index2 is out of range
        if index2 < 0 or index2 > self.length() - 1:
            raise CDLLException

        # handle case where index1 == index2
        if index1 == index2:
            return

        # iterate through list in search of nodes to swap
        node_1 = self.sentinel.next
        node_1_index = 0
        node_2 = self.sentinel.next
        node_2_index = 0
        node_1_found = False
        node_2_found = False
        while not (node_1_found and node_2_found):
        # search for node_1
            if not node_1_found and node_1_index != index1:
                node_1 = node_1.next
                node_1_index += 1
            if not node_1_found and node_1_index == index1:
                node_1_found = True
            # search for node_2
            if not node_2_found and node_2_index != index2:
                node_2 = node_2.next
                node_2_index += 1
            if not node_2_found and node_2_index == index2:
                node_2_found = True

        # handle case where node_1.next == node_2
        if node_1.next == node_2:
        # link node_1 and node_2 to remainder of CircularList
            node_1.next = node_2.next
            node_2.prev = node_1.prev
            # link between node_1 and node_2
            node_2.next = node_1
            node_1.prev = node_2
            # link remainder of CircularList to node_1 and node_2
            node_2.prev.next = node_2
            node_1.next.prev = node_1

        # handle case where node_2.next == node_1
        elif node_2.next == node_1:
        # link node_1 and node_2 to remainder of CircularList
            node_2.next = node_1.next
            node_1.prev = node_2.prev
            # link between node_1 and node_2
            node_1.next = node_2
            node_2.prev = node_1
            # link remainder of CircularList to node_1 and node_2
            node_1.prev.next = node_1
            node_2.next.prev = node_2

        # handle case where node_1 and node_2 are not adjacent
        else:
        # remove node_1 from CircularList and point both pointers to its previous
            node_1.prev.next = node_1.next
            node_1.next.prev = node_1.prev
            node_1.next = node_1.prev

            # remove node_2 from CircularList and point both pointers to its previous
            node_2.prev.next = node_2.next
            node_2.next.prev = node_2.prev
            node_2.next = node_2.prev

            # swap prev pointers for both nodes
            node_1.prev = node_2.prev
            node_2.prev = node_1.next

            # swap next pointers for both nodes
            node_1.next = node_1.prev
            node_2.next = node_2.prev

            # re-insert node_1 into the list where node_2 used to live
            node_1.next = node_1.next.next
            node_1.next.prev = node_1
            node_1.prev.next = node_1

            # re-insert node_2 into the list where node_1 used to live
            node_2.next = node_2.next.next
            node_2.next.prev = node_2
            node_2.prev.next = node_2



    def reverse(self) -> None:
        """
        TODO: Write this implementation
        """
        node_1 = self.sentinel.next
        node_2 = self.sentinel.prev
        index_1 = 0
        index_2 = self.length() - 1

        while index_1 < index_2:
            new_node_1 = node_1.next
            new_node_2 = node_2.prev

            if node_1.next == node_2:
                node_1.next = node_2.next
                node_2.prev = node_1.prev
        # link between node_1 and node_2
                node_2.next = node_1
                node_1.prev = node_2
                # link remainder of CircularList to node_1 and node_2
                node_2.prev.next = node_2
                node_1.next.prev = node_1

        # handle case where node_2.next == node_1
            elif node_2.next == node_1:
        # link node_1 and node_2 to remainder of CircularList
                node_2.next = node_1.next
                node_1.prev = node_2.prev
                # link between node_1 and node_2
                node_1.next = node_2
                node_2.prev = node_1
                # link remainder of CircularList to node_1 and node_2
                node_1.prev.next = node_1
                node_2.next.prev = node_2

        # handle case where node_1 and node_2 are not adjacent
            else:
        # remove node_1 from CircularList and point both pointers to its previous
                node_1.prev.next = node_1.next
                node_1.next.prev = node_1.prev
                node_1.next = node_1.prev

                # remove node_2 from CircularList and point both pointers to its previous
                node_2.prev.next = node_2.next
                node_2.next.prev = node_2.prev
                node_2.next = node_2.prev

                # swap prev pointers for both nodes
                node_1.prev = node_2.prev
                node_2.prev = node_1.next

                # swap next pointers for both nodes
                node_1.next = node_1.prev
                node_2.next = node_2.prev

                # re-insert node_1 into the list where node_2 used to live
                node_1.next = node_1.next.next
                node_1.next.prev = node_1
                node_1.prev.next = node_1

                # re-insert node_2 into the list where node_1 used to live
                node_2.next = node_2.next.next
                node_2.next.prev = node_2
                node_2.prev.next = node_2

            # iterate to next set of nodes to swap and update indices
            node_1 = new_node_1
            node_2 = new_node_2
            index_1 += 1
            index_2 -= 1

    def sort(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.length() < 2:
            return

        # utilize bubble sort in sorting the CircularList
        outer_loop = self.length() - 1
        while outer_loop > 0:
            inner_loop = 0
            current = self.sentinel.next
            following = current.next
            while inner_loop < outer_loop:
            # handle case where next.value < current.value
                if following.value < current.value:
                # swap nodes
                    current.next = following.next
                    following.prev = current.prev
                    following.next = current
                    current.prev = following
                    current.next.prev = current
                    following.prev.next = following
                    # update variables for next iteration
                    following = current.next
                    inner_loop += 1
                    # handle case where next.value >= current.value
                else:
                    current = following
                    following = current.next
                    inner_loop += 1

            # update outer_loop variable for next iteration
            outer_loop -= 1


    # def left_rotate(self,N):
    #
    #     current = self.sentinel
    #     count = 1
    #
    #     while count < N and current != None :   # reach Nth node
    #         current = current.next
    #         count = count + 1
    #     NthNode = current
    #
    #     while current.next != None:      # reach last node
    #         current = current.next
    #     current.next = self.sentinel      # make last node point to sentinel node
    #     self.sentinel.prev = current
    #
    #     self.sentinel = NthNode.next      # make Nth node as sentinel node
    #
    #     self.sentinel.prev = NthNode    # make circular again
    #     NthNode.next = self.sentinel

    def rotate(self, steps: int) -> None:
        """
        TODO: Write this implementation
        """
        # len = self.length()
        # if len == 0 or steps == 0:
        #     return
        # if steps < 0:
        #     steps = - steps
        #
        # else:
        #     steps = len - steps
        #
        # steps = steps % len
        # if(steps == 0):
        #     return
        #
        # self.sentinel.prev.next =  None
        # self.sentinel.prev = None
        # self.left_rotate(steps)


    def remove_duplicates(self) -> None:
        """
        TODO: Write this implementation
        """

        if self.sentinel == None:   # if list is empty
            return

        cur = self.sentinel

        while (cur.next != self.sentinel) :
            if (cur.value == cur.next.value):
                cur.next = cur.next.next
                #self.remove(value)
            else:
                cur = cur.next

    def odd_even(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_front('A')
    # lst.add_front('B')
    # lst.add_front('C')
    # print(lst)
    #
    # print('\n# add_back example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_back('C')
    # lst.add_back('B')
    # lst.add_back('A')
    # print(lst)
    #
    # print('\n# insert_at_index example 1')
    # lst = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # #
    # print('\n# remove_front example 1')
    # lst = CircularList([1, 2])
    # print(lst)
    # for i in range(3):
    #     try:
    #         lst.remove_front()
    #         print('Successful removal', lst)
    #     except Exception as e:
    #         print(type(e))
    # #
    # print('\n# remove_back example 1')
    # lst = CircularList()
    # try:
    #     lst.remove_back()
    # except Exception as e:
    #     print(type(e))
    # lst.add_front('Z')
    # lst.remove_back()
    # print(lst)
    # lst.add_front('Y')
    # lst.add_back('Z')
    # lst.add_front('X')
    # print(lst)
    # lst.remove_back()
    # print(lst)
    #
    # print('\n# remove_at_index example 1')
    # lst = CircularList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)
    # #
    # print('\n# get_front example 1')
    # lst = CircularList(['A', 'B'])
    # print(lst.get_front())
    # print(lst.get_front())
    # lst.remove_front()
    # print(lst.get_front())
    # lst.remove_back()
    # try:
    #     print(lst.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    # print('\n# get_back example 1')
    # lst = CircularList([1, 2, 3])
    # lst.add_back(4)
    # print(lst.get_back())
    # lst.remove_back()
    # print(lst)
    # print(lst.get_back())
    # # #
    # print('\n# remove example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3]:
    #     print(lst.remove(value), lst.length(), lst)
    # #
    # print('\n# count example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    #
    # print('\n# swap_pairs example 1')
    # lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    # test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
    #               (4, 2), (3, 3), (1, 2), (2, 1))
    #
    # for i, j in test_cases:
    #     print('Swap nodes ', i, j, ' ', end='')
    #     try:
    #         lst.swap_pairs(i, j)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# reverse example 1')
    # test_cases = (
    #     [1, 2, 3, 3, 4, 5],
    #     [1, 2, 3, 4, 5],
    #     ['A', 'B', 'C', 'D']
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     lst.reverse()
    #     print(lst)
    #
    # print('\n# reverse example 2')
    # lst = CircularList()
    # print(lst)
    # lst.reverse()
    # print(lst)
    # lst.add_back(2)
    # lst.add_back(3)
    # lst.add_front(1)
    # lst.reverse()
    # print(lst)
    #
    # print('\n# reverse example 3')
    #
    #
    # class Student:
    #     def __init__(self, name, age):
    #         self.name, self.age = name, age
    #
    #     def __eq__(self, other):
    #         return self.age == other.age
    #
    #     def __str__(self):
    #         return str(self.name) + ' ' + str(self.age)


    # s1, s2 = Student('John', 20), Student('Andy', 20)
    # lst = CircularList([s1, s2])
    # print(lst)
    # lst.reverse()
    # print(lst)
    # print(s1 == s2)
    #
    # print('\n# reverse example 4')
    # lst = CircularList([1, 'A'])
    # lst.reverse()
    # print(lst)
    #
    # print('\n# sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print(lst)
    #     lst.sort()
    #     print(lst)
    #
    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = list(source)
    print(lst)
    #
    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)

    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)
    # #
    # print('\n# remove_duplicates example 1')
    # test_cases = (
    # [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    # [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    # [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],list("abccd"),list("005BCDDEEFI")
    # )
    #
    # print(list("032hfsha"))
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.remove_duplicates()
    #     print('OUTPUT:', lst)

    print('\n# odd_even example 1')
    test_cases = (
    [1, 2, 3, 4, 5], list('ABCDE'),
    [], [100], [100, 200], [100, 200, 300],
    [100, 200, 300, 400],
    [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E'] )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)
