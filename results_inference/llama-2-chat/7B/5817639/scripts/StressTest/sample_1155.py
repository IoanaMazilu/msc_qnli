approximately_premise = 1979
approximately_hypothesis = 2979

# the hypothesis refers to a smaller time period than the premise
if approximately_hypothesis <= approximately_premise:
    # check if the estimate of 'approximately_hypothesis' contradicts the number of passengers reported in the premise
    label = "contradiction"
else:
    # the premise gives a larger time frame than the hypothesis, so we can infer entailment
    label = "entailment"

print(label)
