traveled_premise = 440
traveled_hypothesis = 240

# the hypothesis talks about the distance traveled by Louisa on the first day of her vacation
if traveled_hypothesis <= traveled_premise:
    # check if the hypothesis value contradicts the estimate of less than 'traveled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance traveled by Louisa on the first day of her vacation that is less than or equal to 'traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
