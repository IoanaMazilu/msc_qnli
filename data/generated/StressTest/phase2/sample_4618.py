# Premise: The distance from Steve's house to work is less than 45 Km.
# Hypothesis: The distance from Steve's house to work is 35 Km.
# Golden Label: neutral

distance_to_work_premise = 45
distance_to_work_hypothesis = 35

# the hypothesis mentions a specific distance from Steve's house to work, the premise gives an estimate
if distance_to_work_hypothesis >= distance_to_work_premise:
    # check if the distance in the hypothesis contradicts the 'less than' estimate from the premise
    label = "contradiction"
else:
    # any distance less than 'distance_to_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

