import unittest
import timeit
import mergeSort
#mergesort code is copied directly from geeksforgeeks
#unit tests written with whitebox testing


class MergeSortTest(unittest.TestCase):
    def test_positive(self):
        arr = [2,5,4,6,0,7,3,1]
        self.assertEqual(mergeSort.merge_sort(arr, 0, len(arr)-1), [0,1,2,3,4,5,6,7])


    def test_negative(self):
        #string
        self.assertRaises(TypeError, mergeSort.merge_sort, ["u", "o", "i"])
        #float
        self.assertRaises(TypeError, mergeSort.merge_sort, [2.5,9.1,27.4,1.7])
    
    def test_performance(self):
        arr = [1,2,3,4,5,6,7,8,9,10,12,11,13,14,21,15,16,17,87,33,0]
        #timing the sort
        timing = timeit.timeit(lambda: mergeSort.merge_sort(arr, 0, len(arr)-1), number=1)
        self.assertEqual(mergeSort.merge_sort(arr, 0, len(arr)-1), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,21,33,87])
        #printing the time in seconds with six decimal places
        print(f"Time = {timing:.6f}s")

    def test_boundary(self):
        #empty 
        #this initially failed because the merge_sort function did not consider empty arrays
        #I changed the logic of the function so it would return empty arrays as well
        arr = []
        self.assertEqual(mergeSort.merge_sort(arr, 0, len(arr)-1), [])
        #single
        arr = []
        self.assertEqual(mergeSort.merge_sort(arr, 0, len(arr)-1), [])
        #sorted
        arr = [0,1,2,3,4,5]
        self.assertEqual(mergeSort.merge_sort(arr, 0 , len(arr)-1), [0,1,2,3,4,5])
        #reverse
        arr = [5,4,3,2,1,0]
        self.assertEqual(mergeSort.merge_sort(arr, 0 , len(arr)-1), [0,1,2,3,4,5])
        #duplicate
        arr = [2,3,3,2,1,0]
        self.assertEqual(mergeSort.merge_sort(arr, 0 , len(arr)-1), [0,1,2,2,3,3])

    def test_idempotency(self):
        arr = [3,5,8,2,1]
        self.assertEqual(mergeSort.merge_sort(arr, 0, len(arr)-1), [1,2,3,5,8])
        self.assertEqual(mergeSort.merge_sort(arr, 0, len(arr)-1), [1,2,3,5,8])
        self.assertEqual(mergeSort.merge_sort(arr, 0, len(arr)-1), [1,2,3,5,8])

if __name__ == "__main__":
    unittest.main()