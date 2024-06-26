correct_sum_marks_premise = 3
incorrect_sum_marks_premise = -2
correct_sum_marks_hypothesis = 8
incorrect_sum_marks_hypothesis = -2

# the hypothesis talks about the marks Sandy gets for correct and incorrect sums
# these are same aspects mentioned in the premise
if correct_sum_marks_hypothesis != correct_sum_marks_premise:
    # check if the marks for correct sums in the hypothesis contradicts the marks for correct sums in the premise
    label = "contradiction"
elif incorrect_sum_marks_hypothesis != incorrect_sum_marks_premise:
    # check if the marks for incorrect sums in the hypothesis contradicts the marks for incorrect sums in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
