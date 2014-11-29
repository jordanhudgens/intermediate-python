# http://towersofhanoi.info/Animate.aspx

def hanoi(n, start_pole, end_pole, inter_pole):

    # Checks to see if there are still discs left on the pole
    if n >= 1:
        hanoi(n - 1, start_pole, inter_pole, end_pole) # Call method recursively
        print("Disc moves from", start_pole, "to", end_pole, "pole") # Print out step
        hanoi(n - 1, inter_pole, end_pole, start_pole) # Call method recursively

# Calls problem and passes in 3 for the number of discs to start out with
hanoi(3, "a", "b", "c")