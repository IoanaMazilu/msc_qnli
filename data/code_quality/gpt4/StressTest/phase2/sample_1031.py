germs_premise = 2.16 * 10 ** 6
germs_hypothesis = 2.16 * 40 ** 6
petri_dishes_premise = 10800
petri_dishes_hypothesis = 10800

# hypothesis and premise refer to the number of germs and Petri dishes in the same biology lab
if germs_hypothesis != germs_premise:
    # check if the number of germs in the hypothesis contradicts the number of germs reported in the premise
    label = "contradiction"
elif petri_dishes_hypothesis != petri_dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
