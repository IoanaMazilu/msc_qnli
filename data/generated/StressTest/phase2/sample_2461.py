# Premise: Jack wants to take more than 3 apples.
# Hypothesis: Jack wants to take 5 apples.
# Golden Label: neutral

apples_premise = 3
apples_hypothesis = 5

# the hypothesis mentions a specific number of apples that Jack wants to take, which is also discussed in the premise
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

