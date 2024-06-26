outfit_premise = 3
outfit_hypothesis = 5

# the hypothesis talks about the number of outfits, which is also referred to in the premise
if outfit_hypothesis <= outfit_premise:
    # check if the hypothesis value contradicts the estimate of 'outfit_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of outfits, but the hypothesis value is not necessarily contradictory
    label = "neutral"

print(label)
