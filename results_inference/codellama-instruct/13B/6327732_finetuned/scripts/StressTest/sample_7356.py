amar_age = 10
akbar_age = 15
anthony_age = 10

total_ages_premise = amar_age + akbar_age + anthony_age
total_ages_hypothesis = 35

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_ages_premise <= total_ages_hypothesis:
    # check if the estimate of 'total_ages_hypothesis' contradicts the total age of Amar, Akbar and Anthony in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total age
    # any total age greater than 'total_ages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
