# bc + ad = (a + b) * (c + d) - (a * c) - (b * d)
# ^ gauss, 1777-1855
# T(n) <= 3T(n/2 + 1) + Big-O(n)

# ^ Figure 2.1

function multiply(x,y)
# Input: as prior
# Output: as Prior

# e.g. Input positive integers x and y in binary, output is their product

n = max(size x, size y)
if n == 1: return x * y

xL, xR = leftmost abs(n/2), rightmost abs(n/2) bits of x
yL, yR = leftmost abs(n/2), rightmost abs(n/2) bits of y

P1 = multiply(xL, yL)
P2 = multiply(xR, yR)
P3 = multiply((xL + xR), (yL + yR))

return P 1 x 2^n + (P3 - P1 - P2) x 2^(n/2) + P2

## Sum of any increasing geometric series is, within a constant factor,
#  simply the last term of the series (Vazirani, Exercise 0.2)
#

This implemented herein (project for the day).


