# defining the variables
x = 7
y = 5
z = 7

# defining the hypothesis
hypothesis = 5

# comparing the premise and hypothesis
if x!= hypothesis:
    # if the value of x in the hypothesis does not match the value in the premise, it is a contradiction
    label = "contradiction"
elif y!= 7:
    # if the value of y in the hypothesis does not match the value in the premise, it is a contradiction
    label = "contradiction"
elif z!= 7:
    # if the value of z in the hypothesis does not match the value in the premise, it is a contradiction
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the values in the premise, it is entailment
    label = "entailment"

print(label)
