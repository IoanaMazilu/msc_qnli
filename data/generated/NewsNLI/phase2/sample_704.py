# Premise: The letter -- addressed to Senate Majority Leader Harry Reid, D-Nevada ; Minority Leader Mitch McConnell, R-Kentucky ; Judiciary Committee Chairman Patrick Leahy, D-Vermont ; and Alabama Sen. Jeff Sessions, the ranking Republican on the Senate Judiciary Committee -- was signed by 45 of her 49 former law clerks.
# Hypothesis: Endorsement signed by 45 of Supreme Court nominee's 49 former law clerks.
# Golden Label: neutral

clerks_premise = 49
signed_premise = 45
clerks_hypothesis = 49
signed_hypothesis = 45

# the hypothesis mentions the number of former law clerks who signed an endorsement, which is also referenced in the premise
# however, the hypothesis refers to the Supreme Court nominee, which cannot be entailed from the premise
label = "neutral"

print(label)

