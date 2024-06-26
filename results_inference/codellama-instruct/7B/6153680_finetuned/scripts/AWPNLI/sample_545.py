cats_mrs_sheridan_premise = 17.0
cats_given_away_premise = 14.0
cats_left_hypothesis = 5.0

# the hypothesis refers to the number of cats left, which is also mentioned in the premise
# compute the number of cats left in the premise
cats_left_premise = cats_mrs_sheridan_premise - cats_given_away_premise
if cats_left_hypothesis!= cats_left_premise:
    # check if the number of cats left in the hypothesis contradicts the number of cats left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
