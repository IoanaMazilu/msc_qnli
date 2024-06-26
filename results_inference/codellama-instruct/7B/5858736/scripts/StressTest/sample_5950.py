premise_temp = 20
premise_k = 32
hypothesis_temp = 20
hypothesis_k = 32

# the hypothesis talks about the temperature in Fahrenheit, referenced also in the premise
if hypothesis_temp <= premise_temp:
    # check if the hypothesis value contradicts the estimate of more than 'premise_temp'
    label = "contradiction"
elif hypothesis_k!= premise_k:
    # check if the number of roses in the hypothesis contradicts the number of roses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
