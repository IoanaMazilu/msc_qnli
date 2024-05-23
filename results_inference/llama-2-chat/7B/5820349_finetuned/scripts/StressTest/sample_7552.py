boys_premise = 2
boys_hypothesis = 6
girls_premise = 4
girls_hypothesis = 4
committee_premise = 4
committee_hypothesis = 4

# the hypothesis talks about the number of boys, girls and the committee in a group, referenced also in the premise
if boys_hypothesis <= boys_premise:
    # check if the number of boys in the hypothesis contradicts the estimate of more than 'boys_premise'
    label = "contradiction"
elif girls_hypothesis!= girls_premise or committee_hypothesis!= committee_premise:
    # check if the number of girls or the committee in the hypothesis contradicts the number of girls or the committee in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys
    # any number of boys greater than 'boys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)