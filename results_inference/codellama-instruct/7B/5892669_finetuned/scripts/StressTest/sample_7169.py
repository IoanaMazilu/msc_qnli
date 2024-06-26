people_entered_premise = 7
people_entered_hypothesis = 8

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj, mentioned in the premise
if people_entered_hypothesis!= people_entered_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
