# Premise: The Super Eagles had earlier booked their place in the final with a convincing 4-1 win over Mali in Durban.
# Hypothesis: Nigeria thrashed Mali 4-1 in Durban to seal place in final.
# Golden Label: entailment

score_premise = 4-1
score_hypothesis = 4-1

# the hypothesis mentions the score of the game, which is also mentioned in the premise
if score_hypothesis != score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the score in the hypothesis does not contradict the score in the premise, we can infer entailment
    label = "entailment"

print(label)

