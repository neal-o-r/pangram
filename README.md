# Pangram

If you can find 5 five-letter words that share no letters (i.e. that contain 25 different letters) you can use them as your Wordle guesses every time, making guess 6 just a matter of solving an anagram. The issue is in finding 5 words with 25 different letters in a reasonably speedy way.

First off I tried writing a simple recursive function. This works fine for finding 4 words with 20 different letters, but it's not efficient enough to scale to 5 words.

Next I tried what seemed like a clever idea, which involved encoding the words as ints by writing each word as a binary number based on the letters it contians. Then we do some bit-twiddling; starting with the target we're aiming for (a 26 digit long binary number containing 25 1's) and XOR'ing words until we hit 0. This worked, and was a lot faster than the naive method, but still felt wrong.

Finally I twigged that this is an exact cover problem (or 26 exact cover problems, one for each distinct 25 letter set), so we can use [Donald Knuth's Algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) to solve it. This wored really well, and generates all possible word sets very efficiently, here's the output:

```
No solutions for a
No solutions for b
No solutions for c
No solutions for d
No solutions for e
No solutions for f
No solutions for g
No solutions for h
No solutions for i
Without j: waqfs,vozhd,cylix,kempt,brung
Without j: waqfs,vozhd,bemix,grypt,clunk
Without j: waqfs,vozhd,xylic,kempt,brung
Without j: waqfs,vozhd,cimex,blunk,grypt
No solutions for k
No solutions for l
No solutions for m
No solutions for n
No solutions for o
No solutions for p
Without q: fjord,vibex,waltz,gucks,nymph
Without q: fjord,vibex,waltz,gymps,chunk
No solutions for r
No solutions for s
No solutions for t
No solutions for u
No solutions for v
No solutions for w
Without x: waqfs,jumby,vozhd,kreng,clipt
Without x: waqfs,jumby,vozhd,prick,glent
Without x: waqfs,jumby,vozhd,treck,pling
Without x: waqfs,jumpy,vozhd,bling,treck
Without x: waqfs,jumpy,vozhd,brick,glent
No solutions for y
No solutions for z
```
