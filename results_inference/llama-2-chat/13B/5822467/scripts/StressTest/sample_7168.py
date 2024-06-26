people_entered_premise = 20
people_entered_hypothesis = 7

# the hypothesis refers to the number of people entered the theater between Sujit and Suraj and the number of people entered the theater after Suraj
if people_entered_hypothesis <= people_entered_premise:
    # check if the estimate of 'people_entered_hypothesis' contradicts the number of people entered the theater reported in the premise
    label = "contradiction"
elif people_entered_hypothesis!= people_entered_premise:
    # check if the number of people entered the theater in the hypothesis contradicts the number of people entered the theater reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
