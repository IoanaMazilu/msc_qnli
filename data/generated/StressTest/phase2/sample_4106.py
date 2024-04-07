# Premise: Alex joined him 8 months later, investing Rs.
# Hypothesis: Alex joined him less than 8 months later, investing Rs.
# Golden Label: contradiction

joining_time_premise = 8
joining_time_hypothesis = 8

# the hypothesis refers to the time Alex joined, which is also mentioned in the premise
if joining_time_hypothesis >= joining_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

