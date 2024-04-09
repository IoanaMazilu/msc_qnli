peak_premise = 8586
hypothesis = "Kanchenjunga is 8586 meters high."

# extract numerical information from the premise and hypothesis
peak_premise_int = int(peak_premise)

# check if the hypothesis is a valid number
try:
    hypothesis_int = int(hypothesis)
except ValueError:
    # the hypothesis is not a valid number, so we cannot compare it to the premise
    label = "neutral"
    print(label)
    return

# compare the peak heights in the premise and hypothesis
if peak_premise_int == hypothesis_int:
    # the peak heights in the premise and hypothesis are the same
    label = "entailment"
elif peak_premise_int!= hypothesis_int:
    # the peak heights in the premise and hypothesis are different
    label = "contradiction"
else:
    # the peak heights in the premise and hypothesis are not comparable, so we cannot infer entailment or contradiction
    label = "neutral"

print(label)
