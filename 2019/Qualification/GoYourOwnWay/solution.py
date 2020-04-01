"""
On this problem I spent a little time pondering first.
I realized that as long as the other path was subject
to the same constraints (this was not actually expressed
in the problem, though, so it was risky), then there would
always be one valid and extrememly simple solution, and it
should be very easy to find. 

The idea is to either discover that you can go "all the
way around", or that you need to cross the other path,
but you would only have to cross it exactly once. This
truth arises entirely from the specific constraints expressed.

I start by looking at the first and last steps in the
other path. If they are "opposites" of each other (that
is, if the path starts with a vertical and ends with 
horizontal, or vice versa), we can take a perimiter-only
approach. If they are the same direction as each other,
we need to find a crossing point, which I seek as the 
first place where the path moves 2 steps in the same 
direction. With a little thinking I convinced myself that
this would always be true of their path: that there would
necessarily be somewhere in their path where they stepped
twice in the same direction, and that direction would be
"opposite" the start/end menuver direction.

So my algorithm seeks the first of these cases, counts
the previous steps in that direction to figure out how
far over or down we need to traverse, and then makes
a simple 3 legged path, essentially perimiter-only
except for one board-crossing meneuver that aligns
with the place the other path is crossable.

If there was no time pressure (I know there technically
isn't for me, but what fun would it be if I didn't pretend
there was??), the first "cleanup" I would do is
generalizing the last two cases. Their logic is identical,
with only the specific direction names swapped. I don't like 
code like this :-) but I want to stick to a "pure" sharing here
of the code I would actually submit under competetive 
circumstances.
"""


def firstlast(in_str):
    return (in_str[0], in_str[-1])

def main():
    num_cases = input()
    for c in range(1, int(num_cases) + 1):
        size = int(input())
        other = input()
        if firstlast(other) == ('E','S'):
            answer = "S" * (size-1) + "E" * (size-1)
        elif firstlast(other) == ('S', 'E'):
            answer = "E" * (size-1) + "S" * (size-1)
        elif firstlast(other) == ('E', 'E'):
            cross = other.find("SS")
            # find how many s's before this...
            s_steps = other[0:cross].count("S") + 1
            first = "S" * s_steps
            crossing = "E" * (size-1)
            last = "S" * (size - 1 - s_steps)
            answer = "{0}{1}{2}".format(first, crossing, last)
        else:
            cross = other.find("EE")
            s_steps = other[0:cross].count("E") + 1
            first = "E" * s_steps
            crossing = "S" * (size-1)
            last = "E" * (size - 1 - s_steps)
            answer = "{0}{1}{2}".format(first, crossing, last)
        print("Case #{0}: {1}".format(c, answer))
if __name__ == "__main__":
    main()
