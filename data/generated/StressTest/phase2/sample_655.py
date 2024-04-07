# Premise: Lee Colle insures its students for thefts up to $less than 2000.
# Hypothesis: Lee Colle insures its students for thefts up to $1000.
# Golden Label: neutral

theft_insurance_premise = 2000
theft_insurance_hypothesis = 1000

# the hypothesis talks about the theft insurance coverage amount for students, referenced also in the premise
if theft_insurance_hypothesis > theft_insurance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'theft_insurance_premise'
    label = "contradiction"
elif theft_insurance_hypothesis == theft_insurance_premise:
    # the hypothesis value equals the upper limit from the premise, which contradicts the "less than" condition
    label = "contradiction"
else:
    # the premise gives an upper limit for the theft insurance coverage 
    # any value less than 'theft_insurance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

