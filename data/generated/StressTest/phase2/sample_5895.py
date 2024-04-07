# Premise: A starts from Delhi with a speed of 20 kmph at 7 a.
# Hypothesis: A starts from Delhi with a speed of less than 30 kmph at 7 a.
# Golden Label: entailment

speed_premise = 20
speed_hypothesis = 30

# the hypothesis talks about the speed of 'A' which is also referenced in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of less than 'speed_hypothesis'
    label = "contradiction"
else:
    # the speed of 'A' in the premise is less than the speed mentioned in the hypothesis
    # hence it is consistent with the hypothesis, so we can infer entailment
    label = "entailment"

print(label)

