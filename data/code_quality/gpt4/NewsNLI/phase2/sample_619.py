killings_premise = 20
killings_hypothesis = 20

# the hypothesis mentions the number of suspected smugglers killed by police in India, which is also mentioned in the premise
if killings_hypothesis != killings_premise:
    # check if the number of killings in the hypothesis contradicts the number of killings reported in the premise
    label = "contradiction"
else:
    # if the number of killings in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
