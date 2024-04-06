# Premise: There were a total of 27.0 soccer games during the 3.0 month season, and the games are equally divided.
# Hypothesis: 9.0 soccer games are played a month.
# Golden Label: entailment

total_games_premise = 27.0
months_premise = 3.0
games_per_month_hypothesis = 9.0

# the hypothesis refers to the number of soccer games per month, which is also calculated in the premise
# compute the average number of games per month in the premise
games_per_month_premise = total_games_premise / months_premise
if games_per_month_hypothesis != games_per_month_premise:
    # check if the number of games per month in the hypothesis contradicts the number of games per month from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

