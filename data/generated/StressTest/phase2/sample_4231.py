# Premise: Dan leaves City A less than 420 minutes after Cara.
# Hypothesis: Dan leaves City A 120 minutes after Cara.
# Golden Label: neutral

leave_time_premise = 420
leave_time_hypothesis = 120

# the hypothesis refers to the time difference between Dan's and Cara's departure from City A
if leave_time_hypothesis >= leave_time_premise:
    # check if the time difference in the hypothesis contradicts the premise
    label = "contradiction"
elif leave_time_hypothesis < leave_time_premise:
    # if the time difference in the hypothesis is less than in the premise, it can be entailed from the premise
    label = "entailment"

print(label)

