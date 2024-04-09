start_age_premise = 20
start_age_hypothesis = 40

# the hypothesis refers to the age when Jane started baby-sitting
if start_age_hypothesis <= start_age_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif start_age_premise > start_age_hypothesis:
    # the premise indicates that Jane started baby-sitting at 20, which is less than the hypothesis
    label = "entailment"
else:
    # the premise only gives an estimate of the age, so we cannot infer entailment or contradiction
    label = "neutral"

print(label)
