# Premise: In a recent election, Geoff received 1 percent of the 6,000 votes cast.
# Hypothesis: In a recent election, Geoff received 8 percent of the 6,000 votes cast.
# Golden Label: contradiction

total_votes_premise = 6000
geoff_votes_percentage_premise = 1
geoff_votes_percentage_hypothesis = 8

# the hypothesis talks about the percentage of votes received by Geoff in an election, also mentioned in the premise
if geoff_votes_percentage_hypothesis == geoff_votes_percentage_premise:
    # check if the percentage of votes Geoff received in the hypothesis matches the percentage provided in the premise
    label = "entailment"
elif geoff_votes_percentage_hypothesis < geoff_votes_percentage_premise:
    # check if the percentage of votes Geoff received in the hypothesis contradicts the percentage provided in the premise
    label = "contradiction"
else:
    # the premise provides a specific percentage of votes Geoff received
    # any percentage greater than 'geoff_votes_percentage_premise' contradicts the premise
    label = "contradiction"

print(label)

