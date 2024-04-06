# Premise: The House version of the budget passed by a margin of 233-196 in a virtual party-line vote.
# Hypothesis: Budget passes 233-196 in party-line vote ; no House Republican voted in favor.
# Golden Label: neutral

votes_for_premise = 233
votes_against_premise = 196

votes_for_hypothesis = 233
votes_against_hypothesis = 196

# the hypothesis mentions the number of votes for and against the budget, which are also mentioned in the premise
if votes_for_hypothesis != votes_for_premise:
    # check if the number of votes for from the hypothesis contradicts the number in the premise
    label = "contradiction"
elif votes_against_hypothesis != votes_against_premise:
    # check if the number of votes against from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis vote numbers do not contradict the premise vote numbers, we can infer entailment
    label = "entailment"

print(label)

