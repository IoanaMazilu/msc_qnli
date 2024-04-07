# Premise: How many different possible committees of 4 people can be selected from these 9 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of more than 1 people can be selected from these 9 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: entailment

committee_size_premise = 4
committee_size_hypothesis = 1
people_count = 9

# the hypothesis refers to the size of committees that can be selected from a group of people mentioned in the premise
if committee_size_hypothesis >= committee_size_premise:
    # check if the size of the committee in the hypothesis contradicts the size given in the premise
    label = "contradiction"
elif people_count < committee_size_premise or people_count < committee_size_hypothesis:
    # check if the number of people is less than the required size of the committee in premise and hypothesis
    label = "contradiction"
else:
    # the premise specifies the exact size of the committee, while the hypothesis gives only a lower limit
    # any committee size greater than 'committee_size_hypothesis' and less than or equal to 'committee_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

