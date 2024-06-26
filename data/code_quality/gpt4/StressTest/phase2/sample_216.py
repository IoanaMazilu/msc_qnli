correct_sum_premise = 3
correct_sum_hypothesis = 4
incorrect_sum_premise = 2
incorrect_sum_hypothesis = 2

# the hypothesis refers to the marks for correct and incorrect sums mentioned in the premise
if correct_sum_premise >= correct_sum_hypothesis:
    # check if the estimate of 'correct_sum_hypothesis' contradicts the number of marks for correct sum in the premise
    label = "contradiction"
elif incorrect_sum_hypothesis != incorrect_sum_premise:
    # check if the number of marks lost for incorrect sum in the hypothesis contradicts the number of marks lost reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
