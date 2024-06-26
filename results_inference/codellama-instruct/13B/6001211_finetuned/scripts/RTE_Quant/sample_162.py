total_pills_premise = 70e6
pills_with_metal_premise = 200e3
total_pills_hypothesis = 70e6
pills_with_metal_hypothesis = 200e3

# the hypothesis talks about the number of pills with metal which are not referenced in the premise (the source of the pills is not mentioned)
# the hypothesis cannot be entailed from the premise, since the number of pills with metal is unknown.
label = "neutral"

print(label)
