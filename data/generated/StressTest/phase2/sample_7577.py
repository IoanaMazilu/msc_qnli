# Premise: Sreedhar and Sravan together can do a work in 25 days.
# Hypothesis: Sreedhar and Sravan together can do a work in more than 25 days.
# Golden Label: contradiction

work_days_premise = 25
work_days_hypothesis = 25

# the hypothesis refers to the number of days needed by Sreedhar and Sravan to finish a work, mentioned also in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days stated in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis is greater than the number of days stated in the premise
    # we can infer entailment
    label = "entailment"

print(label)

