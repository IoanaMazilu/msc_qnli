# Premise: Dan leaves City A more than 20 minutes after Cara.
# Hypothesis: Dan leaves City A 90 minutes after Cara.
# Golden Label: neutral

leave_time_difference_premise = 20
leave_time_difference_hypothesis = 90

# the hypothesis talks about the time difference between when Dan and Cara leave City A, also mentioned in the premise
if leave_time_difference_hypothesis <= leave_time_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'leave_time_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'leave_time_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

