dividend_premise = 180
dividend_hypothesis = 880

# the hypothesis refers to the dividend from Carol's stock mentioned in the premise
if dividend_premise >= dividend_hypothesis:
    # check if the estimate of 'dividend_hypothesis' contradicts the value of Carol's stock dividend in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
