people_premise = 7
people_hypothesis = 1
people_after_suraj_premise = 20
people_after_suraj_hypothesis = 20

# the hypothesis refers to the number of people entering the theater between Sujit and Suraj and after Suraj, also mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the estimate of 'people_hypothesis' contradicts the number of people entering the theater between Sujit and Suraj in the premise
    label = "contradiction"
elif people_after_suraj_hypothesis!= people_after_suraj_premise:
    # check if the number of people entering the theater after Suraj in the hypothesis contradicts the number of people entering the theater after Suraj reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
