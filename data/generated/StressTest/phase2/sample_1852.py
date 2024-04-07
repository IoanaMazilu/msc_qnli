# Premise: In a recent election, James received less than 35 percent of the 10000 votes cast.
# Hypothesis: In a recent election, James received 15 percent of the 10000 votes cast.
# Golden Label: neutral

percentage_votes_premise = 35
percentage_votes_hypothesis = 15
total_votes_premise = 10000
total_votes_hypothesis = 10000

# the hypothesis provides a specific value for the percentage of votes James received, which is also mentioned in the premise
if percentage_votes_hypothesis >= percentage_votes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_votes_premise'
    label = "contradiction"
elif total_votes_hypothesis != total_votes_premise:
    # check if the total number of votes in the hypothesis contradicts the total number of votes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of votes
    # any percentage of votes less than 'percentage_votes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

