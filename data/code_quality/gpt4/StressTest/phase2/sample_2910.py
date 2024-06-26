correct_sum_premise = 3
correct_sum_hypothesis = 8
incorrect_sum_premise = 2
incorrect_sum_hypothesis = 2

# the hypothesis talks about the number of marks Sandy gets or loses for each correct or incorrect sum, referenced also in the premise
if correct_sum_hypothesis <= correct_sum_premise:
    # check if the hypothesis value contradicts the premise value for each correct sum
    label = "contradiction"
elif incorrect_sum_hypothesis != incorrect_sum_premise:
    # check if the number of marks Sandy loses for each incorrect sum in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
