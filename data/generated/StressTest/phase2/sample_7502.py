# Premise: Pat runs at 9 miles per hour, and Cara runs at 5 miles per hour.
# Hypothesis: Pat runs at more than 9 miles per hour, and Cara runs at 5 miles per hour.
# Golden Label: contradiction

pat_speed_premise = 9
pat_speed_hypothesis = 9
cara_speed_premise = 5
cara_speed_hypothesis = 5

# the hypothesis refers to the speeds of Pat and Cara mentioned in the premise
if pat_speed_hypothesis != pat_speed_premise:
    # checking if the speed of Pat in the hypothesis contradicts the speed of Pat in the premise
    label = "contradiction"
elif cara_speed_hypothesis != cara_speed_premise:
    # checking if the speed of Cara in the hypothesis contradicts the speed of Cara in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

