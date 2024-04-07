# Premise: Sandy gets 3 marks for each correct sum and loses 2 marks for each incorrect sum.
# Hypothesis: Sandy gets less than 3 marks for each correct sum and loses 2 marks for each incorrect sum.
# Golden Label: contradiction

correct_sum_premise = 3
correct_sum_hypothesis = 3
incorrect_sum_premise = -2
incorrect_sum_hypothesis = -2

# the hypothesis talks about the marks Sandy gets for correct and incorrect sums which is also mentioned in the premise
if correct_sum_hypothesis >= correct_sum_premise:
    # check if the hypothesis value contradicts the premise value for correct sums
    label = "contradiction"
elif incorrect_sum_hypothesis != incorrect_sum_premise:
    # check if the hypothesis value contradicts the premise value for incorrect sums
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

