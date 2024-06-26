dividend_premise = 180
dividend_hypothesis = 380

# the hypothesis refers to the dividend from Carol's stock mentioned in the premise
if dividend_premise != dividend_hypothesis:
    # check if the dividend value in the hypothesis contradicts the dividend value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
