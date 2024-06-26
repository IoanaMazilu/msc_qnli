shirts_premise = 8
pants_premise = 3
shirts_hypothesis = 2
pants_hypothesis = 3

# The hypothesis refers to the number of shirt and pant combinations mentioned in the premise
if shirts_hypothesis >= shirts_premise:
    # Check if the number of shirts in the hypothesis contradicts the estimate of not less than 'shirts_premise'
    label = "contradiction"
elif pants_hypothesis != pants_premise:
    # Check if the number of pants in the hypothesis contradicts the number of pants reported in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of shirts
    # Any number of shirts less than 'shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
