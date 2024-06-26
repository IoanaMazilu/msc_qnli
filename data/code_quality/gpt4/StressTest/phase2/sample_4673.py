cities_to_visit_premise = 4
cities_to_visit_hypothesis = 4

# the hypothesis mentions a number of cities to be visited, also stated in the premise
if cities_to_visit_hypothesis != cities_to_visit_premise:
    # check if the number of cities in the hypothesis contradicts the number of cities in the premise
    label = "contradiction"
else:
    # if the number of cities in the premise and hypothesis are the same, we infer entailment
    label = "entailment"

print(label)
