from math import comb

def display_answer(denom):
    print("1/{} = {:.15f}%\n".format(denom,100/denom))

print("Matt: \"What's the probability of winning the lottery in the UK at the moment? ... 45 million, roughly\"\n")
print("59 choose 6: {}\n".format(comb(59,6)))

print("Matt: \"the probability is 0.0000022%\"\n")
display_answer(comb(59,6))

print("Matt: \"But let's say along the way while I'm working it out, for strange reasons I go 'oh you know what, I'm going to ignore all the options which are all square numbers. You know, I just can't be bothered including them. Yeah, they're legitimate lottery tickets, but just to make the maths easier I'm going to ignore them'. And people are getting up in arms, and they're like 'you can't ignore them, they're real options'. Well, that changes the probability from being 0.00000221939% to being 0.00000221939%, it's identical. Just because I ruled out those options.\"\n")
print("Here we're ignoring {} tickets which are all squares:".format(comb(7,6)))
display_answer(comb(59,6)-comb(7,6))

print("Matt: \"Even if I said I'm going to ignore all the tickets which are all odd numbers, it's still 0.0000022%. It hasn't changed.\"\n")
print("Here we're ignoring {} tickets which contain only odd numbers:".format(comb(30,6)))
display_answer(comb(59,6)-comb(30,6))

print("Matt: \"Even if I say I'm going to ignore all the lottery tickets that have a 7 on them, the number 7, which is a lot, over half a million, it's still 0.000002%, little bit different. Instead of being 0.0000022, it's 0.0000025.\"\n")
print("Here we're ignoring {} tickets which choose literally the number 7 and five other numbers:".format(comb(58,5)))
display_answer(comb(59,6)-comb(58,5))
print("Here we're ignoring {} tickets which choose one of the six numbers with a 7 digit and five other numbers which may or may not include a 7 digit:".format(6*comb(58,5)))
display_answer(comb(59,6)-6*comb(58,5))
