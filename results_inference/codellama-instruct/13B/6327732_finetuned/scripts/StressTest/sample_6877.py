amar_age = 25
akbar_age = 30
anthony_age = 31

# the hypothesis refers to the total age of Amar, Akbar and Anthony
if amar_age + akbar_age + anthony_age < 86:
    # check if the hypothesis value contradicts the estimate of less than '86' years
    label = "contradiction"
elif amar_age + akbar_age + anthony_age == 66:
    # check if the hypothesis value is consistent with the estimate of '66' years
    label = "entailment"
else:
    # the premise gives only an estimate for the total age
    # any number of years greater than '66' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
