# Premise: What is the share of Sravan, if Sreedhar alone can do the work in 75 days?
# Hypothesis: What is the share of Sravan, if Sreedhar alone can do the work in more than 25 days?
# Golden Label: entailment

work_days_sreedhar_premise = 75
work_days_sreedhar_hypothesis = 25

# the hypothesis refers to the number of days Sreedhar can do the work, mentioned also in the premise
if work_days_sreedhar_hypothesis >= work_days_sreedhar_premise:
    # check if the estimate of 'work_days_sreedhar_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif work_days_sreedhar_hypothesis < work_days_sreedhar_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

