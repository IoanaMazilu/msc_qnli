# Premise: Sandy gets less than 6 marks for each correct sum and loses 2 marks for each incorrect sum.
# Hypothesis: Sandy gets 3 marks for each correct sum and loses 2 marks for each incorrect sum.
# Golden Label: neutral

marks_per_correct_sum_premise = 6
marks_per_correct_sum_hypothesis = 3
marks_per_incorrect_sum_premise = 2
marks_per_incorrect_sum_hypothesis = 2

# the hypothesis refers to the number of marks gained or lost per sum, mentioned in the premise
if marks_per_correct_sum_hypothesis >= marks_per_correct_sum_premise:
    # check if the number of marks gained per correct sum in the hypothesis contradicts the estimate of less than 'marks_per_correct_sum_premise'
    label = "contradiction"
elif marks_per_incorrect_sum_hypothesis != marks_per_incorrect_sum_premise:
    # check if the number of marks lost per incorrect sum in the hypothesis contradicts the number of lost marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

