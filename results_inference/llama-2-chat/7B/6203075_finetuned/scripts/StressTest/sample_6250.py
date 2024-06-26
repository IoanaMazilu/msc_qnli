boys_premise = 5
boys_hypothesis = 6
girls_premise = 4
girls_hypothesis = 4

# the hypothesis refers to the number of boys and girls in a group, mentioned in the premise
if boys_hypothesis <= boys_premise:
    # check if the number of boys in the hypothesis contradicts the estimate of more than 'boys_premise'
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
