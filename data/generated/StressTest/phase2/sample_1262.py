# Premise: Two men, Vikas and Vishal, working separately can mow a field in 8 and 12 hours respectively.
# Hypothesis: Two men, Vikas and Vishal, working separately can mow a field in more than 8 and 12 hours respectively.
# Golden Label: contradiction

vikas_time_premise = 8
vishal_time_premise = 12
vikas_time_hypothesis = 8
vishal_time_hypothesis = 12

# the hypothesis refers to the time taken by Vikas and Vishal to mow a field, which is also mentioned in the premise
if vikas_time_hypothesis < vikas_time_premise or vishal_time_hypothesis < vishal_time_premise:
    # check if the time given in the hypothesis contradicts the time given in the premise
    label = "contradiction"
else:
    # the premise gives exact time for both Vikas and Vishal, but the hypothesis only estimates that it will take more than the given time
    # the estimate is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)

