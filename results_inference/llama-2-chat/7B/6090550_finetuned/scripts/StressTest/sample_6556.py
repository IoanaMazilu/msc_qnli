# No members of the club traveled to both England and France in both the premise and hypothesis
# Less than 7 members traveled to both England and Italy in both the premise and hypothesis
# 11 members traveled to both France and Italy in both the premise and hypothesis

# The hypothesis talks about the number of members who traveled to both England and Italy, which is also mentioned in the premise
# However, the number of members who traveled to both France and Italy in the hypothesis is different from the premise
if 6 <= 7:
    # The hypothesis contradicts the premise in the number of members who traveled to both France and Italy
    label = "contradiction"
elif 11!= 11:
    # The number of members who traveled to both France and Italy in the hypothesis is different from the premise
    label = "contradiction"
else:
    # The premise and hypothesis are consistent, but the number of members who traveled to both France and Italy in the hypothesis is different
    label = "neutral"

print(label)
