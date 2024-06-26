builder_label = "entailment"

# the hypothesis refers to the same builder as the premise
if "builder" in premise:
    builder_label = "entailment"

print(builder_label)
