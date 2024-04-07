# Premise: In a recent election, Geoff received 15 percent of the 6,000 votes cast.
# Hypothesis: In a recent election, Geoff received 35 percent of the 6,000 votes cast.
# Golden Label: contradiction

votes_premise = 6000
votes_hypothesis = 6000
percentage_premise = 15
percentage_hypothesis = 35

# the hypothesis refers to the same election and number of votes mentioned in the premise
if votes_hypothesis != votes_premise:
    # check if the number of votes in the hypothesis contradicts the number of votes in the premise
    label = "contradiction"
elif percentage_hypothesis < percentage_premise:
    # check if the percentage of votes in the hypothesis contradicts the percentage of votes in the premise
    label = "contradiction"
elif percentage_hypothesis > percentage_premise:
    # check if the percentage of votes in the hypothesis contradicts the percentage of votes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

