# Premise: Jill, who lives in City C, plans to visit 4 different cities, M, N, L, and S.
# Hypothesis: Jill, who lives in City C, plans to visit less than 8 different cities, M, N, L, and S.
# Golden Label: entailment

cities_visit_premise = 4
cities_visit_hypothesis = 8

# the hypothesis talks about the number of cities Jill plans to visit, which is also mentioned in the premise
if cities_visit_hypothesis < cities_visit_premise:
    # check if the estimate of 'cities_visit_hypothesis' contradicts the number of cities mentioned in the premise
    label = "contradiction"
elif cities_visit_hypothesis > cities_visit_premise:
    # the hypothesis gives an upper limit for the number of cities
    # any number of cities less than 'cities_visit_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

