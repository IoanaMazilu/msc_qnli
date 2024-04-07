# Premise: Every time you travel a mile towards Bananaville you must pay a tax of 1 apple but you pay nothing when going in the other direction (towards Appleland). What is highest number of apples you can get to Bananaville?
# Hypothesis: Every time you travel a mile towards Bananaville you must pay a tax of less than 8 apple but you pay nothing when going in the other direction (towards Appleland). What is highest number of apples you can get to Bananaville?
# Golden Label: entailment

tax_bananaville_premise = 1
tax_bananaville_hypothesis = 8

# the hypothesis talks about the tax per mile towards Bananaville, referenced also in the premise
if tax_bananaville_hypothesis < tax_bananaville_premise:
    # check if the tax amount of 'tax_bananaville_hypothesis' contradicts the tax amount per mile in the premise
    label = "contradiction"
else:
    # if the tax amount in the hypothesis do not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

