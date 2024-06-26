amar_age = 20
akbar_age = 25
anthony_age = 31

# the hypothesis refers to the total age of Amar, Akbar and Anthony
if amar_age + akbar_age + anthony_age < 66:
    # check if the hypothesis value contradicts the total age in the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the total age
    # any value less than 66 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
