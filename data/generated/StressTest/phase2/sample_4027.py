# Premise: Richard will arrange less than 7 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Hypothesis: Richard will arrange 6 people of 6 different heights for photograph by placing them in two rows of three so that each person in the first row is standing is standing in front of someone in the second row.
# Golden Label: neutral

people_premise = 7
people_hypothesis = 6

# the hypothesis refers to the number of people Richard will arrange for a photo, also mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the number of people in the hypothesis contradicts the estimation of less than 'people_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of people
    # the number given in the hypothesis is less than 'people_premise', so it doesn't contradict the premise, but it can be explicitly entailed from the premise
    label = "entailment"

print(label)

