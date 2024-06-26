boys_premise = 6
girls_premise = 4
committee_size_premise = 4

boys_hypothesis = len(boys_premise) - 1
girls_hypothesis = len(girls_premise) - 1
committee_size_hypothesis = 4

# the hypothesis talks about the number of boys and girls in the group
if boys_hypothesis <= girls_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'girls_premise'
    label = "contradiction"
elif girls_hypothesis!= committee_size_premise:
    # check if the number of girls in the hypothesis contradicts the number of committee members reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys and girls in the group
    # any number of boys and girls less than or equal to 'committee_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
