people_entered_premise = 7
people_entered_hypothesis = 8

# the hypothesis refers to the number of people entered the theater between Sujit and Suraj, which is also mentioned in the premise
if people_entered_hypothesis <= people_entered_premise:
    # check if the estimate of 'people_entered_hypothesis' contradicts the number of people entered the theater in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
