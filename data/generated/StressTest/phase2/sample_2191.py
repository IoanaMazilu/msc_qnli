# Premise: Jill, who lives in City C, plans to visit less than 6 different cities, M, L, S, N, and O.
# Hypothesis: Jill, who lives in City C, plans to visit 5 different cities, M, L, S, N, and O.
# Golden Label: neutral

cities_to_visit_premise = 6
cities_to_visit_hypothesis = 5

# the hypothesis talks about the number of cities Jill plans to visit, referenced also in the premise
if cities_to_visit_hypothesis >= cities_to_visit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cities_to_visit_premise'
    label = "contradiction"
elif cities_to_visit_hypothesis < cities_to_visit_premise - 1:
    # check if the hypothesis value is less than 'cities_to_visit_premise' minus 1,
    # this would also contradict the premise
    label = "contradiction"
else:
    # any number of cities less than 'cities_to_visit_premise' but more than 'cities_to_visit_premise' minus 1
    # is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

