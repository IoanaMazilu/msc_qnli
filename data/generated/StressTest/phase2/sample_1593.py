# Premise: Jane had an average of 87 on his first 7 tests.
# Hypothesis: Jane had an average of more than 17 on his first 7 tests.
# Golden Label: entailment

average_premise = 87
average_hypothesis = 17
tests_count = 7

# the hypothesis talks about the average score of Jane's tests, which is also mentioned in the premise
if average_hypothesis >= average_premise:
    # check if the hypothesis value contradicts the given average score in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise's average score, we can infer entailment
    label = "entailment"

print(label)

