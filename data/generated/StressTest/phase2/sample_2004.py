# Premise: Mary played the game, getting at least one score of each of 1, 2, 3 and 4 and never getting the same score in consecutive steps.
# Hypothesis: Mary played the game, getting at least one score of each of less than 4, 2, 3 and 4 and never getting the same score in consecutive steps.
# Golden Label: entailment

score_premise = [1, 2, 3, 4]
score_hypothesis = [4, 2, 3, 4]

# the hypothesis talks about the scores Mary got in the game, which is also referred in the premise
if score_premise != score_hypothesis:
    # check if the scores in the hypothesis contradict the scores Mary got in the premise
    label = "contradiction"
else:
    # the premise and hypothesis both state that Mary never got the same score in consecutive steps
    label = "entailment"

print(label)

