# Premise: Henry runs the second leg of the course in 7 seconds.
# Hypothesis: Henry runs the second leg of the course in 6 seconds.
# Golden Label: contradiction

second_leg_time_premise = 7
second_leg_time_hypothesis = 6

# the hypothesis refers to the time Henry runs the second leg of the course, which is also mentioned in the premise
if second_leg_time_hypothesis != second_leg_time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the times are the same, we can infer entailment
    label = "entailment"

print(label)

