children_man_premise = 2
children_man_hypothesis = 3

# the hypothesis talks about the number of children of the man, referenced also in the premise
if children_man_hypothesis <= children_man_premise:
    # check if the hypothesis value contradicts the estimate of more than 'children_man_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of children
    # any number of children greater than 'children_man_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
