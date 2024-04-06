# Premise: Quarterback Donovan McNabb was every bit Quarterback Tom Brady's equal for 48 passes Sunday night, throwing for 357 yards and three touchdowns in his Super Bowl debut for the Philadelphia Eagles.
# Hypothesis: McNabb's 357 yards were the best postseason game of his career.
# Golden Label: neutral

mcnabb_yards_premise = 357
mcnabb_yards_hypothesis = 357

# the hypothesis talks about McNabb's best postseason game, which is not mentioned in the premise (just his Super Bowl debut is mentioned)
# the hypothesis cannot be entailed from the premise, since we don't know if this was his best postseason game.
label = "neutral"

print(label)

