# How i spent my weekly allowance

allowance = 2000
print(f"my weekly allowance is:{allowance}")

allowance -= 400
print(f"I bought books worth ₦400 and i'm left with {allowance}")

allowance += 100
print(f"I found ₦100 under my bed and added to what i had and i'm left with ₦{allowance}")

allowance -= 250
print(f"I bought snacks worth ₦250 and i'm left with ₦{allowance}")

percentage = 25/100
percentage *= allowance
allowance -= percentage
print(f"I gave 25% to my younger sibling and i'm left with ₦{allowance}")

oneThird = allowance / 3
allowance -= oneThird
print(f"from my balance i used one third to buy data and i'm left with ₦{allowance}")

allowance //= 2
print(f"I split the remaining balance for savings and tithing and i'm left with ₦{allowance}")

allowance %= 100
print(f"now my final balance is ₦{allowance}")
