# Premise: In a recent election, James received 15 percent of the 10000 votes cast.
# Hypothesis: In a recent election, James received less than 35 percent of the 10000 votes cast.
# Golden Label: entailment

votes_cast_premise = 10000
votes_cast_hypothesis = 10000
james_votes_premise = 15/100 * votes_cast_premise
james_votes_hypothesis = 35/100 * votes_cast_hypothesis

# the hypothesis refers to the percentage of votes James received in an election mentioned in the premise
if james_votes_hypothesis <= james_votes_premise:
    # check if the hypothesis estimate contradicts the percentage of votes James received in the premise
    label = "contradiction"
elif votes_cast_hypothesis != votes_cast_premise:
    # check if the number of total votes in the hypothesis contradicts the number of total votes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

