points_premise = 60
points_hypothesis = 0
jason_percentage_premise = 0.6
jason_percentage_hypothesis = 0.6

# the hypothesis talks about a lower score and the same percentage of points contributed by Jason
if points_hypothesis <= points_premise:
    # check if the hypothesis value contradicts the estimate of points scored in the premise
    label = "contradiction"
elif jason_percentage_hypothesis!= jason_percentage_premise:
    # check if the percentage of points contributed by Jason in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
