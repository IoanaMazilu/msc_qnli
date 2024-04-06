# Premise: Ohio State got the nod after stomping the Wisconsin Badgers 59-0 in the Big Ten championship game.
# Hypothesis: Ohio State jumped into the Final Four by drubbing Wisconsin in the Big Ten championship game.
# Golden Label: entailment

score_premise = 59
score_hypothesis = None

# the hypothesis does not mention the score, so there cannot be a contradiction based on the score
# however, the hypothesis does not provide enough information to entail the premise fully
label = "neutral"

print(label)

