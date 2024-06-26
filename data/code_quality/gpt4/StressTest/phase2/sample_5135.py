votes_needed_premise = 3000
votes_needed_hypothesis = 3000

# the hypothesis refers to the number of votes Geoff needed to win the election, which is also mentioned in the premise
if votes_needed_hypothesis != votes_needed_premise:
    # check if the number of votes in the hypothesis contradicts the number of votes mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
