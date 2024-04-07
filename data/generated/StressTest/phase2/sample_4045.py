# Premise: Jane and Thomas are among the more than 8 people from which a committee of 4 people is to be selected.
# Hypothesis: Jane and Thomas are among the 9 people from which a committee of 4 people is to be selected.
# Golden Label: neutral

people_premise = 8
people_hypothesis = 9

# the hypothesis refers to the number of people from which a committee is selected, as mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the number of people in the hypothesis contradicts the premise stating more than 'people_premise'
    label = "contradiction"
elif people_hypothesis > people_premise:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

