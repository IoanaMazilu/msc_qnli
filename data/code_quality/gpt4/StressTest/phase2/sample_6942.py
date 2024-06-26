cities_to_visit_premise = 7
cities_to_visit_hypothesis = 8

# the hypothesis refers to the number of cities Jill plans to visit, mentioned in the premise
if cities_to_visit_premise >= cities_to_visit_hypothesis:
    # check if the estimate of 'cities_to_visit_hypothesis' contradicts the number of cities in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
