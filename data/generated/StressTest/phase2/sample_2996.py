# Premise: Sandy gets 3 marks for each correct sum and loses 2 marks for each incorrect sum.
# Hypothesis: Sandy gets more than 3 marks for each correct sum and loses 2 marks for each incorrect sum.
# Golden Label: contradiction

correct_sum_marks_premise = 3
incorrect_sum_marks_premise = -2
correct_sum_marks_hypothesis = 3
incorrect_sum_marks_hypothesis = -2

# the hypothesis refers to the number of marks Sandy gets for correct and incorrect sums, mentioned in the premise
if correct_sum_marks_hypothesis <= correct_sum_marks_premise:
    # check if the hypothesis value contradicts the number of marks for correct sums reported in the premise
    label = "contradiction"
elif incorrect_sum_marks_hypothesis != incorrect_sum_marks_premise:
    # check if the number of marks for incorrect sums in the hypothesis contradicts the number of marks for incorrect sums reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

