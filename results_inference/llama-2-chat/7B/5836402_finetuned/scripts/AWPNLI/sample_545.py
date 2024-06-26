cats_mrs_sheridan_premise = 17.0
cats_given_away_premise = 14.0
cats_hypothesis = 5.0

# the hypothesis refers to the number of cats, which are also mentioned in the premise
# compute the current number of cats from the premise
current_cats_premise = cats_mrs_sheridan_premise - cats_given_away_premise
if current_cats_hypothesis!= current_cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
