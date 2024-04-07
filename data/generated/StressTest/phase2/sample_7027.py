# Premise: Dan leaves City A less than 520 minutes after Cara.
# Hypothesis: Dan leaves City A 120 minutes after Cara.
# Golden Label: neutral

leave_time_premise = 520
leave_time_hypothesis = 120

# the hypothesis talks about the time difference between Dan and Cara leaving City A, which is also mentioned in the premise
if leave_time_hypothesis > leave_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'leave_time_premise'
    label = "contradiction"
elif leave_time_hypothesis < leave_time_premise:
    # the premise gives only an estimate for the leaving time difference
    # any time difference less than 'leave_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value equal to the premise, it would be entailment
    label = "entailment"

print(label)

