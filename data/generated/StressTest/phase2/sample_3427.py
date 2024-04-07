# Premise: Craig had less than 400 apples.
# Hypothesis: Craig had 200 apples.
# Golden Label: neutral

apples_premise = 400
apples_hypothesis = 200

# the hypothesis refers to the number of apples Craig had, also mentioned in the premise
if apples_hypothesis >= apples_premise:
    # check if the number of apples in the hypothesis contradicts the premise's estimate of less than 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples less than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

