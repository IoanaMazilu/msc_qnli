boy_premise = 200
girl_premise = 160
boy_hypothesis = 700
girl_hypothesis = 160

# the hypothesis refers to the number of boys and girls in the senior class
if boy_hypothesis <= boy_premise and girl_hypothesis == girl_premise:
    # the hypothesis is consistent with the premise, but does not provide any new information
    label = "neutral"
elif boy_hypothesis > boy_premise:
    # the hypothesis indicates there are more boys in the senior class than the premise
    label = "entailment"
else:
    # the hypothesis indicates there are fewer boys in the senior class than the premise
    label = "contradiction"

print(label)
