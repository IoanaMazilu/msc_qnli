rent_payment_premise = 360
rent_payment_hypothesis = 160

# the hypothesis talks about the rental payment made by Rahul, which is also mentioned in the premise
if rent_payment_hypothesis >= rent_payment_premise:
    # check if the hypothesis value contradicts the premise estimate of 'less than rent_payment_premise'
    label = "contradiction"
else:
    # if the payment made in the hypothesis is less than 'rent_payment_premise', the hypothesis does not contradict the premise
    # however, the exact amount paid is not specified in the premise, so we cannot fully entail the hypothesis from the premise
    label = "neutral"

print(label)
