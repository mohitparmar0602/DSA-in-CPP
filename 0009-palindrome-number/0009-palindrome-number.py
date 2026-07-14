class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # When the length is an odd number, we can get rid of the middle digit by reverted_number // 10
        # For example, when x = 12321, at the end of the while loop we get x = 12, reverted_number = 123
        # since the middle digit doesn't matter in palindrome, we can simply get rid of it.
        return x == reverted_number or x == reverted_number // 10