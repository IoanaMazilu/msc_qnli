amar_age = 20
akbar_age = 25
anthony_age = 10

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if amar_age + akbar_age + anthony_age <= 35:
    # check if the estimate of 'amar_age + akbar_age + anthony_age' contradicts the number of years mentioned in the premise
    label = "contradiction"
elif amar_age + akbar_age + anthony_age == 45:
    # check if the hypothesis value contradicts the number of years mentioned in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
