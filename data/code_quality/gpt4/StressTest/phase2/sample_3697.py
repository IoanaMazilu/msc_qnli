germs_premise = 0.037 * (30 ** 5)
germs_hypothesis = 0.037 * (10 ** 5)
petri_dishes = 148000 * (10 ** (-3))

# the hypothesis refers to the number of germs and Petri dishes mentioned in the premise
if germs_hypothesis != germs_premise:
    # check if the number of germs in the hypothesis contradicts the number of germs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
