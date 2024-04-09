rank_premise = 75
rank_hypothesis = 15

# the hypothesis refers to the rank of Nitin in the class
if rank_hypothesis < rank_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif rank_premise!= rank_hypothesis:
    # check if the rank in the hypothesis contradicts the rank reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
