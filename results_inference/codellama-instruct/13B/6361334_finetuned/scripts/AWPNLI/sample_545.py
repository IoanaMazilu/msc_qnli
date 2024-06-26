num_cats_premise = 17.0
num_cats_given_away_premise = 14.0
num_cats_hypothesis = 5.0

# the hypothesis refers to the number of cats, which are also mentioned in the premise
# compute the total number of cats in the premise
total_num_cats_premise = num_cats_premise - num_cats_given_away_premise
if total_num_cats_premise!= num_cats_hypothesis:
    # check if the number of cats in the hypothesis contradicts the number of cats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
