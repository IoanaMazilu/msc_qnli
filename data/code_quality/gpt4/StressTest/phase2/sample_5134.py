votes_needed_premise = 6000
votes_needed_hypothesis = 3000

# the hypothesis refers to the number of votes needed for Geoff to win the election, also mentioned in the premise
if votes_needed_hypothesis >= votes_needed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'votes_needed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of votes needed
    # any number of votes less than 'votes_needed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
