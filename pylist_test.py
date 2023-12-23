#!/usr/bin/env python3

# Do not remove the above line, it is needed for testing

import sys

from pylist import LinkedList
import unittest

class TestListMethods(unittest.TestCase):
    """A set of unit tests for the LinkedList class.

    You will need to write a LOT more tests (you can copy/be inspired
    by the posted tests on Canvas).
    
    These test function must ONLY call the defined public API for
    LinkedList (that is, the functions in the LinkedList class that
    were defined as ones you need to implement).

    The reason is because 1/3rd of your grade is a 'capture the flag':
    We have our fully correct solution: this solution contains a bunch
    of 'flags' in the corner cases.  Your tests must trigger our
    corner cases to get full credit.
    
    You MUST also write docstrings for the tests describing what they
    do.  They will be read.  You are welcome to use the tests posted
    associated with Lecture 2, but you need to explain what they are
    doing in the docstrings.
    """

    def test_sanity(self):
        """A simple sanity test of some of the functions you need to do"""
        tmp = LinkedList()
        tmp.append(1)
        tmp.append(1)
        tmp.append(1)
        tmp2 = [1,1,1]
        self.assertEquals(repr(tmp),repr(tmp2))
        self.assertEquals(str(tmp),str(tmp2))
        tmp[0] = 2
        del tmp[1]
        tmp.map_in_place(lambda x: x + 1)
        self.assertEqual(tmp[0], 3)
        self.assertEqual(len(tmp), 2)

    def test_basic(self):
        """A basic check:
        can items be added to the front and back and the length is
        reported right?
        """
        tmp = LinkedList()
        self.assertEqual(len(tmp), 0)
        for i in range(1,4):
            tmp.append(i)
            self.assertEqual(len(tmp), i)
        for i in range(4, 10):
            tmp.prepend(i)
            self.assertEqual(len(tmp), i)
    
    def test_index(self):
        """Tests the index operation for valid values
        Creates a new list, adds 10 items and checks that the ith element is at the correct location.
        """
        tmp = LinkedList()
        for i in range(10):
            tmp.append(i)
        print(tmp)
        for i in range(10):
            self.assertEqual(tmp[i], i)

    def test_bad_index_types(self):
        """Testing the proper errors are raised for bad indexes
        Checking to see if an IndexError is raised when asking for an element in an empty array, element outside length
          & at a negative index. 
        Making sure it handles a type error correctly.
        """
        tmp = LinkedList()
        with self.assertRaises(IndexError):
            tmp[0]
        with self.assertRaises(IndexError):
            tmp[-1]
        with self.assertRaises(TypeError):
            tmp["fubar"]
        with self.assertRaises(IndexError):
            tmp[3]

    def test_del(self): 
        """
        Checking :
            IndexError raised for deleting an el in an empty array
            IndexError raised for deleting at an index that doesn't exist
            IndexError raised for trying to delete an element out of bounds
            TypeError raised for having str index
        """
        tmp = LinkedList()
        with self.assertRaises(IndexError):
            del tmp[2] 
        with self.assertRaises(IndexError):
            tmp[-2]
        for i in range(10):
            tmp.append(i)
        with self.assertRaises(IndexError):
            del tmp[10] 
        with self.assertRaises(TypeError):
            del tmp["text"] 
        
    def test_del_good(self):
        """Tests to see if delete does what it should do
        
        - Deleting the head of the list, checks to make sure each element is what it should be and checks that
        length was properly updated
        - Deleting the end of the list
        - Deleting from somehwere within the lsit (not head or end)
        """
        tmp = LinkedList()
        for i in range(10):
            tmp.append(i)
        del tmp[0] #9 elements
        for i in range(9):
            self.assertEqual(tmp[i], i+1)
        self.assertEqual(len(tmp), 9)
        del tmp[8]
        self.assertEqual(len(tmp), 8)
        for i in range(8):
            self.assertEqual(tmp[i], i+1)

    def test_get(self):
        """Testing get for first and last elements in a longer list
        """ 
        tmp = LinkedList()
        for i in range (1000):
            tmp.append(i)
        self.assertEqual(tmp[0], 0)
        self.assertEqual(tmp[999], 999)

    def test_map(self):
        """Testing map in place for applying function to all elements in a list
        Checks to verify map in place worked for all functions
        
        """
        tmp = LinkedList()
        for i in range(10):
            tmp.append(i)
        
    
    def test_prepend(self):
        tmp = LinkedList()
        for i in range(10000):
            tmp.prepend(i)
        count = 999
        for x in range(10000):
            self.assertEqual(x, count)
            count -= 1
    

        
    def test_length(self):
        """Testing to make sure the length is properly updated

        Checks if length is properly updated each time you append, prepend and delete
        Also checks that length is properly updated when you __set__ the "last" element in an array
        
        """
        tmp = LinkedList()
        length1 = 0
        for i in range(10):
            tmp.append(i)
            length1 += 1
            self.assertEqual(length1, len(tmp))

        length2 = 10
        for i in range(10):
            del tmp[0] 
            length2 -= 1
            self.assertEqual(length2, len(tmp))
    
        tmp2 = LinkedList()
        

        for i in range(10):
            tmp2.prepend(i)
            self.assertEqual(tmp.length, len(tmp))
        
        tmp[10] = 11
        self.assertEqual(11, len(tmp))

        
    def test_append(self):
        """Appending items to a list and making sure that append is correctly appending to the list
        
        """
        tmp = LinkedList()
        for i in range(10):
            tmp.append(i)
        count = 0
        for x in tmp: 
            self.assertEqual(x, count)
            count += 1
    def test_prepend(self):
        tmp = LinkedList()
        for i in range (10):
            tmp.prepend(i)
        count = 9
        for x in tmp:
            self.assertEqual(x, count)
            count -= 1
    def test_single_element(self):
        """Testing to see if functions work for an element with just one list

        Checks that we can append to an empty list,
        delete from a single element list, and prepend to a single element list
        """
        tmp = LinkedList()
        tmp.append(0)
        self.assertEqual(tmp[0], 0)
        del tmp[0]
        self.assertEqual(len(tmp),0)
        tmp.append(1)
        tmp.prepend(0)
        self.assertEqual(tmp[0], 0)

        
    def test_mult_els(self):
        """Tests if functions work for a multi-element list
        
        Checks if functions work for string elements and larger sizes
        """
        tmp = LinkedList()
        myString = "abcdefg"
        for x in myString:
            tmp.append(x)
        count = 0
        for x in myString:
            self.assertEqual(tmp[count], x)
            count += 1
        
        bigList = LinkedList()
        for x in range(1000):
            tmp.append(x)
        count2 = 0
        for i in bigList:
            self.assertEqual(tmp[count2], x)
            count += 1
    
    def test_set(self):
        """Tests to make sure set does the right thing
        Making sure you can't set an element in an empty list.
        Makes a list of 10 items, checks to make sure you can't set an item outside of the list
        Then, goes through the list and sets each item to itself +1 and makes sure each was set correctly
        Checks to see if can correctly set last element of a list to some data (in HW description, should be able
        to set list[len(list)], ~= appending a new LinkedListCell)
        """
        tmp = LinkedList()
    
        with self.assertRaises(IndexError):
            tmp[2] = 4
        for i in range(10):
            tmp.append(i)
        with self.assertRaises(IndexError):
            tmp[13] = 4
        for i in range(10):
            tmp[i] = tmp[i]+1
            self.assertEqual(tmp[i], i+1)
        
        tmp[10] = 10
        self.assertEqual(tmp[10], 10)
 


        

"""Run the unit tests"""
if __name__ == '__main__':
    print("It is OK to print as much as you want to standard error", file=sys.stderr)
    unittest.main()



