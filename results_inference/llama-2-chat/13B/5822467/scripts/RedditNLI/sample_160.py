# Premise: GDP Report Shows US Economy Off to Slow Start in 2017.
premise_gdp = "GDP Report Shows US Economy Off to Slow Start in 2017."

# Hypothesis: U.S. economy off to slow start in 2017 under Trump.
hypothesis_trump = "U.S. economy off to slow start in 2017 under Trump."

# Extract the year from the premise
year_premise = int(premise_gdp.split("in")[1].split(".")[0])

# Extract the year from the hypothesis
year_hypothesis = int(hypothesis_trump.split("in")[1].split(".")[0])

# Define variables for the numerical entities in the premise and hypothesis
gdp_premise = float(premise_gdp.split("GDP")[1])
economy_premise = float(premise_gdp.split("economy")[1])

# Define variables for the numerical entities in the hypothesis
gdp_hypothesis = float(hypothesis_trump.split("GDP")[1])
economy_hypothesis = float(hypothesis_trump.split("economy")[1])

# Check if the years in the premise and hypothesis are the same
if year_premise == year_hypothesis:
    # Check if the GDP values in the premise and hypothesis are the same
    if gdp_premise == gdp_hypothesis:
        # Check if the economy values in the premise and hypothesis are the same
        if economy_premise == economy_hypothesis:
            # Infer entailment
            label = "entailment"
        else:
            # Infer neutral
            label = "neutral"
    else:
        # Infer contradiction
        label = "contradiction"
else:
    # Infer neutral
    label = "neutral"

print(label)
