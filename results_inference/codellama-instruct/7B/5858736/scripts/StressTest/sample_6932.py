age_sandy_premise = 6
age_sandy_hypothesis = 6

# the hypothesis refers to the number of years that have passed since Sandy's birth
if age_sandy_hypothesis <= age_sandy_premise:
    # check if the estimate of 'age_sandy_hypothesis' contradicts the number of years that have passed since Sandy's birth
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years that have passed since Sandy's birth
    # any number of years greater than 'age_sandy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
