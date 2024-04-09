appearance_premise = 4/4
appearance_hypothesis = 1/4

# the hypothesis talks about the appearance of a film in top-10-movies lists, referenced also in the premise
if appearance_hypothesis >= appearance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'appearance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the appearance of a film
    # any appearance less than 'appearance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
