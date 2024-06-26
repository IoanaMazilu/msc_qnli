cats_premise = 17.0
given_away_cats_premise = 14.0
cats_hypothesis = 5.0

# the hypothesis refers to the number of cats, which are also mentioned in the premise
# compute the number of cats left in the premise
cats_left_premise = cats_premise - given_away_cats_premise
if cats_hypothesis!= cats_left_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
