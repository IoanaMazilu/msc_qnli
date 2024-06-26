net_income_premise = 0.79
estimate_analysts_premise = 0.72
estimate_analysts_hypothesis = 0.72

# the hypothesis talks about the earnings per share expected by the analysts, which is also mentioned in the premise
if estimate_analysts_hypothesis != estimate_analysts_premise:
    # check if the earnings per share expected by the analysts in the hypothesis contradicts the earnings per share expected by the analysts from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
