# Premise: more than 2600 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: 6600 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: neutral

total_premise = 2600
total_hypothesis = 6600

# the hypothesis refers to the same persons and the same ratio as in the premise
if total_hypothesis <= total_premise:
    # check if the total value in the hypothesis contradicts the estimate of more than 'total_premise'
    label = "contradiction"
elif total_hypothesis > total_premise:
    # the premise gives only an estimate for the total
    # a total greater than 'total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

