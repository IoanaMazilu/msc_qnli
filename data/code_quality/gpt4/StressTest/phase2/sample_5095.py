avg_raise_premise = 5
avg_raise_hypothesis = 3

# the hypothesis talks about the points Jerry wants to raise his average by, also referenced in the premise
if avg_raise_hypothesis >= avg_raise_premise:
    # check if the hypothesis value contradicts the estimate of less than 'avg_raise_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
