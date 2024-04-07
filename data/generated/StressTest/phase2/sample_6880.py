# Premise: Q:Robert purchased $less than 6500 worth of US saving bonds.
# Hypothesis: Q:Robert purchased $1500 worth of US saving bonds.
# Golden Label: neutral

saving_bonds_premise = 6500
saving_bonds_hypothesis = 1500

# the hypothesis talks about the value of US saving bonds Robert purchased, which is also mentioned in the premise
if saving_bonds_hypothesis >= saving_bonds_premise:
    # check if the value of 'saving_bonds_hypothesis' contradicts the estimate of less than 'saving_bonds_premise'
    label = "contradiction"
elif saving_bonds_hypothesis < saving_bonds_premise:
    # the premise gives an estimate for the value of US saving bonds Robert purchased
    # any value less than 'saving_bonds_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

