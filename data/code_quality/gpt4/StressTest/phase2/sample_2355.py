total_cars_premise = 280
ratio_hybrid_tajima_non_hybrid_frank_premise = 5/4
ratio_hybrid_tajima_non_hybrid_frank_hypothesis = 4/4

# the hypothesis refers to the ratio of hybrid Tajima's to non hybrid Franks and the total number of automobiles
if ratio_hybrid_tajima_non_hybrid_frank_hypothesis >= ratio_hybrid_tajima_non_hybrid_frank_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif total_cars_premise != 280:
    # check if the number of total cars in the hypothesis contradicts the number of total cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
