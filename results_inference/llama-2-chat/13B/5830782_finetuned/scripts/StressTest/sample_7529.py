boys_premise = 6
boys_hypothesis = 3
girls_premise = 4
girls_hypothesis = 4

# the hypothesis refers to the number of boys and girls in a group, mentioned in the premise
if boys_premise!= boys_hypothesis:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
