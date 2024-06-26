boys_group_premise = 8
boys_group_hypothesis = 6
girls_group_premise = 4
girls_group_hypothesis = 4
committee_size_premise = 4
committee_size_hypothesis = 4

# the hypothesis refers to the number of boys, girls and committee size mentioned in the premise
if boys_group_hypothesis >= boys_group_premise:
    # check if the number of boys in the hypothesis contradicts the estimate of less than 'boys_group_premise'
    label = "contradiction"
elif girls_group_hypothesis != girls_group_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
elif committee_size_hypothesis != committee_size_premise:
    # check if the committee size in the hypothesis contradicts the committee size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
