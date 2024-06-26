salman_shirt_premise = 40
salman_shirt_hypothesis = 30
ambani_shirt_premise = 40
ambani_shirt_hypothesis = 35
dalmiya_shirt_premise = 40
dalmiya_shirt_hypothesis = 45

# the hypothesis refers to the average number of shirts with each of the three individuals
if salman_shirt_hypothesis <= salman_shirt_premise:
    # check if the estimate of'salman_shirt_hypothesis' contradicts the number of shirts reported in the premise
    label = "contradiction"
elif ambani_shirt_hypothesis!= ambani_shirt_premise:
    # check if the number of shirts purchased by Ambani in the hypothesis contradicts the number of shirts reported in the premise
    label = "contradiction"
elif dalmiya_shirt_hypothesis!= dalmiya_shirt_premise:
    # check if the number of shirts purchased by Dalmiya in the hypothesis contradicts the number of shirts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
