# Premise: Sandy gets 3 marks for each correct sum and loses 2 marks for each incorrect sum.
# Hypothesis: Sandy gets 6 marks for each correct sum and loses 2 marks for each incorrect sum.
# Golden Label: contradiction

correct_sum_premise = 3
correct_sum_hypothesis = 6
incorrect_sum_premise = 2
incorrect_sum_hypothesis = 2

# the hypothesis talks about the marks Sandy gets and loses for correct and incorrect sums, respectively
if correct_sum_hypothesis != correct_sum_premise:
    # check if the marks for correct sum in the hypothesis contradicts the marks for correct sum mentioned in the premise
    label = "contradiction"
elif incorrect_sum_hypothesis != incorrect_sum_premise:
    # check if the marks for incorrect sum in the hypothesis contradicts the marks for incorrect sum mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

