# Premise: Lindy runs at a constant speed of 8 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of more than 8 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: contradiction

speed_premise = 8
speed_hypothesis = 8

# the hypothesis talks about the speed of Lindy, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the specified speed of 'speed_premise'
    label = "contradiction"
else:
    # the premise gives an exact speed for Lindy
    # any speed greater than 'speed_premise' contradicts the premise
    label = "contradiction"

print(label)

