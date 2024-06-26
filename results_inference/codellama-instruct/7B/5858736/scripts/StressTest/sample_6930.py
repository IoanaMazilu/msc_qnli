age_sandy_premise = 6
age_sandy_hypothesis = 2

# the hypothesis refers to the number of years that have passed since Sandy's age was 30
if age_sandy_hypothesis <= age_sandy_premise:
    # check if the estimate of 'age_sandy_hypothesis' contradicts the number of years that have passed since Sandy's age was 30
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years that have passed since Sandy's age was 30
    # any number of years greater than 'age_sandy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
