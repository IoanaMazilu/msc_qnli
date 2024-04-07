# Premise: Carol budgeted less than 28 dollars for gifts for each of the 15 people on her Christmas list.
# Hypothesis: Carol budgeted 18 dollars for gifts for each of the 15 people on her Christmas list.
# Golden Label: neutral

budget_per_person_premise = 28
budget_per_person_hypothesis = 18
people_premise = 15
people_hypothesis = 15

# the hypothesis refers to the budget per person and the number of people on the list mentioned in the premise
if budget_per_person_hypothesis >= budget_per_person_premise:
    # check if the budget per person in the hypothesis contradicts the premise of less than 'budget_per_person_premise'
    label = "contradiction"
elif people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

