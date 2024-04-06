# Premise: Third-placed Valencia lost ground after being held to a 1-1 draw at Sporting Gijon, needing a second-half equalizer from Juan Mata.
# Hypothesis: Third-placed Valencia lose ground following 1-1 draw away to Sporting Gijon.
# Golden Label: entailment

valencia_score_premise = 1
gijon_score_premise = 1
valencia_score_hypothesis = 1
gijon_score_hypothesis = 1

# the hypothesis mentions the final score of the Valencia vs Sporting Gijon game, which is also mentioned in the premise
if valencia_score_hypothesis != valencia_score_premise:
    # check if the Valencia score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif gijon_score_hypothesis != gijon_score_premise:
    # check if the Sporting Gijon score from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)

