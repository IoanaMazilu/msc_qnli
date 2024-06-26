# Premise: Mrs. Sheridan has 11.0 cats and she bought 43.0 more.
# Hypothesis: She has 49.0 cats now.
# Golden Label: contradiction

cats_premise = 11.0
bought_cats_premise = 43.0
total_cats_hypothesis = 49.0

# the hypothesis talks about the total number of cats, which are also mentioned in the premise
# compute the total number of cats in the premise
total_cats_premise = cats_premise + bought_cats_premise
if total_cats_hypothesis != total_cats_premise:
    # check if the total number of cats in the hypothesis contradicts the total number of cats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

