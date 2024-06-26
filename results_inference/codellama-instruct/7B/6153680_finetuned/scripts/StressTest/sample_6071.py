builder_label = "entailment"

# the hypothesis refers to the same builder who builds in 15 days
# the premise and hypothesis both refer to the number of 2's used by the builder from Chennai
# the premise and hypothesis both refer to the number of homes built by the builder

if builder_label == "entailment":
    print("The hypothesis is entailed by the premise.")
elif builder_label == "contradiction":
    print("The hypothesis contradicts the premise.")
else:
    print("The hypothesis and premise are neutral.")
