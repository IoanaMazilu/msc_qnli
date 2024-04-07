# Premise: Winson will arrange more than 5 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Hypothesis: Winson will arrange 6 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Golden Label: neutral

people_arrange_premise = 5
people_arrange_hypothesis = 6

# the hypothesis talks about the number of people Winson will arrange, referenced also in the premise
if people_arrange_hypothesis <= people_arrange_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_arrange_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_arrange_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

