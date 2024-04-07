# Premise: What must be Robin's score on a 10 th test for his average score on the 10 tests to be 83?
# Hypothesis: What must be Robin's score on a less than 70 th test for his average score on the 10 tests to be 83?
# Golden Label: entailment

test_number_premise = 10
test_number_hypothesis = 70
average_score_premise = 83
average_score_hypothesis = 83

# the hypothesis refers to the test number and average score mentioned in the premise
if test_number_hypothesis >= test_number_premise:
    # check if the hypothesis value contradicts the test number in the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

