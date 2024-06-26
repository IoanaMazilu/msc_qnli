required_percentage_premise = 50
required_percentage_hypothesis = 80
marks_obtained_premise = 50
marks_obtained_hypothesis = 50
marks_failed_by_premise = 10
marks_failed_by_hypothesis = 10

# the hypothesis refers to the percentage required to pass, and the marks obtained by Paul, which are also mentioned in the premise
if (required_percentage_premise != required_percentage_hypothesis) or (marks_obtained_premise != marks_obtained_hypothesis) or (marks_failed_by_premise != marks_failed_by_hypothesis):
    # check if the required percentage, the obtained marks, or the marks failed by in the hypothesis contradict the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
