boys_group_premise = 6
boys_group_hypothesis = 2
girls_group_premise = 4
girls_group_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis refers to the number of boys and girls in a group and the committee size
if boys_group_premise <= boys_group_hypothesis:
    # check if the estimate of 'boys_group_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_group_hypothesis!= girls_group_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
elif committee_hypothesis!= committee_premise:
    # check if the committee size in the hypothesis contradicts the committee size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
