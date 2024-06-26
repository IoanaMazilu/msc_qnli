# defining the ratios
mona_sona_ratio_premise = 4/5
mona_sona_ratio_hypothesis = 1/5

# the hypothesis talks about the ratio of the ages of Mona and Sona, referenced also in the premise
if mona_sona_ratio_hypothesis >= mona_sona_ratio_premise:
    # check if the hypothesis value contradicts the estimate of ratio 'mona_sona_ratio_premise'
    label = "contradiction"
else:
    # any ratio smaller than 'mona_sona_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
