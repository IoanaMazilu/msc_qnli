cats_premise = 17.0
cats_given_away_premise = 14.0
cats_hypothesis = 5.0

# compute the total number of cats in the premise
total_cats_premise = cats_premise + cats_given_away_premise

# check if the hypothesis value contradicts the total number of cats in the premise
if cats_hypothesis!= total_cats_premise:
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the total number of cats in the premise, we can infer entailment
    label = "entailment"

print(label)
