# Premise: If Suresh is less than 65% more efficient than Kamal, he can complete the work in---days.
# Hypothesis: If Suresh is 25% more efficient than Kamal, he can complete the work in---days.
# Golden Label: neutral

suresh_efficiency_premise = 65
suresh_efficiency_hypothesis = 25

# the hypothesis talks about the efficiency of Suresh compared to Kamal, referenced also in the premise 
if suresh_efficiency_hypothesis > suresh_efficiency_premise:
    # check if the hypothesis value contradicts the estimate of less than 'suresh_efficiency_premise'
    label = "contradiction"
else:
    # the premise gives an upper limit for the efficiency of Suresh
    # any efficiency less than 'suresh_efficiency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

