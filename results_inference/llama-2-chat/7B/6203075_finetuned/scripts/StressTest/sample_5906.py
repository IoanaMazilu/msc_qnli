michael_eat_premise = 1/8
michael_eat_hypothesis = 1/8
steve_eat_premise = 1/2
steve_eat_hypothesis = 1/2
tyler_eat_premise = 150
tyler_eat_hypothesis = 150

# the hypothesis refers to the amount of cookies eaten by Michael, Steve and Tyler
if michael_eat_hypothesis >= michael_eat_premise:
    # check if the amount of cookies eaten by Michael in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif steve_eat_hypothesis!= steve_eat_premise:
    # check if the amount of cookies eaten by Steve in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif tyler_eat_hypothesis!= tyler_eat_premise + michael_eat_premise:
    # check if the amount of cookies eaten by Tyler in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
