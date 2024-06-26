rupee_premise = 65.36
rupee_hypothesis = 68.19
sensex_premise = 300
sensex_hypothesis = 282.50
nifty_premise = 27
nifty_hypothesis = 28

# the hypothesis refers to the same event as the premise, but with different values
if rupee_premise > rupee_hypothesis:
    # check if the premise value contradicts the hypothesis value
    label = "contradiction"
elif sensex_premise > sensex_hypothesis:
    # check if the premise value contradicts the hypothesis value
    label = "contradiction"
elif nifty_premise > nifty_hypothesis:
    # check if the premise value contradicts the hypothesis value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
