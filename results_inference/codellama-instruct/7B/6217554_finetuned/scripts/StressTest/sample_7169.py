people_premise = 7
people_after_suraj_premise = 20
people_hypothesis = 8
people_after_suraj_hypothesis = 20

# the hypothesis talks about the number of people who entered the theater, referenced also in the premise
if people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
elif people_after_suraj_hypothesis!= people_after_suraj_premise:
    # check if the number of people after Suraj in the hypothesis contradicts the number of people after Suraj reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
