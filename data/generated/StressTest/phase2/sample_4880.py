# Premise: How many different possible committees of 3 people can be selected from these 8 people if at least one of either Jane or Thomas is to be selected?
# Hypothesis: How many different possible committees of 1 people can be selected from these 8 people if at least one of either Jane or Thomas is to be selected?
# Golden Label: contradiction

committees_people_premise = 3
committees_people_hypothesis = 1
total_people = 8

# the hypothesis refers to the number of people in a committee mentioned in the premise
if committees_people_hypothesis > committees_people_premise:
    # check if the hypothesis value contradicts the number of people in a committee in the premise
    label = "contradiction"
elif committees_people_hypothesis < committees_people_premise:
    # if the number of people in a committee in hypothesis is less than that in premise, we can infer entailment
    label = "entailment"
else:
    # if the number of people in a committee in hypothesis is equal to that in premise, it's neutral
    label = "neutral"

print(label)

