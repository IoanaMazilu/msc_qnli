# Premise: Kerri leaves City A 60 minutes after Jim.
# Hypothesis: Kerri leaves City A more than 60 minutes after Jim.
# Golden Label: contradiction

leave_time_premise = 60
leave_time_hypothesis = 60

# the hypothesis mentions the time difference between when Kerri and Jim leave City A, which is also mentioned in the premise
if leave_time_hypothesis > leave_time_premise:
    # check if the hypothesis time difference contradicts the time difference stated in the premise
    label = "contradiction"
elif leave_time_hypothesis == leave_time_premise:
    # check if the time difference in the hypothesis is exactly the same as in the premise
    label = "entailment"
else:
    # the premise gives only an exact time difference
    # any time difference less than 'leave_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

