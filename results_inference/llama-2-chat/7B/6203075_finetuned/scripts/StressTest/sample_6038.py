members_premise = 59
members_hypothesis = 59
clubs_premise = 1 to 3
clubs_hypothesis = 1 to 3

# the hypothesis refers to the number of members in the class mentioned in the premise
if members_hypothesis!= members_premise:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
elif clubs_hypothesis!= clubs_premise:
    # check if the number of clubs in the hypothesis contradicts the number of clubs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
