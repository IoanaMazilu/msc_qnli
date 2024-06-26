investment_premise = 20000
investment_hypothesis = 20000
duration_premise = 6
duration_hypothesis = 7

# the hypothesis refers to the amount invested by Rick mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the amount invested by Rick in the premise
    label = "contradiction"
elif duration_hypothesis >= duration_premise:
    # check if the duration in the hypothesis contradicts the duration reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
