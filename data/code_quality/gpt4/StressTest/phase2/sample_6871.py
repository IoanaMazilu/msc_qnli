puppies_premise = 5
puppies_hypothesis = 2
birds_premise = 9
birds_hypothesis = 9
fishes_premise = 4
fishes_hypothesis = 4

# the hypothesis refers to the number of each pet Mary has, mentioned in the premise
if puppies_hypothesis >= puppies_premise:
    # check if the number of puppies in the hypothesis contradicts the estimate of less than 'puppies_premise'
    label = "contradiction"
elif birds_hypothesis != birds_premise or fishes_hypothesis != fishes_premise:
    # check if the number of birds or fishes in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
