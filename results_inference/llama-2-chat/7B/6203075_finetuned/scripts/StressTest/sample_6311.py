boys_premise = 6
girls_premise = 4
boys_hypothesis = 1
girls_hypothesis = 4

# the hypothesis refers to the total number of boys and girls in the group, which is also mentioned in the premise
if boys_hypothesis!= boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
else:
    # if the number of boys and girls in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
