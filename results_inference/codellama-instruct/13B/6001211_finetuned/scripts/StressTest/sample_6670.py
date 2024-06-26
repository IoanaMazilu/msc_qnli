suresh_efficiency_premise = 35
suresh_efficiency_hypothesis = 25

# the hypothesis refers to the efficiency of Suresh compared to Kamal, also mentioned in the premise
if suresh_efficiency_hypothesis >= suresh_efficiency_premise:
    # check if the hypothesis value contradicts the estimate of less than'suresh_efficiency_premise'
    label = "contradiction"
elif suresh_efficiency_hypothesis < suresh_efficiency_premise:
    # the premise gives only an estimate for the efficiency of Suresh
    # any efficiency less than'suresh_efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
