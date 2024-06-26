balls_store_premise = 3
balls_store_hypothesis = 5
games_store_premise = 6
games_store_hypothesis = 6

# the hypothesis refers to the number of different types of balls and board games in the store, mentioned also in the premise
if balls_store_hypothesis >= balls_store_premise:
    # check if the estimate of 'balls_store_hypothesis' contradicts the number of different types of balls in the premise
    label = "contradiction"
elif games_store_hypothesis!= games_store_premise:
    # check if the number of different types of board games in the hypothesis contradicts the number of different types of board games reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
