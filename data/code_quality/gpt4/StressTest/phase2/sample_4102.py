peter_candies_premise = 3
peter_candies_hypothesis = 9
rina_candies_premise = 5
rina_candies_hypothesis = 5

# the hypothesis talks about the number of candies Peter and Rina have, referenced also in the premise
if peter_candies_hypothesis <= peter_candies_premise:
    # check if the hypothesis value contradicts the estimate of more than 'peter_candies_premise'
    label = "contradiction"
elif rina_candies_hypothesis != rina_candies_premise:
    # check if the number of candies Rina has in the hypothesis contradicts the number of candies Rina has in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of candies Peter has
    # any number of candies greater than 'peter_candies_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
