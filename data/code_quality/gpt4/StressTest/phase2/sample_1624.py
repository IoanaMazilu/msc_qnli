flour_cups_premise = 65
flour_cups_hypothesis = 15
sugar_cups_premise = 16
sugar_cups_hypothesis = 16
milk_cups_premise = 8
milk_cups_hypothesis = 8

# the hypothesis talks about the number of cups of flour, sugar, and milk Victor has, all of which are mentioned in the premise
if flour_cups_hypothesis >= flour_cups_premise:
    # check if the hypothesis value contradicts the premise of having less than 'flour_cups_premise'
    label = "contradiction"
elif sugar_cups_hypothesis != sugar_cups_premise or milk_cups_hypothesis != milk_cups_premise:
    # check if the number of cups of sugar or milk in the hypothesis contradicts the number of cups reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of flour cups
    # any number of flour cups less than 'flour_cups_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
