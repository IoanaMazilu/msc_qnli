# Premise: Jane and Thomas are among the 6 people from which a committee of 3 people is to be selected.
# Hypothesis: Jane and Thomas are among the more than 6 people from which a committee of 3 people is to be selected.
# Golden Label: contradiction

people_premise = 6
people_hypothesis = 6

# the hypothesis refers to the same event as the premise
if people_hypothesis < people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif people_hypothesis == people_premise:
    # the hypothesis statement matches exactly the premise
    label = "entailment"
else:
    # the premise gives only an exact value for the number of people
    # any number of people greater than 'people_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

