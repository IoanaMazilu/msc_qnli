# Premise: Sreedhar and Sravan together can do a work in 25 days.
# Hypothesis: Sreedhar and Sravan together can do a work in less than 65 days.
# Golden Label: entailment

work_days_premise = 25
work_days_hypothesis = 65

# the hypothesis refers to the number of days Sreedhar and Sravan would take to finish a work, as mentioned in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

