# Premise: Sandy gets less than 4 marks for each correct sum and loses 2 marks for each incorrect sum.
# Hypothesis: Sandy gets 3 marks for each correct sum and loses 2 marks for each incorrect sum.
# Golden Label: neutral

correct_marks_premise = 4
correct_marks_hypothesis = 3
incorrect_marks_premise = 2
incorrect_marks_hypothesis = 2

# the hypothesis talks about the number of marks Sandy gets for correct sums and loses for incorrect sums, referenced also in the premise
if correct_marks_hypothesis >= correct_marks_premise:
    # check if the number of marks for correct sums in the hypothesis contradicts the estimate of less than 'correct_marks_premise'
    label = "contradiction"
elif incorrect_marks_hypothesis != incorrect_marks_premise:
    # check if the number of lost marks for incorrect sums in the hypothesis contradicts the number of lost marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

