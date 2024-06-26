percentage_to_pass_premise = 70
percentage_to_pass_hypothesis = 30
marks_obtained_hypothesis = 110
marks_obtained_premise = 110
marks_failed_by_hypothesis = 100
marks_failed_by_premise = 100

# the hypothesis refers to the percentage needed to pass and 
# the marks obtained by Henry in the exam, as well as the marks he failed by, all of which are also mentioned in the premise
if percentage_to_pass_hypothesis > percentage_to_pass_premise:
    # check if the percentage to pass in the hypothesis contradicts the percentage to pass in the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the marks obtained by Henry in the hypothesis contradicts the marks obtained by Henry in the premise
    label = "contradiction"
elif marks_failed_by_hypothesis != marks_failed_by_premise:
    # check if the marks Henry failed by in the hypothesis contradicts the marks Henry failed by in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
