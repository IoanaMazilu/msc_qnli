power_loss_premise = 125e3
power_loss_hypothesis = 125e3

# the hypothesis talks about the number of people killed by a storm, which is not referenced in the premise
# the hypothesis cannot be entailed from the premise, since the number of people killed is unknown.
label = "neutral"

print(label)
