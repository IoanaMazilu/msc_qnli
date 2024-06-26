fannie_freddie_premise = 363
fannie_freddie_hypothesis = 215

# the hypothesis and premise mention the amount of money needed by Fannie and Freddie
if fannie_freddie_hypothesis!= fannie_freddie_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
