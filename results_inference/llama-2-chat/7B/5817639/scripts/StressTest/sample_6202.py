traveled_miles_premise = 300
traveled_miles_hypothesis = 200

# the hypothesis talks about the distance traveled by Louisa on the first day of her vacation, referenced also in the premise
if traveled_miles_hypothesis <= traveled_miles_premise:
    # check if the hypothesis value contradicts the estimate of less than 'traveled_miles_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance traveled greater than 'traveled_miles_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
