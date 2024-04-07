# Premise: If Geoff needed exactly 3000 more votes to win the election, what is the value of x?
# Hypothesis: If Geoff needed exactly less than 6000 more votes to win the election, what is the value of x?
# Golden Label: entailment

votes_needed_premise = 3000
votes_needed_hypothesis = 6000

# the hypothesis talks about the number of votes needed for Geoff to win the election, referenced also in the premise
if votes_needed_hypothesis <= votes_needed_premise:
    # check if the hypothesis value contradicts the exact number of 'votes_needed_premise'
    label = "contradiction"
elif votes_needed_hypothesis != votes_needed_premise:
    # any number of votes needed other than 'votes_needed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

