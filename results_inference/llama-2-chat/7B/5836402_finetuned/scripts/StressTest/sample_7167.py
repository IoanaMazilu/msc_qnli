people_entered_premise = 7
people_entered_hypothesis = 1
people_entered_after_suraj_premise = 20
people_entered_after_suraj_hypothesis = 20

# the hypothesis refers to the number of people entered the theater mentioned in the premise
if people_entered_hypothesis!= people_entered_premise:
    # check if the number of people entered in the hypothesis contradicts the number of people entered in the premise
    label = "contradiction"
elif people_entered_after_suraj_hypothesis!= people_entered_after_suraj_premise:
    # check if the number of people entered after Suraj in the hypothesis contradicts the number of people entered after Suraj in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
