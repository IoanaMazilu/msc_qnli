herd_parts_premise = 5
herd_parts_hypothesis = 5

# the hypothesis refers to the number of parts Antony can divide his herd into, mentioned in the premise
if herd_parts_hypothesis >= herd_parts_premise:
    # check if the hypothesis value contradicts the premise of exactly 'herd_parts_premise' parts
    label = "contradiction"
else:
    # the premise gives an exact number of parts
    # any number of parts less than 'herd_parts_premise' contradicts the premise
    label = "contradiction"

print(label)
