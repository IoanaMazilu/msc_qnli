germs_premise = 0.036 * (30 ** 5)
germs_hypothesis = 0.036 * (10 ** 5)
petri_dishes_premise = 45000 * (10 ** -3)
petri_dishes_hypothesis = 45000 * (10 ** -3)

# the hypothesis refers to the number of germs and Petri dishes mentioned in the premise
if germs_hypothesis > germs_premise:
    # check if the given number of germs in the hypothesis contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_hypothesis != petri_dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes reported in the premise
    label = "contradiction"
elif germs_hypothesis < germs_premise:
    # if the hypothesis germs value is less than the premise and petri dishes are equal, we can infer entailment
    label = "entailment"
else:
    # the premise gives the exact number of germs and Petri dishes
    # if the hypothesis values match the premise ones, we can infer entailment
    label = "entailment"

print(label)
