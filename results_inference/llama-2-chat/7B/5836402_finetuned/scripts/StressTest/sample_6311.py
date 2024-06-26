boys_premise = 6
girls_premise = 4
boys_hypothesis = 1
girls_hypothesis = 4

# the hypothesis refers to the number of boys and girls mentioned in the premise
if boys_premise!= boys_hypothesis:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
elif girls_premise!= girls_hypothesis:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
