lists_premise = 4/4
lists_hypothesis = 1/4
members_premise = 760
members_hypothesis = 760

# the hypothesis refers to the number of lists and members mentioned in the premise
if lists_hypothesis >= lists_premise:
    # check if the number of lists in the hypothesis contradicts the estimate of less than 'lists_premise'
    label = "contradiction"
elif members_hypothesis!= members_premise:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of lists
    # any number of lists less than 'lists_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
