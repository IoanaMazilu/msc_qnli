# Premise: Two men, Vikas and Vishal, working separately can mow a field in more than 1 and 12 hours respectively.
# Hypothesis: Two men, Vikas and Vishal, working separately can mow a field in 8 and 12 hours respectively.
# Golden Label: neutral

vikas_time_premise = 1
vishal_time_premise = 12
vikas_time_hypothesis = 8
vishal_time_hypothesis = 12

# the hypothesis talks about the time taken by Vikas and Vishal to mow a field, which is also mentioned in the premise
if vikas_time_hypothesis <= vikas_time_premise:
    # check if the time taken by Vikas in the hypothesis contradicts the estimate given in the premise
    label = "contradiction"
elif vishal_time_hypothesis != vishal_time_premise:
    # check if the time taken by Vishal in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif vikas_time_hypothesis > vikas_time_premise and vishal_time_hypothesis == vishal_time_premise:
    # the premise gives an estimate for the time taken by Vikas, thus any time more than 'vikas_time_premise' is consistent with the premise
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

