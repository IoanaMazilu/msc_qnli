amar_age_premise = 20
akbar_age_premise = 30
anthony_age_premise = 26
total_age_premise = amar_age_premise + akbar_age_premise + anthony_age_premise

amar_age_hypothesis = 20
akbar_age_hypothesis = 30
anthony_age_hypothesis = 26
total_age_hypothesis = amar_age_hypothesis + akbar_age_hypothesis + anthony_age_hypothesis

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_age_premise < total_age_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than 'total_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total age
    # any total age greater than or equal to 'total_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
