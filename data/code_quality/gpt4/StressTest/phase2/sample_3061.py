boys_group_premise = 1
boys_group_hypothesis = 6
girls_group_premise = 4
girls_group_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis talks about the number of boys and girls in a group, and the committee to be formed, all referenced in the premise
if boys_group_hypothesis <= boys_group_premise or girls_group_hypothesis != girls_group_premise:
    # check if the number of boys in the hypothesis contradicts the estimate of more than 'boys_group_premise'
    # also check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
elif committee_hypothesis != committee_premise:
    # check if the number of persons in the committee in the hypothesis contradicts the number of persons in the committee in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys
    # any number of boys greater than 'boys_group_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
