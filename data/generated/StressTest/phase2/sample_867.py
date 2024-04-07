# Premise: A starts from Delhi with a speed of 20 kmph at 7 a.
# Hypothesis: A starts from Delhi with a speed of less than 70 kmph at 7 a.
# Golden Label: entailment

speed_premise = 20
speed_hypothesis = 70

# the hypothesis refers to the speed of A mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of 'less than speed_hypothesis'
    label = "contradiction"
else:
    # if the premise speed does not contradict the hypothesis speed, we can infer entailment
    label = "entailment"

print(label)

