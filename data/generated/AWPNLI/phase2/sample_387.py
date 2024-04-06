# Premise: Keith picked 47.0 pears, and Mike picked 12.0 pears from the pear tree and Keith gave away 46.0 pears.
# Hypothesis: Mike has 10.0 pears left.
# Golden Label: contradiction

pears_keith_premise = 47.0
pears_mike_premise = 12.0
pears_keith_gave_away_premise = 46.0
pears_mike_hypothesis = 10.0

# the hypothesis refers to the number of pears Mike has, which is also mentioned in the premise
# since Keith gave away 46 pears, we can assume that he gave them to Mike
# so, compute the total number of pears Mike has in the premise
total_pears_mike_premise = pears_mike_premise + pears_keith_gave_away_premise
if pears_mike_hypothesis != total_pears_mike_premise:
    # check if the number of pears Mike has in the hypothesis contradicts the number of pears from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

