plate_digits_premise = 5
plate_digits_hypothesis = 7

# the hypothesis refers to the number of digits on the plate of the car bought by Sachin Tendulkar, mentioned also in the premise
if plate_digits_premise > plate_digits_hypothesis:
    # check if the number of digits on the plate in the premise contradicts the estimate of less than 'plate_digits_hypothesis'
    label = "contradiction"
elif plate_digits_hypothesis != plate_digits_premise:
    # the premise gives only an exact number of digits on the plate
    # any number of digits less than 'plate_digits_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
