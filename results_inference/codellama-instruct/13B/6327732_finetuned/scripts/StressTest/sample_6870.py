puppies_premise = 2
puppies_hypothesis = 5
birds_premise = 9
birds_hypothesis = 9
fishes_premise = 4
fishes_hypothesis = 4

# the hypothesis talks about the number of puppies, referenced also in the premise
if puppies_hypothesis >= puppies_premise:
    # check if the hypothesis value contradicts the estimate of less than 'puppies_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of puppies
    # any number of puppies less than 'puppies_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
