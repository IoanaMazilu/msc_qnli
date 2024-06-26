kg_kiwi_premise = 8
kg_kiwi_hypothesis = float(input("Enter the amount of kiwi fruit bought (in kg): "))
avg_rate_premise = 360

# check if the hypothesis value contradicts the estimate of 'kg_kiwi_premise'
if kg_kiwi_hypothesis > kg_kiwi_premise:
    label = "contradiction"
elif kg_kiwi_hypothesis <= kg_kiwi_premise:
    # check if the hypothesis value is consistent with the premise
    if avg_rate_premise == avg_rate_hypothesis:
        # if the hypothesis value is consistent with the premise, we can infer entailment
        label = "entailment"
    else:
        # the hypothesis value is consistent with the premise, but the rate is different
        label = "neutral"
else:
    # the hypothesis value is greater than the premise value, so there is no need for further comparison
    label = "neutral"

print(label)
