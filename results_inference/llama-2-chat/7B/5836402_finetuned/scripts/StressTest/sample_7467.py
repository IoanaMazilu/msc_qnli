graduates_premise = 0.10
graduates_hypothesis = 0.07

# the hypothesis refers to the percentage of college graduates in Listco's sales staff, also mentioned in the premise
if graduates_hypothesis >= graduates_premise:
    # check if the estimate of 'graduates_hypothesis' contradicts the percentage of graduates in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
