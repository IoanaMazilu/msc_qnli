germs_premise = 4.32 * 30 ** 6
germs_hypothesis = 4.32 * 10 ** 6
petri_dishes_premise = 10800
petri_dishes_hypothesis = 10800

# the hypothesis talks about the number of germs and Petri dishes in the biology lab, referenced also in the premise
if germs_hypothesis!= germs_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif petri_dishes_hypothesis!= petri_dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
