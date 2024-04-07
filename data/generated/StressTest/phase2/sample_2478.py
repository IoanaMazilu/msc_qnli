# Premise: Jill, who lives in City C, plans to visit 2 different cities L, and S.
# Hypothesis: Jill, who lives in City C, plans to visit less than 3 different cities L, and S.
# Golden Label: entailment

cities_to_visit_premise = 2
cities_to_visit_hypothesis = 3

# the hypothesis refers to the number of different cities Jill plans to visit, mentioned in the premise
if cities_to_visit_hypothesis <= cities_to_visit_premise:
    # check if the hypothesis value contradicts the exact number of cities to visit in the premise
    label = "contradiction"
elif cities_to_visit_hypothesis != cities_to_visit_premise + 1:
    # check if the number of cities to visit in the hypothesis contradicts the number of cities to visit reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

