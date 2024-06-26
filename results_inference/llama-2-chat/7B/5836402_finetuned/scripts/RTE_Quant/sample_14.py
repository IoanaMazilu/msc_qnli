power_loss_premise = 125000
power_loss_hypothesis = 125000

# the hypothesis talks about the number of people killed by a storm, which is not referenced in the premise (the number of people affected by the storm is mentioned, but not the number of deaths)
# the hypothesis cannot be entailed from the premise, since the number of people killed is unknown.
label = "neutral"

print(label)
