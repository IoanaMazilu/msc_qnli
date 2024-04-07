# Premise: Jenny can divide her sweets equally to more than 4 people and also to 6 people equally but not to 12 people.
# Hypothesis: Jenny can divide her sweets equally to 5 people and also to 6 people equally but not to 12 people.
# Golden Label: neutral

people_divide_sweets_premise = 4
people_divide_sweets_hypothesis = 5
people_divide_sweets_premise_2 = 6
people_divide_sweets_hypothesis_2 = 6
people_cannot_divide_sweets_premise = 12
people_cannot_divide_sweets_hypothesis = 12

# the hypothesis states that Jenny can divide her sweets to more people than stated in the premise
if people_divide_sweets_hypothesis <= people_divide_sweets_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif people_divide_sweets_hypothesis_2 != people_divide_sweets_premise_2:
    # check if the second number of people in the hypothesis contradicts the second number of people in the premise
    label = "contradiction"
elif people_cannot_divide_sweets_hypothesis != people_cannot_divide_sweets_premise:
    # check if the number of people Jenny cannot divide her sweets to in the hypothesis contradicts the number of people Jenny cannot divide her sweets to in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

