sreedhar_work_days_premise = 75
sreedhar_work_days_hypothesis = 25

# the hypothesis talks about the number of days Sreedhar can do the work, referenced also in the premise
if sreedhar_work_days_hypothesis != sreedhar_work_days_premise:
    # check if the number of days Sreedhar can do the work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"

print(label)
