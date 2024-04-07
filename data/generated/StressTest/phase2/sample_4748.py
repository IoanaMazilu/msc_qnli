# Premise: If Glen is 130 km away from Hannah at 6 am, and also 130 km away from Hannah at 11 am, then how fast is Hannah driving (in kilometers per hour)?
# Hypothesis: If Glen is 430 km away from Hannah at 6 am, and also 130 km away from Hannah at 11 am, then how fast is Hannah driving (in kilometers per hour)?
# Golden Label: contradiction

distance_glen_hannah_premise = 130
distance_glen_hannah_hypothesis = 430

# the hypothesis refers to the same scenario as the premise, but with a different initial distance between Glen and Hannah
if distance_glen_hannah_hypothesis != distance_glen_hannah_premise:
    # the hypothesis contradicts the premise in terms of the initial distance between Glen and Hannah
    label = "contradiction"
else:
    # the hypothesis is identical to the premise apart from the initial distance, which is not specified in the hypothesis
    label = "neutral"

print(label)

