votes_total_premise = 10000
votes_total_hypothesis = 10000
votes_percentage_premise = 15
votes_percentage_hypothesis = 15

# the hypothesis talks about the percentage of votes James received in a recent election, referenced also in the premise
if votes_percentage_hypothesis <= votes_percentage_premise and votes_total_hypothesis == votes_total_premise:
    # check if the hypothesis contradicts the percentage of votes James received according to the premise
    # also check if the total number of votes cast in the hypothesis is the same as in the premise
    label = "contradiction"
elif votes_total_hypothesis != votes_total_premise:
    # check if the total number of votes cast in the hypothesis contradicts the amount stated in the premise
    label = "contradiction"
else:
    # any percentage of votes greater than 'votes_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
