# Premise: Lindy runs at a constant speed of more than 1 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of 8 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: neutral

speed_premise = 1
speed_hypothesis = 8

# the hypothesis refers to the speed of Lindy mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the 'speed_hypothesis' contradicts the estimate of more than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Lindy's speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

