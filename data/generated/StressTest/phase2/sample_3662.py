# Premise: In a recent election, James received 5 percent of the 2,000 votes cast.
# Hypothesis: In a recent election, James received more than 5 percent of the 2,000 votes cast.
# Golden Label: contradiction

votes_premise = 2000
percentage_votes_premise = 5

votes_hypothesis = 2000
percentage_votes_hypothesis = 5

# the hypothesis refers to the same election and the same candidate's results
if votes_hypothesis != votes_premise:
    # check if the total votes cast in the hypothesis contradicts the total votes cast in the premise
    label = "contradiction"
elif percentage_votes_hypothesis <= percentage_votes_premise:
    # check if the percentage of votes in the hypothesis contradicts the percentage of votes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of votes
    # any percentage of votes greater than 'percentage_votes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

