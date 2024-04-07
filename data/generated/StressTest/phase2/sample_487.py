# Premise: If Dana gives her parents less than 3% of that amount back each month, how much will she still owe her parents after three years of college?
# Hypothesis: If Dana gives her parents 2% of that amount back each month, how much will she still owe her parents after three years of college?
# Golden Label: neutral

return_rate_premise = 3
return_rate_hypothesis = 2

# the hypothesis refers to the percentage that Dana gives back to her parents each month, which is also mentioned in the premise
if return_rate_hypothesis >= return_rate_premise:
    # check if the hypothesis value contradicts the premise of less than 'return_rate_premise'%
    label = "contradiction"
elif return_rate_hypothesis == return_rate_premise - 1:
    # if the return rate in the hypothesis is exactly one percentage point less than the one in the premise, we can infer entailment
    label = "entailment"
else:
    # any return rate less than 'return_rate_premise'% is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

