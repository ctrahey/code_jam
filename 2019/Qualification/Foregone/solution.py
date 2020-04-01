"""
My first thought on this one is to simply reduce every
4 to a 3, and pair it with a corresponding 1 in the same
digit-place. Example: 
 454217
=======
 353217
+101000

So the algorithm is purely string-based.
We simply enumerate the input digits and
build up the output strings one by one.
This turned out to be very similar to one
of the solutions in the analysis section
on Google's site.
"""
def main():
    num_lines = input()
    for c in range(1, int(num_lines) + 1):
        input_string = input()
        a = ''
        b = ''
        for digit in input_string:
            if digit == '4':
                a += '3'
                b += '1'
            else:
                a += digit
                b += '0'
        print("Case #{0}: {1} {2}".format(c, a, b))

if __name__ == "__main__":
    main()
