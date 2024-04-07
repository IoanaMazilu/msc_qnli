# Premise: Lindy runs at a constant speed of less than 52 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of 12 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: neutral

speed_premise = 52
speed_hypothesis = 12

# the hypothesis talks about the speed at which Lindy runs, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of less than 'speed_premise'
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # any speed less than 'speed_premise' is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)

