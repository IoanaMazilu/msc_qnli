cats_premise = 17.0
cats_given_away = 14.0
cats_hypothesis = 5.0

# the hypothesis refers to the number of cats Mrs. Sheridan has, which is also mentioned in the premise
# compute the remaining cats in the premise
remaining_cats_premise = cats_premise - cats_given_away

if cats_hypothesis!= remaining_cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of remaining cats in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
