boys_group_premise = 6
boys_group_hypothesis = 5
girls_group_premise = 4
girls_group_hypothesis = 4
committee_size_premise = 4
committee_size_hypothesis = 4

# the hypothesis refers to the number of boys, girls and the size of the committee mentioned in the premise
if boys_group_premise <= boys_group_hypothesis:
    # check if the estimate of 'boys_group_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_group_hypothesis != girls_group_premise or committee_size_premise != committee_size_hypothesis:
    # check if the number of girls or the size of the committee in the hypothesis contradicts the number of girls or the size of the committee reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
