# Premise: In a recent election, Geoff received 1 percent of the 6,000 votes cast.
# Hypothesis: In a recent election, Geoff received less than 1 percent of the 6,000 votes cast.
# Golden Label: contradiction

votes_total_premise = 6000
votes_percent_premise = 1
votes_percent_hypothesis = 1

# the hypothesis refers to the percentage of votes Geoff received in the election mentioned in the premise
if votes_percent_hypothesis >= votes_percent_premise:
    # check if the percentage of votes for Geoff in the hypothesis contradicts the percentage of votes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

