sides_premise = {
    "ST": 10,
    "TV": 10,
    "SV": 12
}

sides_hypothesis = {
    "ST": less than 50,
    "TV": less than 50,
    "SV": 12
}

# compare the hypothesis values with the premise values
if sides_hypothesis["ST"] <= sides_premise["ST"] or sides_hypothesis["TV"] <= sides_premise["TV"]:
    # check if the hypothesis value contradicts the estimate of more than'sides_premise["ST"]'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than'sides_premise["SV"]' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
