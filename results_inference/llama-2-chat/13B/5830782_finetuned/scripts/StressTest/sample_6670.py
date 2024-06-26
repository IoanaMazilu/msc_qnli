suresh_efficiency_premise = 35
suresh_efficiency_hypothesis = 25

# the hypothesis talks about the efficiency of Suresh compared to Kamal, referenced also in the premise
if suresh_efficiency_hypothesis > suresh_efficiency_premise:
    # check if the hypothesis value contradicts the estimate of'suresh_efficiency_premise'
    label = "contradiction"
elif suresh_efficiency_hypothesis < suresh_efficiency_premise:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    # but we cannot explicitly entail it from the premise, so the relation is neutral
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it is an entailment
    label = "entailment"

print(label)
