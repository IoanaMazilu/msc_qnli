people_entered_premise_sujit_suraj = 7
people_entered_hypothesis_sujit_suraj = 8
people_entered_after_suraj_premise = 20
people_entered_after_suraj_hypothesis = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj, mentioned in the premise
if people_entered_hypothesis_sujit_suraj!= people_entered_premise_sujit_suraj:
    # check if the number of people who entered the theater between Sujit and Suraj in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
elif people_entered_after_suraj_hypothesis!= people_entered_after_suraj_premise:
    # check if the number of people who entered the theater after Suraj in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
