y = 100

m = 400

# the hypothesis refers to the speed of Molly and Max's driving, which is also mentioned in the premise

if m >= 400:
    # check if the hypothesis value contradicts the premise statement of less than 400 kilometers per hour
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)

