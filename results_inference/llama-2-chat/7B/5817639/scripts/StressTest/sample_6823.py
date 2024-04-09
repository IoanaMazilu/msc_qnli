fish_premise = 80
fish_hypothesis = 10

# the hypothesis talks about the number of fish held by Lilly and Rosy, referenced also in the premise
if fish_hypothesis <= fish_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fish_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish held by Lilly and Rosy
    # any number of fish held by Lilly and Rosy consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
