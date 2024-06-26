puppies_premise = 2
puppies_hypothesis = 5
birds_premise = 9
birds_hypothesis = 9
fishes_premise = 4
fishes_hypothesis = 4

# the hypothesis refers to the number of puppies, birds and fishes Mary has, which is also mentioned in the premise
if puppies_premise >= puppies_hypothesis:
    # check if the number of puppies in the premise contradicts the hypothesis of having less than 'puppies_hypothesis'
    label = "contradiction"
elif birds_premise!= birds_hypothesis or fishes_premise!= fishes_hypothesis:
    # check if the number of birds or fishes in the premise contradicts the number in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
# 