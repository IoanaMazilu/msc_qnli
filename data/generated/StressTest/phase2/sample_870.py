# Premise: for Mathura and B starts from Mathura with a speed of 25 kmph at 8 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of less than 65 kmph at 8 p.
# Golden Label: entailment

speed_premise = 25
speed_hypothesis = 65

# the hypothesis refers to the speed of B mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of less than 'speed_hypothesis'
    label = "contradiction"
else:
    # the speed in the premise is less than 'speed_hypothesis', so it does not contradict the hypothesis
    # but it cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)

