sony_johnny_fish_premise = 60
sony_johnny_fish_hypothesis = 30

# the hypothesis talks about the number of fish caught by Sony and Johnny, referenced also in the premise
if sony_johnny_fish_hypothesis <= sony_johnny_fish_premise:
    # check if the hypothesis value contradicts the estimate of'sony_johnny_fish_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish caught
    # any number of fish caught greater than'sony_johnny_fish_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
