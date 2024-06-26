girls_premise = 5
girls_hypothesis = 4

# the hypothesis refers to the number of girls going on a date, mentioned also in the premise
if girls_hypothesis > girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
elif girls_hypothesis == girls_premise:
    # check if the number of girls in the hypothesis matches the number of girls in the premise
    label = "entailment"
else:
    # if the number of girls in the hypothesis is less than the number in the premise, it does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
