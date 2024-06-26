people_seating_premise = 4
people_seating_hypothesis = 4

# the hypothesis refers to the number of people that can be seated on a bench mentioned in the premise
if people_seating_hypothesis > people_seating_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif people_seating_hypothesis <= people_seating_premise:
    # if the hypothesis value is less or equal to the premise ones, we can infer entailment
    label = "entailment"

print(label)
