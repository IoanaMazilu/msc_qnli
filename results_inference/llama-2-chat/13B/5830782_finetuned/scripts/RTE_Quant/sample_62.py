# There are no numerical entities in the hypothesis or premise

# The hypothesis talks about the lighthouse of Alexandria being one of the seven wonders of the world, which is also mentioned in the premise
if hypothesis == premise:
    # check if the hypothesis is fully and explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis is not fully and explicitly entailed from the premise, we infer neutrality
    label = "neutral"

print(label)
