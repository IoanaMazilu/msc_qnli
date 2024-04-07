# Premise: Billy has less than 20 apples.
# Hypothesis: Billy has 10 apples.
# Golden Label: neutral

apples_billy_premise = 20
apples_billy_hypothesis = 10

# the hypothesis talks about the number of apples Billy has, referenced also in the premise
if apples_billy_hypothesis >= apples_billy_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_billy_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples less than 'apples_billy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

