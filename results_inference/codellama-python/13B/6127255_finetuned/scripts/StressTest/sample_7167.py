people_entered_premise_sujit_suraj = 7
people_entered_hypothesis_sujit_suraj = 1
people_entered_premise_suraj = 20
people_entered_hypothesis_suraj = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj, mentioned in the premise
if people_entered_hypothesis_sujit_suraj >= people_entered_premise_sujit_suraj:
    # check if the estimate of 'people_entered_hypothesis_sujit_suraj' contradicts the number of people who entered between Sujit and Suraj in the premise
    label = "contradiction"
elif people_entered_hypothesis_suraj!= people_entered_premise_suraj:
    # check if the number of people who entered after Suraj in the hypothesis contradicts the number of people who entered after Suraj reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
