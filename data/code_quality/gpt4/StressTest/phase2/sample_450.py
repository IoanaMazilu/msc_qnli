life_fraction_premise = 1/7
life_fraction_hypothesis = 7/7

# The hypothesis talks about the fraction of his life after which he marries Diana
if life_fraction_hypothesis < life_fraction_premise:
    # checking if the fraction of life in the hypothesis contradicts the fraction of life in the premise
    label = "contradiction"
else:
    # the premise gives a specific fraction of his life after which he marries Diana
    # any fraction greater than or equal to 'life_fraction_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
