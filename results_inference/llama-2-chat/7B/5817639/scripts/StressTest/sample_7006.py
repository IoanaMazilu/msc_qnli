gerbil_total_premise = 56
gerbil_total_hypothesis = 96

# the hypothesis talks about the total number of pets consisting of gerbils and hamsters, referenced also in the premise
if gerbil_total_hypothesis <= gerbil_total_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gerbil_total_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pets
    # any number of pets greater than 'gerbil_total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
