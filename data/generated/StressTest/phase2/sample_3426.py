# Premise: Craig had 200 apples.
# Hypothesis: Craig had less than 400 apples.
# Golden Label: entailment

apples_premise = 200
apples_hypothesis = 400

# the hypothesis talks about the number of apples Craig had, referenced also in the premise
if apples_premise >= apples_hypothesis:
    # check if the premise value contradicts the estimate of less than 'apples_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an estimate for the number of apples
    # any number of apples less than 'apples_hypothesis' is consistent with the hypothesis, but since we know exactly how many apples Craig had, we can infer entailment
    label = "entailment"

print(label)

