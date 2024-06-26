premise_earned = 4000
hypothesis_earned = 9000

# the hypothesis refers to the amount of money earned at the end of one year
if hypothesis_earned <= premise_earned:
    # check if the estimate of 'hypothesis_earned' contradicts the amount of money earned in the premise
    label = "contradiction"
elif hypothesis_earned > premise_earned:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the amount of money earned
    # any amount of money greater than 'premise_earned' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
