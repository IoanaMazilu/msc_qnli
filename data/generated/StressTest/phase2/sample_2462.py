# Premise: Jack wants to take 5 apples.
# Hypothesis: Jack wants to take less than 5 apples.
# Golden Label: contradiction

apples_premise = 5
apples_hypothesis = 5

# the hypothesis refers to the number of apples Jack wants to take, which is also mentioned in the premise
if apples_hypothesis >= apples_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number of apples Jack wants to take
    # any number less than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

