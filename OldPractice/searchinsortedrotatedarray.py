'''
Input arr[] = {3, 4, 5, 1, 2}
Element to Search = 1
  1) Find out pivot point and divide the array in two
      sub-arrays. (pivot = 2) /*Index of 5*/
  2) Now call binary search for one of the two sub-arrays.
      (a) If element is greater than 0th element then
             search in left array
      (b) Else Search in right array
          (1 will go in else as 1 < 0th element(3))
  3) If element is found in selected sub-array then return index
     Else return -1.
'''

def calc(lst,l,h,key):
    pivot = findpivot(lst,l,h)

    if pivot == -1:
        return binarysearch(lst,l,h,key)

    if key == lst[pivot]:
        return pivot

    if lst[0] <= key:
        return binarysearch(lst,l,pivot-1,key)

    return binarysearch(lst,pivot+1,h,key)



def binarysearch(arr,low,high,key):

    mid = int((high+low)/2)

    if arr[mid]== key:
        return mid
    if key > arr[mid]:
        return binarysearch(arr,mid+1,high,key)
    else:
        return binarysearch(arr,low,mid-1,key)


def findpivot(arr,low , high):

    if low > high:
        return -1
    if low == high:
        return low

    mid = int((high+low)/2)
    if low < mid and arr[mid] > arr[mid+1]:
        return mid
    if high > mid and arr[mid-1] >arr[mid]:
        return mid-1
    if arr[low] >= arr[mid]:
        return findpivot(arr,low,mid-1)
    return findpivot(arr,mid+1,high)



if __name__ == "__main__":
    lst = [4, 5, 6, 7, 8, 9,10, 1, 2, 3]
    h = len(lst) - 1 
    l = 0
    key = 6
    place = calc(lst,l,h,key)

    print(f"Value {key} is found at position : {place}")
    