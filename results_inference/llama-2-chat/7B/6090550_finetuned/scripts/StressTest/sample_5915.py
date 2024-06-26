 score_premise = 90
tests_premise = 3
tests_hypothesis = 4

# the hypothesis refers to the average score of Jerry on the first 3-4 tests, which is also mentioned in the premise
if tests_hypothesis <= tests_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif score_premise!= 90:
    # check if the average score of Jerry in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
