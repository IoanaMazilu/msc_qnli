average_score_premise = 90
tests_premise = 4
tests_hypothesis = 3

# the hypothesis refers to the average score of the first 3 tests, which is also mentioned in the premise
if average_score_premise < tests_hypothesis:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
elif average_score_premise == tests_hypothesis:
    # if the average score in the hypothesis is equal to the average score in the premise, we can infer entailment
    label = "entailment"
else:
    # if the average score in the hypothesis is greater than the average score in the premise, we can infer neutral
    label = "neutral"

print(label)
