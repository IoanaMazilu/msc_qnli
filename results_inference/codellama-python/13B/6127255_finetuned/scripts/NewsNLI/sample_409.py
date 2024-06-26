risk_increase_premise = 0.44
risk_increase_hypothesis = 0.44

# the hypothesis mentions the risk increase of a teen driver having a crash due to passengers, which is also mentioned in the premise
if risk_increase_hypothesis!= risk_increase_premise:
    # check if the risk increase in the hypothesis contradicts the risk increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
