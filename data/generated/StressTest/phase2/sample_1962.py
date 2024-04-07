# Premise: How many liters of blue paint must be added to 40 liters of Fuchsia to change it to Mauve paint?
# Hypothesis: How many liters of blue paint must be added to less than 60 liters of Fuchsia to change it to Mauve paint?
# Golden Label: entailment

fuchsia_premise = 40
fuchsia_hypothesis = 60

# the hypothesis states about the amount of Fuchsia paint mentioned in the premise
if fuchsia_hypothesis <= fuchsia_premise:
    # check if the estimate of 'fuchsia_hypothesis' contradicts the amount of Fuchsia paint in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

