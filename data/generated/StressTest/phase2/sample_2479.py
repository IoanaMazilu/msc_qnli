# Premise: Jill, who lives in City C, plans to visit less than 3 different cities L, and S.
# Hypothesis: Jill, who lives in City C, plans to visit 2 different cities L, and S.
# Golden Label: neutral

cities_jill_premise = 3
cities_jill_hypothesis = 2

# the hypothesis talks about the number of cities Jill plans to visit, which is also referenced in the premise
if cities_jill_hypothesis >= cities_jill_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cities_jill_premise'
    label = "contradiction"
else:
    # if the number of cities Jill plans to visit in the hypothesis is less than 'cities_jill_premise', it can be explicitly entailed from the premise
    label = "entailment"

print(label)

