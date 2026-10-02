class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Keep only the lowest 32 bits.
        # This is needed because Python integers can be larger than 32 bits,
        # while the problem expects 32-bit integer behavior.
        mask = 0xFFFFFFFF

        # Largest positive signed 32-bit integer:
        # 01111111111111111111111111111111 = 2^31 - 1
        max_int = 0x7FFFFFFF

        # Keep adding until there is no carry left.
        while b != 0:

            # Find the carry bits.
            # a & b identifies positions where both bits are 1.
            # << 1 moves those carry bits one position to the left.
            carry = (a & b) << 1

            # XOR adds the numbers without considering the carry.
            # Apply the mask to keep the result within 32 bits.
            a = (a ^ b) & mask

            # The carry becomes the new value of b.
            # We will add it to a in the next iteration.
            b = carry & mask

        # If the highest bit is 0, the result is positive.
        if a <= max_int:
            return a

        # Otherwise, the highest bit is 1, meaning the result
        # represents a negative number in 32-bit two's complement.
        # Convert the unsigned 32-bit value into Python's negative integer.
        return ~(a ^ mask)