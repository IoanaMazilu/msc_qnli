pears_keith_premise = 47.0
pears_mike_premise = 12.0
pears_keith_gave_away_premise = 46.0
pears_mike_hypothesis = 13.0

# the hypothesis refers to the number of pears Mike has left, which is also mentioned in the premise
# compute the total number of pears Keith has and gave away
total_pears_keith_premise = pears_keith_premise + pears_keith_gave_away_premise

# compute the number of pears Mike has left
pears_mike_hypothesis = pears_mike_premise - total_pears_keith_premise

# check if the number of pears Mike has left in the hypothesis contradicts the number of pears Mike has left in the premise
if pears_mike_hypothesis!= pears_mike_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
