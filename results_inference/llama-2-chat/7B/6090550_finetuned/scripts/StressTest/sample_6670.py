suresh_efficiency_premise = 35
suresh_efficiency_hypothesis = 25
work_days_premise = 1
work_days_hypothesis = 1

# the hypothesis talks about the efficiency of Suresh compared to Kamal, also mentioned in the premise
if suresh_efficiency_hypothesis >= suresh_efficiency_premise:
    # check if the hypothesis value contradicts the estimate of less than'suresh_efficiency_premise'
    label = "contradiction"
elif suresh_efficiency_hypothesis < suresh_efficiency_premise:
    # the premise gives only an estimate for the efficiency of Suresh
    # any efficiency percentage less than'suresh_efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is exactly equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
