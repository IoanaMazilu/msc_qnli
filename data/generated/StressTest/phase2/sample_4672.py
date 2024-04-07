# Premise: Jill, who lives in City C, plans to visit less than 8 different cities, M, N, L, and S.
# Hypothesis: Jill, who lives in City C, plans to visit 4 different cities, M, N, L, and S.
# Golden Label: neutral

cities_to_visit_premise = 8
cities_to_visit_hypothesis = 4

# the hypothesis talks about the number of cities Jill plans to visit, which is also mentioned in the premise
if cities_to_visit_hypothesis >= cities_to_visit_premise:
    # check if the number of cities in the hypothesis contradicts the estimate of less than 'cities_to_visit_premise'
    label = "contradiction"
elif cities_to_visit_hypothesis < cities_to_visit_premise:
    # if the number of cities in the hypothesis is less than 'cities_to_visit_premise', we can infer entailment
    label = "entailment"

print(label)

