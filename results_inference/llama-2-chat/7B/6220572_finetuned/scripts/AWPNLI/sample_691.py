dollars_saved_premise = 21
allowance_premise = 15
gambles_wins_premise = 6
dollars_hypothesis = 220.0

# the hypothesis refers to the amount of dollars, which are also mentioned in the premise
# compute the total amount of dollars in the premise
total_dollars_premise = dollars_saved_premise + allowance_premise + gambles_wins_premise * 6
if total_dollars_hypothesis!= total_dollars_premise:
    # check if the number of dollars in the hypothesis contradicts the number of dollars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
