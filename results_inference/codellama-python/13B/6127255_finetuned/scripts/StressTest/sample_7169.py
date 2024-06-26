people_premise_sujit_suraj = 7
people_hypothesis_sujit_suraj = 8
people_premise_suraj_end = 20
people_hypothesis_suraj_end = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj, which is also mentioned in the premise
if people_hypothesis_sujit_suraj!= people_premise_sujit_suraj:
    # check if the number of people in the hypothesis who entered the theater between Sujit and Suraj contradicts the number of people in the premise who entered the theater between Sujit and Suraj
    label = "contradiction"
elif people_hypothesis_suraj_end!= people_premise_suraj_end:
    # check if the number of people in the hypothesis who entered the theater after Suraj contradicts the number of people in the premise who entered the theater after Suraj
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
