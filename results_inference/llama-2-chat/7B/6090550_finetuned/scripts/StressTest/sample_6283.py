average_score_premise = 82
tests_premise = 2
tests_hypothesis = 9

# the hypothesis talks about the average test score of Robin on more than 'tests_premise' tests
if tests_hypothesis <= tests_premise:
    # check if the hypothesis's estimate of 'tests_hypothesis' tests contradicts the premise
    label = "entailment"
else:
    # if the hypothesis's estimate of 'tests_hypothesis' tests is greater than 'tests_premise', we can infer the premise
    label = "contradiction"

print(label)
