cities_to_visit_premise = 5
cities_to_visit_hypothesis = 5

# the hypothesis refers to the number of cities Jill plans to visit, mentioned in the premise
if cities_to_visit_hypothesis != cities_to_visit_premise:
    # check if the number of cities to visit in the hypothesis contradicts the number of cities to visit in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
