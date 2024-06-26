average_gym_visits_premise = 2
average_gym_visits_hypothesis = 2

# the hypothesis talks about the number of times Rikki goes to the gym after less than 2 more weeks, which is also mentioned in the premise
if average_gym_visits_hypothesis!= average_gym_visits_premise:
    # check if the average number of times Rikki goes to the gym in the hypothesis contradicts the average number of times Rikki goes to the gym in the premise
    label = "contradiction"
else:
    # if the hypothesis values and premise values are equal, it is an entailment
    label = "entailment"

print(label)
