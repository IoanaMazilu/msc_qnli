boys_premise = 6
girls_premise = 4
hypothesis = 1

# the hypothesis refers to the number of boys and girls in the group
if boys_premise >= hypothesis:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
elif girls_premise >= hypothesis:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the estimate in the premise do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
