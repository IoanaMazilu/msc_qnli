premise_scores = [40, 60, 70, 80, 80]
hypothesis_scores = [40, 60, 70, 80, 80]

# the hypothesis refers to the number of scores obtained by Reeya in different subjects
if hypothesis_scores <= premise_scores:
    # check if the estimate of 'hypothesis_scores' contradicts the number of scores obtained by Reeya in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of scores obtained by Reeya
    # any number of scores greater than 'premise_scores' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
