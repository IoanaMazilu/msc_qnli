people_between_sujit_suraj_premise = 7
people_between_sujit_suraj_hypothesis = 1
people_after_suraj_premise = 20
people_after_suraj_hypothesis = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj mentioned in the premise
if people_between_sujit_suraj_premise <= people_between_sujit_suraj_hypothesis:
    # check if the estimate of 'people_between_sujit_suraj_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
elif people_after_suraj_hypothesis != people_after_suraj_premise:
    # check if the number of people who entered after Suraj in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
