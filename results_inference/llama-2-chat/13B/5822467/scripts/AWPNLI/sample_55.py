gems_premise = 5155.0
diamonds_premise = 45.0
rubies_premise = gems_premise - diamonds_premise

hypothesis_gems = 5108.0
hypothesis_diamonds = 0.0

# compute the total number of rubies in the hypothesis
rubies_hypothesis = hypothesis_gems - hypothesis_diamonds

# check if the number of rubies in the hypothesis contradicts the number of rubies in the premise
if rubies_hypothesis!= rubies_premise:
    label = "contradiction"
elif hypothesis_gems!= gems_premise or hypothesis_diamonds!= diamonds_premise:
    # check if the number of gems or diamonds in the hypothesis contradicts the number of gems or diamonds in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
