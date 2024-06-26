suresh_efficiency_premise = 25
suresh_efficiency_hypothesis = 35

# the hypothesis refers to the efficiency of Suresh compared to Kamal mentioned in the premise
if suresh_efficiency_premise >= suresh_efficiency_hypothesis:
    # check if the efficiency of Suresh in the premise contradicts the estimate of less than'suresh_efficiency_hypothesis'
    label = "contradiction"
else:
    # if the efficiency of Suresh in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
