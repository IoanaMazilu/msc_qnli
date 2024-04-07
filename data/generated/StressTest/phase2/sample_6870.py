# Premise: Mary has 2 puppies, 9 birds, 4 fishes.
# Hypothesis: Mary has less than 5 puppies, 9 birds, 4 fishes.
# Golden Label: entailment

puppies_premise = 2
birds_premise = 9
fishes_premise = 4

puppies_hypothesis = 5
birds_hypothesis = 9
fishes_hypothesis = 4

# the hypothesis refers to the number of puppies, birds, and fishes owned by Mary mentioned in the premise
if puppies_premise >= puppies_hypothesis:
    # check if the number of puppies in the premise contradicts the estimate of less than 'puppies_hypothesis'
    label = "contradiction"
elif birds_premise != birds_hypothesis or fishes_premise != fishes_hypothesis:
    # check if the number of birds or fishes in the hypothesis contradicts the number of birds or fishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

