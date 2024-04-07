# Premise: In a recent election, James received more than 4 percent of the 2,000 votes cast.
# Hypothesis: In a recent election, James received 5 percent of the 2,000 votes cast.
# Golden Label: neutral

percentage_votes_premise = 4
votes_total_premise = 2000
percentage_votes_hypothesis = 5
votes_total_hypothesis = 2000

# the hypothesis talks about the votes James received in an election, referenced also in the premise
if votes_total_hypothesis != votes_total_premise:
    # check if the total number of votes in the hypothesis contradicts the total number of votes in the premise
    label = "contradiction"
elif percentage_votes_hypothesis <= percentage_votes_premise:
    # check if the percentage of votes in the hypothesis contradicts the estimate of more than 'percentage_votes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of votes
    # any percentage of votes greater than 'percentage_votes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

