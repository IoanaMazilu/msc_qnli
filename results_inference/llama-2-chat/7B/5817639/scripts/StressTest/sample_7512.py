outfit_count_premise = 3
outfit_count_hypothesis = 4

# the hypothesis talks about the number of outfits Jordan has, referenced also in the premise
if outfit_count_hypothesis <= outfit_count_premise:
    # check if the hypothesis value contradicts the estimate of 'outfit_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of outfits
    # any number of outfits greater than 'outfit_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
