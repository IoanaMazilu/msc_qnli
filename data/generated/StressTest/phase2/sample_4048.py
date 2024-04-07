# Premise: How many different possible committees of more than 1 people can be selected from these 9 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of 4 people can be selected from these 9 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: neutral

committee_size_premise = 1
committee_size_hypothesis = 4
total_people = 9

# The hypothesis refers to the size of the committees that can be formed from the total people, as stated in the premise
if committee_size_hypothesis <= committee_size_premise:
    # check if the committee size in the hypothesis contradicts the premise's condition of more than 'committee_size_premise'
    label = "contradiction"
elif committee_size_hypothesis > total_people:
    # check if the committee size in the hypothesis contradicts the total number of available people
    label = "contradiction"
else:
    # the premise only gives a minimum size for the committees
    # any committee size larger than 'committee_size_premise' and less than or equal to 'total_people' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

