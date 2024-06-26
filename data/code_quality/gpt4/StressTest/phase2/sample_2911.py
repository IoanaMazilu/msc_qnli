marks_correct_sum_premise = 8
marks_correct_sum_hypothesis = 3
marks_incorrect_sum_premise = 2
marks_incorrect_sum_hypothesis = 2

# the hypothesis talks about the marks Sandy gets for correct and incorrect sums, referenced also in the premise
if marks_correct_sum_hypothesis >= marks_correct_sum_premise:
    # check if the hypothesis value contradicts the estimate of less than 'marks_correct_sum_premise'
    label = "contradiction"
elif marks_incorrect_sum_hypothesis != marks_incorrect_sum_premise:
    # check if the number of lost marks for incorrect sums in the hypothesis contradicts the number of lost marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
