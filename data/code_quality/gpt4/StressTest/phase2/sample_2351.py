non_hybrid_tajimas_difference_premise = 35
non_hybrid_tajimas_difference_hypothesis = 75

# the hypothesis refers to the difference between the number of non hybrid Tajima's and 3 times the number of hybrid Tajima's mentioned in the premise
if non_hybrid_tajimas_difference_hypothesis != non_hybrid_tajimas_difference_premise:
    # check if the number of 'non_hybrid_tajimas_difference_hypothesis' contradicts the number of 'non_hybrid_tajimas_difference_premise'
    label = "contradiction"
else:
    # if the difference in the hypothesis does not contradict the one in premise, we can infer entailment
    label = "entailment"

print(label)
