# Premise: Sreedhar and Sravan together can do a work in 25 days.
# Hypothesis: Sreedhar and Sravan together can do a work in 35 days.
# Golden Label: contradiction

work_days_premise = 25
work_days_hypothesis = 35

# The hypothesis refers to the number of days Sreedhar and Sravan can do a work, which is also mentioned in the premise
if work_days_hypothesis != work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)

