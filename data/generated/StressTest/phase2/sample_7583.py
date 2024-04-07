# Premise: What is the share of Sravan, if Sreedhar alone can do the work in 75 days?
# Hypothesis: What is the share of Sravan, if Sreedhar alone can do the work in less than 75 days?
# Golden Label: contradiction

work_days_sreedhar_premise = 75
work_days_sreedhar_hypothesis = 75

# the hypothesis refers to the number of days Sreedhar can do the work alone, mentioned in the premise
if work_days_sreedhar_hypothesis >= work_days_sreedhar_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

