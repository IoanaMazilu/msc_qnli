germs_lab_premise = 4.32 * 10 ** 6
germs_lab_hypothesis = 4.32 * 10 ** 6 / 30 ** 6
petri_dishes_lab_premise = 10800
petri_dishes_lab_hypothesis = 10800

# the hypothesis talks about the number of germs in the lab, referenced also in the premise
if germs_lab_hypothesis >= germs_lab_premise:
    # check if the number of germs in the hypothesis contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_lab_hypothesis!= petri_dishes_lab_premise:
    # check if the number of petri dishes in the hypothesis contradicts the number of petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
