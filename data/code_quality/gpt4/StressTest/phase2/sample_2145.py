cake_flavors_premise = 7
cake_flavors_hypothesis = 8

# the hypothesis talks about the number of cake flavors in Jeni's bakery, referenced also in the premise
if cake_flavors_premise >= cake_flavors_hypothesis:
    # check if the premise value contradicts the estimate of less than 'cake_flavors_hypothesis'
    label = "contradiction"
else:
    # any number of cake flavors less than 'cake_flavors_hypothesis' is consistent with the hypothesis, and can be explicitly entailed from the premise
    label = "entailment"

print(label)
