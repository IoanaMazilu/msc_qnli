correct_sum_mark_premise = 3
correct_sum_mark_hypothesis = 6
incorrect_sum_mark_premise = 2
incorrect_sum_mark_hypothesis = 2

# the hypothesis refers to the marks Sandy gets for correct and incorrect sums, which are also mentioned in the premise
if correct_sum_mark_premise >= correct_sum_mark_hypothesis:
    # check if the value of 'correct_sum_mark_hypothesis' contradicts the number of marks for correct sums in the premise
    label = "contradiction"
elif incorrect_sum_mark_hypothesis != incorrect_sum_mark_premise:
    # check if the number of marks for incorrect sums in the hypothesis contradicts the number of marks for incorrect sums reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the ones from the premise, we can infer entailment
    label = "entailment"

print(label)
