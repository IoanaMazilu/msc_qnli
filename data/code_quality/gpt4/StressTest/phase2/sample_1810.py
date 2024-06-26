miles_travelled_premise = 350
miles_travelled_hypothesis = 250

# the hypothesis talks about the distance travelled by Louisa on the first day of her vacation, which is also referenced in the premise
if miles_travelled_hypothesis >= miles_travelled_premise:
    # check if the distance travelled in the hypothesis contradicts the estimate of less than 'miles_travelled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance travelled
    # any distance less than 'miles_travelled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
