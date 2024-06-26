boys_premise = 2
boys_hypothesis = 6
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis refers to the number of boys and girls in a group and the number of persons in a committee, all mentioned in the premise
if boys_hypothesis <= boys_premise:
    # check if the number of boys in the hypothesis contradicts the estimate of more than 'boys_premise'
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
elif committee_hypothesis!= committee_premise:
    # check if the number of persons in the committee in the hypothesis contradicts the number of persons in the committee reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys
    # any number of boys greater than 'boys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
