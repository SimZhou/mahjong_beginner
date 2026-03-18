---
title: The Theory of Floating Tiles
description: An English translation of the page explaining tile value by position, overlap between suji-held tiles, and why isolated tiles interact instead of standing alone.
locale: en_US
robots: noindex, nofollow
alt_lang_url: https://simzhou.com/riichi_mahjong_book/pairi/pairi03.html
---

# The Theory of Floating Tiles

Let us think about the function that each of mahjong's 34 tile types has when held by itself.

## 1. Basic Tile Theory

The chance for any tile to become a pair or a triplet is the same for all 34 tile types.  
However, when a pair turns into a triplet, honor tiles and edge-near number tiles are more favorable because they are easier to call.

But if we look at the ability to form sequences, tiles closer to the center are more favorable.  
Honor tiles cannot form sequences at all. They can only become triplets.  
If we assume a closed hand:

**<Set-Building Ability>**

<img src="../../hai/man3.gif" width="24" height="34" /><img src="../../hai/man4.gif" width="24" height="34" /><img src="../../hai/man5.gif" width="24" height="34" /><img src="../../hai/man6.gif" width="24" height="34" /><img src="../../hai/man7.gif" width="24" height="34" /> ＞ <img src="../../hai/man2.gif" width="24" height="34" /><img src="../../hai/man8.gif" width="24" height="34" /> ＞ <img src="../../hai/man1.gif" width="24" height="34" /><img src="../../hai/man9.gif" width="24" height="34" /> ＞ **honor tiles**

That is how they can be ranked.  
The illustration uses manzu, but of course the same is true for pinzu and souzu as well.  
Keep in mind that tiles closer to the inside are worth more.

The value of honor tiles is simpler: tiles that can become valuable triplets are worth more.

**Double wind tiles (double East, double South) ＞ value honors ＞ guest winds**

Value honor tiles that can secure one han by calling are quite valuable, and are often more important than terminal tiles.  
But **once even one copy is discarded, their value drops sharply. If the second copy is visible, they become almost useless for attacking.**

At that point, if you keep them, it is usually as a [safe tile](../mamori/mamori02.md).

## 2. Interaction Between Tiles

Even when number tiles are isolated, combinations that are three apart are generally considered undesirable.

In particular, the combinations **1-4** and **6-9** make the **1** or **9** into a tile with almost no value.

<img src="../../hai/pin1.gif" width="24" height="34" /><img src="../../hai/pin4.gif" width="24" height="34" /> → the acceptance is <img src="../../hai/pin1.gif" width="24" height="34" /> through <img src="../../hai/pin6.gif" width="24" height="34" />  
(after removing overlap, this is almost the same as the acceptance of <img src="../../hai/pin4.gif" width="24" height="34" /> alone)

<img src="../../hai/pin6.gif" width="24" height="34" /><img src="../../hai/pin9.gif" width="24" height="34" /> → the acceptance is <img src="../../hai/pin4.gif" width="24" height="34" /> through <img src="../../hai/pin9.gif" width="24" height="34" />  
(after removing overlap, this is almost the same as the acceptance of <img src="../../hai/pin6.gif" width="24" height="34" /> alone)

In a `1-4` holding, the `1` is only really useful when you draw four specific tiles, such as `2356` or `2335`, and expand it into two sets.

A pair of number tiles that are three apart is called a **suji** relation.  
There is a rule that **when you hold tiles in suji, one of the two tiles loses value**.

The most obvious cases are `1-4` and `6-9`.  
But `2-5`, `3-6`, `4-7`, and `5-8` also show the same negative effect in the kinds of tiles they accept.

That is because **holding tiles in suji causes overlap in acceptance**, and as a result the total number of useful tiles becomes smaller.

| Hand | Draws that can form a taatsu |
| --- | --- |
| <img src="../../hai/man2.gif" width="24" height="34" /> | <img src="../../hai/man1.gif" width="24" height="34" /> <img src="../../hai/man3.gif" width="24" height="34" /> <img src="../../hai/man4.gif" width="24" height="34" /> |
| <img src="../../hai/man5.gif" width="24" height="34" /> | <img src="../../hai/man3.gif" width="24" height="34" /> <img src="../../hai/man4.gif" width="24" height="34" /> <img src="../../hai/man6.gif" width="24" height="34" /> <img src="../../hai/man7.gif" width="24" height="34" /> |
| <img src="../../hai/man2.gif" width="24" height="34" /><img src="../../hai/man5.gif" width="24" height="34" /> | <img src="../../hai/man1.gif" width="24" height="34" /> <img src="../../hai/man3.gif" width="24" height="34" /> <img src="../../hai/man4.gif" width="24" height="34" /> <img src="../../hai/man6.gif" width="24" height="34" /> <img src="../../hai/man7.gif" width="24" height="34" /> |
| (Comparison) <img src="../../hai/sou2.gif" width="24" height="34" /><img src="../../hai/man5.gif" width="24" height="34" /> | <img src="../../hai/sou1.gif" width="24" height="34" /> <img src="../../hai/sou3.gif" width="24" height="34" /> <img src="../../hai/sou4.gif" width="24" height="34" /> <img src="../../hai/man3.gif" width="24" height="34" /> <img src="../../hai/man4.gif" width="24" height="34" /> <img src="../../hai/man6.gif" width="24" height="34" /> <img src="../../hai/man7.gif" width="24" height="34" /> |

Once you look at the table, it becomes obvious.

In the case of <img src="../../hai/man2.gif" width="24" height="34" /><img src="../../hai/man5.gif" width="24" height="34" />, the acceptance on <img src="../../hai/man3.gif" width="24" height="34" /> and <img src="../../hai/man4.gif" width="24" height="34" /> overlaps, so the combined result gives you fewer effective tiles.

If you hold `2-5`, the acceptance on `1` only makes a penchan, so it is not very attractive.  
You should understand a `2-5` holding as "keeping the 2 in order to make a ryanmen when you draw a 3."

That means **when the 1 is thin**, and when the **5 is a red five**, **the value of the 2 goes down**.  
The same applies to the `8` in a `5-8` holding.

As for `3-6` and `4-7`, each tile is strong enough by itself that you do not need to worry much in the early hand about holding them in suji.  
But in shapes like kuttsuki one-shanten, holding them in suji becomes a disadvantage.

**Example**  
<img src="../../hai/man7.gif" width="24" height="34" /><img src="../../hai/pin1.gif" width="24" height="34" /><img src="../../hai/pin2.gif" width="24" height="34" /><img src="../../hai/pin3.gif" width="24" height="34" /><img src="../../hai/pin4.gif" width="24" height="34" /><img src="../../hai/pin7.gif" width="24" height="34" /><img src="../../hai/sou5.gif" width="24" height="34" /><img src="../../hai/sou5.gif" width="24" height="34" /><img src="../../hai/sou7.gif" width="24" height="34" /><img src="../../hai/sou8.gif" width="24" height="34" /><img src="../../hai/sou9.gif" width="24" height="34" /><img src="../../hai/haku.gif" width="24" height="34" /><img src="../../hai/haku.gif" width="24" height="34" /><img src="../../hai/haku.gif" width="24" height="34" /> Dora <img src="../../hai/pin3.gif" width="24" height="34" />

Cutting <img src="../../hai/man7.gif" width="24" height="34" /> here is a loss.  
If you leave both <img src="../../hai/pin4.gif" width="24" height="34" /> and <img src="../../hai/pin7.gif" width="24" height="34" />, the negative effect of suji overlap appears.

If there are no other conditions, the correct answer in this example is to cut <img src="../../hai/pin7.gif" width="24" height="34" />.

### Theory

<div class="green" markdown="1">
Holding tiles in suji causes your effective tiles to overlap, so the end result is a smaller acceptance count.  
In particular, when you have **14**, the `1`, and when you have **69**, the `9`, function very poorly as set candidates, so they should be discarded early.
</div>

---

Finally, let us talk about combinations that are four apart.  
There are five of them: `1-5`, `2-6`, `3-7`, `4-8`, and `5-9`.

In the past, people tended to value these combinations because drawing the middle tile would create a ryan-kan shape.

**Example**  
<img src="../../hai/pin5.gif" width="24" height="34" /><img src="../../hai/pin9.gif" width="24" height="34" />  
Draw <img src="../../hai/pin7.gif" width="24" height="34" /> and it becomes a ryan-kan shape

But this way of thinking is meaningless, and even harmful.

Even without <img src="../../hai/pin9.gif" width="24" height="34" />, you would still accept <img src="../../hai/pin7.gif" width="24" height="34" />.

For example, if you compare <img src="../../hai/pin5.gif" width="24" height="34" /><img src="../../hai/sou9.gif" width="24" height="34" /> with <img src="../../hai/pin5.gif" width="24" height="34" /><img src="../../hai/pin9.gif" width="24" height="34" />, the `5p-9p` holding actually has one fewer accepting tile type.

If you cut <img src="../../hai/pin9.gif" width="24" height="34" /> from <img src="../../hai/pin5.gif" width="24" height="34" /><img src="../../hai/pin9.gif" width="24" height="34" />, the only time that turns out to be a mistake is when you later draw <img src="../../hai/pin7.gif" width="24" height="34" /><img src="../../hai/pin8.gif" width="24" height="34" />.  
Outside of that, <img src="../../hai/pin9.gif" width="24" height="34" /> has no special meaning.

So even though combinations four apart sometimes do form a ryan-kan shape,  
that does not mean they are inherently favorable.  
The conclusion is that there is no need to care at all about preserving these supposed ryan-kan transitions.

---

Original Japanese page: <http://beginners.biz/pairi/pairi03.html>

<!-- PAGE NAV START -->
<div class="page-nav" markdown="0">
  <a class="page-nav__link page-nav__link--prev" href="pairi02.html">Previous: Effective Tiles and Tile Count</a>
  <a class="page-nav__link page-nav__link--next" href="pairi04.html">Next: Taatsu Theory (1)</a>
</div>
<!-- PAGE NAV END -->
