boys_premise = 2
girls_premise = 4
committee_size_premise = 4

boys_hypothesis = 6
girls_hypothesis = 4
committee_size_hypothesis = 4

# the hypothesis refers to the number of boys and girls in the group and the committee size
if boys_hypothesis <= boys_premise and girls_hypothesis <= girls_premise:
    # check if the hypothesis values for boys and girls contradict the premise values
    label = "contradiction"
elif committee_size_hypothesis!= committee_size_premise:
    # check if the committee size in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values for boys and girls are consistent with the premise values and the committee size is consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
