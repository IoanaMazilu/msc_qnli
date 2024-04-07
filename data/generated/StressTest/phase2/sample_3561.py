# Premise: In a recent election, Geoff received 15 percent of the 6,000 votes cast.
# Hypothesis: In a recent election, Geoff received less than 75 percent of the 6,000 votes cast.
# Golden Label: entailment

total_votes_premise = 6000
geoff_votes_percentage_premise = 15 / 100
geoff_votes_percentage_hypothesis = 75 / 100

# the hypothesis refers to the percentage of votes Geoff received, which is also mentioned in the premise
if geoff_votes_percentage_hypothesis <= geoff_votes_percentage_premise:
    # check if the 'geoff_votes_percentage_hypothesis' contradicts the percentage of Geoff's votes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

