average_score_premise = 82
tests_premise = 9
tests_hypothesis = 2

# the hypothesis refers to the average score on more than 2 tests, which is also mentioned in the premise
if average_score_premise <= tests_hypothesis:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average score in the hypothesis does not contradict the average score in the premise, we can infer entailment
    label = "entailment"

print(label)
