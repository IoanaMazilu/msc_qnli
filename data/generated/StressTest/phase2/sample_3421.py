# Premise: How many different possible committees of more than 1 people can be selected from these 6 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of 3 people can be selected from these 6 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: neutral

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

