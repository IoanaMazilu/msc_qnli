suresh_efficiency_premise = 35
suresh_efficiency_hypothesis = 25

# the hypothesis talks about the efficiency of Suresh compared to Kamal, referenced also in the premise
if suresh_efficiency_hypothesis >= suresh_efficiency_premise:
    # check if the hypothesis value contradicts the estimate of less than'suresh_efficiency_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the efficiency of Suresh
    # any efficiency less than'suresh_efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
