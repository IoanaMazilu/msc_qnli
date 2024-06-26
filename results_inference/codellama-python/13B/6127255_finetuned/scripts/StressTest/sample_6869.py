people_seating_premise = 5
people_seating_hypothesis = 5

# the hypothesis refers to the number of people that can be seated on a bench mentioned in the premise
if people_seating_hypothesis >= people_seating_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
