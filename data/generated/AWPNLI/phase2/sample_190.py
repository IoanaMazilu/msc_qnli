# Premise: Paul got a box of 479.0 crayons for his birthday and at the end of the school year, he only had 134.0 left.
# Hypothesis: 345.0 crayons had been lost or given away.
# Golden Label: entailment

crayons_start_premise = 479.0
crayons_end_premise = 134.0
crayons_lost_hypothesis = 345.0

# the hypothesis refers to the number of crayons lost or given away, which can be inferred from the premise
# compute the total number of crayons lost or given away in the premise
crayons_lost_premise = crayons_start_premise - crayons_end_premise
if crayons_lost_hypothesis != crayons_lost_premise:
    # check if the number of crayons lost or given away in the hypothesis contradicts the number of crayons lost or given away in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

