saved_percentage_premise = 40
saved_percentage_hypothesis = 10

# the hypothesis refers to the percentage of salary saved by Kishore, which is also mentioned in the premise
if saved_percentage_hypothesis >= saved_percentage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'saved_percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of salary saved
    # any percentage lower than 'saved_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
