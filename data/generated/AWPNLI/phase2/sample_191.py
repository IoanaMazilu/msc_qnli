# Premise: Paul got a box of 479.0 crayons for his birthday and at the end of the school year, he only had 134.0 left.
# Hypothesis: 340.0 crayons had been lost or given away.
# Golden Label: contradiction

crayons_beginning_premise = 479.0
crayons_end_premise = 134.0
crayons_lost_or_given_away_hypothesis = 340.0

# the hypothesis refers to the number of crayons lost or given away, which can be inferred from the premise
# compute the number of crayons lost or given away in the premise
crayons_lost_or_given_away_premise = crayons_beginning_premise - crayons_end_premise
if crayons_lost_or_given_away_hypothesis != crayons_lost_or_given_away_premise:
    # check if the number of crayons lost or given away in the hypothesis contradicts the number computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

