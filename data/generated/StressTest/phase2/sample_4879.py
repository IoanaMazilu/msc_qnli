# Premise: How many different possible committees of more than 2 people can be selected from these 8 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of 3 people can be selected from these 8 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: neutral

committees_premise = 2
committees_hypothesis = 3
people_premise = 8
people_hypothesis = 8

# the hypothesis and the premise talk about the number of people in a committee
if committees_hypothesis <= committees_premise:
    # check if the number of people in a committee in the hypothesis contradicts the estimate of more than 'committees_premise'
    label = "contradiction"
elif people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in a committee
    # any number of people greater than 'committees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

