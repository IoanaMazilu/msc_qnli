total_gems_premise = 5155
diamonds_premise = 45
rubies_hypothesis = 5108

# the hypothesis refers to the number of rubies in the treasure, which is also mentioned in the premise
# compute the total number of rubies in the premise
total_rubies_premise = total_gems_premise - diamonds_premise
if total_rubies_hypothesis!= total_rubies_premise:
    # check if the number of rubies in the hypothesis contradicts the number of rubies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
