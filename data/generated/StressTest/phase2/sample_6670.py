# Premise: If Suresh is less than 35% more efficient than Kamal, he can complete the work in---days.
# Hypothesis: If Suresh is 25% more efficient than Kamal, he can complete the work in---days.
# Golden Label: neutral

suresh_efficiency_premise = 35
suresh_efficiency_hypothesis = 25

# the hypothesis talks about Suresh's efficiency compared to Kamal's, which is also mentioned in the premise
if suresh_efficiency_hypothesis > suresh_efficiency_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'suresh_efficiency_premise'
    label = "contradiction"
elif suresh_efficiency_hypothesis < suresh_efficiency_premise:
    # the premise gives an upper limit for Suresh's efficiency
    # a value less than 'suresh_efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to 'suresh_efficiency_premise', we can infer entailment
    label = "entailment"

print(label)

