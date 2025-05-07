'''setting the base price for tickets'''
BASE_PRICE = 100

discounts = {
    "juggler": 0.5,
    "fireTwirler": 0.75,
    "magician": 0.2,
    "escapeArtist": 0.0,
    "otherArtist": 0.8,
}
print()
print()
performerType = input("What type of performer? ")
print()
if performerType in discounts:
    discountedPrice = BASE_PRICE * discounts[performerType]
    print("Your price is $", discountedPrice)
else:
    print("Sorry, no discount is applied")
