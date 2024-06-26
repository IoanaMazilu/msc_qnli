committee_premise = 1
committee_hypothesis = 3

# the hypothesis refers to the number of people in a committee mentioned in the premise
if committee_hypothesis <= committee_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif committee_hypothesis > committee_premise:
    # the premise gives an estimate for the number of people in a committee 
    # any number of people greater than 'committee_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
