premise_gems = 5155.0
premise_diamonds = 45.0
premise_rubies = premise_gems - premise_diamonds

hypothesis_rubies = 5108.0

# the hypothesis refers to the number of rubies, which are also mentioned in the premise
# compute the total number of rubies in the premise
total_rubies_premise = premise_rubies

if total_rubies_hypothesis!= total_rubies_premise:
    # check if the number of rubies in the hypothesis contradicts the number of rubies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
