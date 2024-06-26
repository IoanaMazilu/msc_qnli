suresh_kamal_efficiency_premise = 35
suresh_kamal_efficiency_hypothesis = 25
work_days_premise = 35
work_days_hypothesis = 35

# the hypothesis talks about the efficiency of Suresh compared to Kamal, which is also mentioned in the premise
if suresh_kamal_efficiency_hypothesis < suresh_kamal_efficiency_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif suresh_kamal_efficiency_hypothesis == suresh_kamal_efficiency_premise:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, we can infer contradiction
    label = "contradiction"

print(label)
