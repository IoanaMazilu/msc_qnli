# Premise: less than 600, what is James'capital?
# Hypothesis: 300, what is James'capital?
# Golden Label: neutral

capital_premise = 600
capital_hypothesis = 300

# the hypothesis talks about James' capital, referenced also in the premise
if capital_hypothesis >= capital_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'capital_premise'
    label = "contradiction"
elif capital_hypothesis < capital_premise:
    # the premise gives an upper limit for the capital
    # any capital less than 'capital_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

