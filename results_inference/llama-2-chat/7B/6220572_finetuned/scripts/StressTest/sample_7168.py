people_entered_premise = 1
people_entered_hypothesis = 7
people_after_suraj_premise = 20
people_after_suraj_hypothesis = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj, also referenced in the premise
if people_entered_hypothesis <= people_entered_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_entered_premise'
    label = "contradiction"
elif people_after_suraj_hypothesis!= people_after_suraj_premise:
    # check if the number of people who entered the theater after Suraj in the hypothesis contradicts the number of people who entered the theater after Suraj reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
