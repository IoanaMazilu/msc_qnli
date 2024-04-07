# Premise: Kamal will complete work in 20 days.
# Hypothesis: Kamal will complete work in 50 days.
# Golden Label: contradiction

work_completion_time_premise = 20
work_completion_time_hypothesis = 50

# the hypothesis mentions the number of days Kamal will take to complete the work, which is also mentioned in the premise
if work_completion_time_hypothesis != work_completion_time_premise:
    # check if the number of days in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

