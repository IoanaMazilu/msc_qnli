cities_to_visit_premise = 6
cities_to_visit_hypothesis = 6

# the hypothesis refers to the number of cities Jill plans to visit, which is also mentioned in the premise
if cities_to_visit_hypothesis >= cities_to_visit_premise:
    # check if the hypothesis estimate contradicts the exact number of cities to visit in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
