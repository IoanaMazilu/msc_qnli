premise_weight = 200
hypothesis_weight = 800
package1_weight = 150
package2_weight = 280

# the hypothesis refers to the weight of Sean and the packages mentioned in the premise
if hypothesis_weight <= premise_weight + package1_weight + package2_weight:
    # check if the estimate of 'hypothesis_weight' contradicts the weight of Sean and the packages in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of Sean and the packages
    # any weight combination that adds up to less than 'hypothesis_weight' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
