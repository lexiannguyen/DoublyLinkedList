
# used to make sure print({something}, file=sys.stderr) works

import sys


class LinkedList:
    
    """A class for a linked list in Python, for ECS 32B at UC Davis.

    A class created for homework so students can get practice with good coding style, unit tests, classes, end other features.
    
    *You will need to implement multiple functions within this,
    including improving the running time of existing functions,
    implementing some functions, and developing tests to make sure
    your code is correct.*

    """

    class LinkedListCell:
        """This is an individual data cell for the linked list.

        We have it be an internal class because the abstract data for
        the LinkedList overall class should not expose this structure
        to others.  We can't use a tuple (a, b) type as tuples are
        immutable.  We COULD use python's arrays but we want named
        fields and the ability to define an iter function.
        
        Cells have two elements: the 'data' and the 'tail'.  Trivia:
        In a lisp language (e.g. Scheme, elisp), this would be 'car'
        and 'cdr'

        """
        def __init__(self, data):
            """Initializes a data cell with data, previous and mynext

            Data = what the cell contains, prev = previous cell, mynext = next cell
            """
            self.data = data
            self.prev = None
            self.mynext = None

        def __iter__(self):   
            """An internal iteration operation that returns the cells
            themselves.  So "for x in self.head" when called from within
            the LinkedList it iterates over the linked list cells.

            Technically you do NOT need to build this, but you may
            very well want to because it makes a fair amount of your
            other code simpler and cleaner.  So think of it as a
            strong hint as Something You Want to Do (tm).
            """
            """
            at = self
            while at != None:
                yield at.data
                at = at.mynext
            """
           
        
    def __init__(self):
        """Creates a new empty LinkedList

        The head refers to the first element of the linked list.
        The tail refers to the last element of the linked list.
        The length stores the number of elements in the linked list, 
        and is updated whenever an element is prepended, appended, or deleted.
        """
        self.head = None 
        self.length = 0
        self.tail = None

    def __repr__(self):  #ASSIGNED TO CHANGE FOR HOMEWORK
        """Implements the repr() operation.

        The repr() should be like python's arrays: that is, an open
        bracket [, elements separated by a comma and a space, and a
        closed bracket.  This makes it much clearer on the command
        line what a LinkedList actually is.

        However, unlike the repr function for arrays, you can assume
        that you do not have a loop, that is, no contents of a
        LinkedList can indirectly include itself.
        """
        #raise NotImplementedError 
        #return "[ start=%i, length=%i, data=%s ]" % (self.head ,self.length, self.head.data)
        res = "["
        at = self.head
        while at != None:
            if at.mynext == None:
                res += str(at.data)
            else:
                res += str(at.data) + ","
                at = at.mynext
        return res + "]"

    def __str__(self):  #done!
        """Implements the str() operation.

        The str() should be like python's arrays: that is, an open
        bracket [, elements (as output by str()) separated by a comma
        and a space, and a closed bracket.

        This will allow things like print(alinkedlist) to work.
        
        However, unlike the repr/string function for arrays, you can assume
        that you do not have a loop, that is, no contents of a
        LinkedList can indirectly include itself.
        """
        res = "["
        at = self.head
        while at != None: #at refers to linkedlist cell
            res += str(at.data) + "/"
            at = at.mynext         
        return res + "]"

    def __iter__(self): 
        """Return a new iteration object for the "for x in n" convention

        This implementation of an iterator is 'thread safe': each
        iterator is its own element rather than updating a variable
        internal to the class.

        Hint: For some of the other problems you may very much want to
        use "for x in self", which will work thanks to this.

        """
        tmp = self.head
        while tmp != None:
            yield tmp.data
            tmp = tmp.mynext

    def __getitem__(self, index):
        """This handles the [] operation for reading data

        it first checks that it is given
        an integer (if not it raises TypeError).  It then checks for a
        negative index (if so it raises IndexError).  Finally, it just
        goes along the list until it either finds the end (raising
        IndexError) or finds the desired element.
        """
        if not isinstance(index, int):
            raise TypeError 
        if index < 0:
            raise IndexError
        if index > self.length:
            raise IndexError
        tmp = self.head
        if tmp == None:
            raise IndexError 
        
        while index > 0:
            tmp = tmp.mynext
            index += -1
            if tmp == None:
                raise IndexError 
        return tmp.data

    def __setitem__(self, index, data): 
        """This function handles the [] assignment operation

        It raises the right errors for using index.
        If the index exists the cell must be changed to insert the right data.  
        It is OK for this to be O(N)

        This should handle the case properly when a list has n
        elements and you want to set element n (that is, add an
        element).  Thus, eg, tmp[len(tmp)] = 32 should work, and not
        raise an IndexError.  (This behavior is different from
        Python's built in 'list'/array type.

        note - prof said tmp[len(tmp) = 32 should work means it should be appending]

        """
        if not isinstance(index, int):
            raise IndexError 
        if index < 0:
            raise IndexError
        if index > self.length:
            raise IndexError #out of bounds
        if index == self.length:
            self.append(data)

        cur = self.head
        count = 0
        while count < self.length:
            if count == index:
                cur.data = data
            cur = cur.mynext
            count += 1
        
        
    def __delitem__(self, index):  #ASSIGNED TO CHANGE FOR HOMEWORK
        """This handles the collection del list[index] operation for a
        single index.

        This must raise the proper errors: the index must be valid and
        the index must exist.  It is OK for this to be O(N)

        """
        
        if not isinstance(index, int):
            raise TypeError
        if index < 0:
            raise IndexError
        if index >= (self.length):
            raise IndexError #greater than the list's length
        
        cur = self.head
        count = 0
        found = False
        prev = None
        while (not found):
            if count == index:
                found = True
            else:
                prev = cur
                cur = cur.mynext
                count += 1
        if cur.prev == None:
            self.head = cur.mynext
        else:
            curNext = cur.mynext
            cur = prev
            cur.mynext = curNext
        self.length -= 1
       
    def map_in_place(self, fn):  #done?
        """This should do map() but in-place, replacing each data
        element of the list with fn(data).

        Unlike python map this is eager: it immediately applies to all
        elements and returns, no yield involved, since this is about
        replacing elements not generating a new collection.  It should
        be O(N) time.

        """
        #raise NotImplementedError
        for x in self:
            x = fn(x)
        return self
    def prepend(self, data): #works!
        """Add an element to the front of the list.  O(1)"""
        self.length += 1
        if self.head == None:
            self.head = self.LinkedListCell(data)
        else:
            newCell = self.LinkedListCell(data)
            self.head.prev = newCell
            newCell.mynext = self.head
            self.head = newCell
            newCell.prev = None
                  
    def append(self, data):  #HW: make O(1) - works
        #append to last element --> know where the last element is 
        """Add an element to the back of the list.

        If the list is empty, create a list with just one cell and increment length.
        If not, find the last cell in the list, and create a new cell.
        Have the previous last cell's tail point to the new cell created, and increment length

        """
        self.length += 1
        if self.head == None: #works!
            self.head = self.tail = self.LinkedListCell(data)
            self.prev = None
            #self.length += 1
        else:  
            newTail = self.LinkedListCell(data)
            newTail.prev = self.tail #self[self.length-1]
            self.tail.mynext = newTail #last cell's tail pointed to a new cell
            self.tail = newTail #assign last cell to the tail
            #self.length += 1

    def __len__(self):  #make O(1) done 
    
        """Implements the len(list) operation.
        
        """
        return self.length
    
        
   
    

