premise = "Last week, saw the fall of the Dutch right wing coalition government, made up of the Christian-democrats (CDA) led by Prime Minister Jan Peter Balkenende, the right wing liberal party (VVD) and the so-called left-liberal D66."
hypothesis = "Three parties form a Dutch coalition government."

# extract the number of parties from the premise
parties_premise = 4

# extract the number of parties from the hypothesis
parties_hypothesis = 3

# check if the number of parties in the hypothesis contradicts the number of parties in the premise
if parties_hypothesis!= parties_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
