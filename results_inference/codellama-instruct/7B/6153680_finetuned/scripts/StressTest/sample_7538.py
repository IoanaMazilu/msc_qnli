scores = [40, 60, 70, 80, 80]

# the hypothesis refers to the scores obtained by Reeya, which are also mentioned in the premise
for score in scores:
    if score >= 40:
        # check if the score is greater than or equal to 40, which is also mentioned in the premise
        label = "contradiction"
        break
else:
    # if the score is less than 40, the hypothesis is consistent with the premise
    label = "entailment"

print(label)
