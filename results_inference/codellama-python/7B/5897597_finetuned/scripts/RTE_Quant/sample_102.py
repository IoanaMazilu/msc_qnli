guardsmen_killed_premise = 4
guardsmen_killed_hypothesis = 4
guardsmen_injured_premise = 80
guardsmen_injured_hypothesis = 80

# the hypothesis talks about the number of Iraqi guardsmen killed and injured, which is also mentioned in the premise
if guardsmen_killed_hypothesis!= guardsmen_killed_premise:
    # check if the number of killed guardsmen in the hypothesis contradicts the number of killed guardsmen from the premise
    label = "contradiction"
elif guardsmen_injured_hypothesis!= guardsmen_injured_premise:
    # check if the number of injured guardsmen in the hypothesis contradicts the number of injured guardsmen from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
