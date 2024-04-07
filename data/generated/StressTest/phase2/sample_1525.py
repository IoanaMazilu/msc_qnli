# Premise: In a recent election, Geoff received less than 7 percent of the 6,000 votes cast.
# Hypothesis: In a recent election, Geoff received 1 percent of the 6,000 votes cast.
# Golden Label: neutral

percent_votes_premise = 7
votes_premise = 6000
percent_votes_hypothesis = 1
votes_hypothesis = 6000

# the hypothesis talks about the percentage of votes Geoff received in a recent election, referenced also in the premise
if percent_votes_hypothesis >= percent_votes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percent_votes_premise'
    label = "contradiction"
elif votes_hypothesis != votes_premise:
    # check if the number of total votes in the hypothesis contradicts the number of total votes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of votes 
    # any percentage less than 'percent_votes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

