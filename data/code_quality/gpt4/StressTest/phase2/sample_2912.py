correct_sum_premise = 3
incorrect_sum_premise = -2
correct_sum_hypothesis = 7
incorrect_sum_hypothesis = -2

# the hypothesis talks about the marks Sandy gets for correct/incorrect sums, which is also mentioned in the premise
if correct_sum_hypothesis != correct_sum_premise:
    # check if the marks for correct sum in the hypothesis contradicts the marks for correct sum mentioned in the premise
    label = "contradiction"
elif incorrect_sum_hypothesis != incorrect_sum_premise:
    # check if the marks for incorrect sum in the hypothesis contradicts the marks for incorrect sum mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
