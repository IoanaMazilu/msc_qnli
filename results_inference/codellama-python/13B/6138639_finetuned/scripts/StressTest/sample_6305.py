james_hours_premise = 41
james_hours_hypothesis = 61

# the hypothesis talks about the number of hours James worked last week, referenced also in the premise
if james_hours_hypothesis!= james_hours_premise:
    # check if the number of hours James worked in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
