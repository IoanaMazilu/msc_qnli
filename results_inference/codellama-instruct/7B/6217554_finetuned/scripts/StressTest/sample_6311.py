boys_group_premise = 6
boys_group_hypothesis = 1
girls_group_premise = 4
girls_group_hypothesis = 4
committee_size_premise = 4
committee_size_hypothesis = 4

# the hypothesis refers to the number of boys and girls in the group and the size of the committee mentioned in the premise
if boys_group_hypothesis!= boys_group_premise or girls_group_hypothesis!= girls_group_premise or committee_size_hypothesis!= committee_size_premise:
    # check if the hypothesis values contradict the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
