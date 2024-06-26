deaths_premise = 5
deaths_hypothesis = 5
fleeing_premise = 85
fleeing_hypothesis = 85

# the hypothesis refers to the number of deaths and people fleeing mentioned in the premise
if deaths_premise!= deaths_hypothesis:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
elif fleeing_hypothesis!= fleeing_premise:
    # check if the number of people fleeing in the hypothesis contradicts the number of people fleeing reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
