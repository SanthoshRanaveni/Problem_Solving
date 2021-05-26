Algorithm for Upgrading Junction Boxes.

1. Initially I created two lists. One for storing lowercase english alphabet and one for storing digits
2. Then I iterated over the given array and checked whether the second element is either a letter or a digit.
3. Then I added either to the alphabet list or digits list based on the element
4. Now I sorted the alphabet list.
5. Then I sorted the digits list.
6. I merged both the lists.
7. Returned the merged list.

Time Complexity:
Iterating over the array and adding to lists: O(n)
Sorting the alphabet list: O(mlogm)  considering there are m alphabet strings.
Sorting the digit list: O(klogk)     considering there are k digits
Merging both the lists: O((m+k)log(m+k))


Overall Complexity: O(n) + O(mlogm) + O(klogk) + O()


1. Create two lists that will store the Letter and Digit Lists.
Iterate through each element in the array and check if the second element is a letter or digit and add it to their respective lists.
Sort the Letter Lists.
Sort the digit Lists.
Merge two Lists.
Return the Merged List.