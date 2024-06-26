gas_spew_premise = 0.17
gas_spew_hypothesis = 0.17

# the hypothesis mentions the percentage of more greenhouse gas spewed by tar sands oil compared to average crude oil, which is also mentioned in the premise
if gas_spew_hypothesis != gas_spew_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
