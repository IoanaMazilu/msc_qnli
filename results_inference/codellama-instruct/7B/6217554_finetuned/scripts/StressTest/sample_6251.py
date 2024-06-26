boys_group_premise = 6
boys_group_hypothesis = 6
girls_group_premise = 4
girls_group_hypothesis = 4
committee_size_premise = 4
committee_size_hypothesis = 4

# the hypothesis gives an estimate for the number of boys and girls in the group
# any number of boys and girls greater than 'boys_group_premise' and 'girls_group_premise' is consistent with the premise
if boys_group_hypothesis <= boys_group_premise:
    # check if the estimate of 'boys_group_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_group_hypothesis!= girls_group_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
elif committee_size_hypothesis!= committee_size_premise:
    # check if the number of persons in the committee in the hypothesis contradicts the number of persons in the committee reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
