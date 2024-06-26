amar_age = 15
akbar_age = 20
anthony_age = 10

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if amar_age + akbar_age + anthony_age!= 75:
    # check if the hypothesis value contradicts the total age in the premise
    label = "contradiction"
else:
    # the premise gives the total age of Amar, Akbar and Anthony
    # any total age of 75 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
