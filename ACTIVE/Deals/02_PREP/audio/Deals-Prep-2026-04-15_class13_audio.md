---
doc_type: audio_prep
class_number: 13
date: 2026-04-15
day_of_week: Wednesday
title: Derivatives — Basic Building Blocks
status: draft # draft|final
time_minutes_target: 11
word_count_target: 1750
inputs:
  syllabus_assignment: 01_SOURCES/syllabus/Class 13 Derivatives The Basic Building Blocks Panel 3/Dealsdiscussion.13-4.md
  class_reference: 02_PREP/text/2026-04-15_class13_text.md
  core_sources:
    - 01_SOURCES/syllabus/Class 13 Derivatives The Basic Building Blocks Panel 3/McLaughlin Building blocks of functional analysis in Over-the-counter derivative_ products.pdf
    - 01_SOURCES/syllabus/Class 13 Derivatives The Basic Building Blocks Panel 3/Gilson & Black The option perspective in some of the essential of finance and investment.pdf
notes:
  - "[SOURCE NOTE] PDF text extraction failed with pdftotext; relying on discussion questions + past outline."
---

# Audio Prep — Class #13 — Derivatives — Basic Building Blocks

**Audio length: ~28 minutes | Listen before class on Wednesday, 2026-04-15**

---

## INTRO (2 minutes)

Today is the basic building blocks of derivatives: forwards, futures, swaps, and options.

The skill is payoff literacy. Once you can translate a derivative into “who is long, who is short, and what is the payoff if the price moves,” the rest is just variations.

By the end of this prep, you should be able to:
1. Define the basic instruments in one sentence each.
2. Compute payoffs quickly on the gold examples.
3. Explain leverage and replication.
4. Explain why volatility increases option value even if expected price is unchanged.

---

## PART 1: What a derivative is (4 minutes)

A derivative is a contract whose value is tied to something else: the price of an underlying asset, an interest rate, a credit event, a commodity index.

At a high level, it’s a way to repackage risk.

If you already have a risk exposure and you don’t want it, derivatives can transfer it. That’s hedging.

If you don’t have exposure but you want it, derivatives can create it precisely. That’s speculation.

For the basic bilateral instruments, the payoff between the two parties is close to zero-sum. One side’s gain is the other side’s loss. The system-level effects can be broader, but for class purposes, start with the two-party payoff.

---

## PART 2: Long and short; the forward contract (12 minutes)

Long and short are directional labels, but they depend on what instrument you’re talking about.

For a plain forward:
- The party who agrees to buy later at a fixed price is long.
- The party who agrees to sell later at a fixed price is short.

Now the gold example.

Spot is $1,800 on June 1, 2022.

Debbie agrees to buy one ounce from Larry in two years, June 1, 2024, for $1,900.

Debbie is long the forward. Larry is short.

### State 1: gold is $2,100 in June 2024

Debbie pays $1,900 and receives something worth $2,100.

Her gain is $2,100 minus $1,900, which is $200.

Larry delivers something worth $2,100 for $1,900.

His loss is $200.

### State 2: gold is $1,500 in June 2024

Debbie is forced to buy for $1,900 something worth $1,500.

Her loss is $400.

Larry sells something worth $1,500 for $1,900.

His gain is $400.

That payoff logic is the first thing to have ready in class.

### Physical settlement vs cash settlement

Physical settlement means actual gold changes hands.

Cash settlement means you just pay the difference.

If spot is $2,100, Larry pays Debbie $200. If spot is $1,500, Debbie pays Larry $400.

Same economics, no delivery.

Now the question that usually trips people: why is the forward price higher than spot?

The wrong instinct is to treat it as prediction. The right instinct is to treat it as a financing and carrying-cost problem.

Here’s a clean intuition.

Owning gold now requires paying $1,800 now.

A forward gives you the economic exposure of ownership without paying until later. You get “control” over future purchase at a fixed price, and you keep your money in the meantime.

Keeping money has value. That’s the time value. So the forward price typically embeds an interest component. There can also be storage or insurance costs, and there can be benefits of holding the asset, like convenience yield. The exact formula depends on context, but the basic point is: forward prices reflect cost of carry and financing, not prophecy.

### Leverage

Now leverage.

Leverage means large economic exposure with relatively little cash up front.

With a forward, you can get almost full price exposure without paying the full price up front. That’s leveraged relative to buying the asset today.

This is a theme you’ll keep seeing in derivatives and also in tax planning: the ability to shift cash flows in time while preserving exposure.

---

## PART 3: Futures and swaps (6 minutes)

Futures are basically standardized forwards traded on an exchange.

The practical differences:
- Futures require margin.
- Futures are marked-to-market daily. Gains and losses are realized daily through margin adjustments.
- Futures reduce counterparty credit risk through clearing.

For class purposes, when you see futures, think: it’s the forward payoff, but with institutional structure that changes credit and liquidity risk.

Swaps.

A swap is typically a series of forward-style settlements over time.

Instead of one final settlement at maturity, the parties net payments periodically.

So if Debbie and Larry want to bet on gold price changes but they want to settle each year, not at the end of two years, they can structure a swap: two one-year periods with net cash settlement each year.

You can think of a swap as a strip of forwards, or a forward with periodic settlement and netting.

---

## PART 4: Options (10 minutes)

Options are the other core building block, and the key difference is: right, not obligation.

In the example, gold is at $1,800.

Debbie pays Larry $40 for an option to buy gold at $1,850 any time in the next year.

That’s a call option. Because it can be exercised any time during the year, it’s American-style.

Debbie is long the call. Larry is short the call. The $40 is the premium.

Now payoffs.

### If gold is $1,950

The option is in the money because Debbie can buy at $1,850 something worth $1,950.

Intrinsic value is $100.

But she paid $40. So her net gain is $100 minus $40, which is $60.

Larry received $40 and loses $100 of intrinsic value, so he is down $60.

### If gold is $1,750

The option is out of the money. Buying at $1,850 would be irrational.

So Debbie doesn’t exercise.

Her loss is limited to the premium, $40.

Larry keeps the premium.

That’s the insurance nature of options. The premium is the price of the right to walk away from losses beyond the premium.

Compare that to a forward at $1,850.

If gold goes to $1,950, a long forward gains $100.

If gold goes to $1,750, a long forward loses $100.

So the forward is symmetric. No premium, but you eat downside.

The option is asymmetric. You pay a premium, and your downside is capped.

Now the question “if Larry thinks gold will fall, what option should he buy?”

He buys a put. A put gives him the right to sell at a fixed strike. If price falls, the put becomes valuable.

Now replication, which is one of the key cold-call targets.

A long forward at strike K can be replicated by:
- long a call at strike K, maturity T
- short a put at strike K, maturity T

Intuition: the call gives you upside above K. The short put forces you to take downside below K. Together that produces a linear payoff around K, which is what a forward gives you.

### Leverage ranking

Most leveraged is typically the call option, because a small premium gives you exposure to potentially large upside.

Forward is next, because you have full linear exposure with little or no upfront payment.

Least leveraged is direct ownership, because you pay full price now.

### The bull call spread question

If Debbie thinks gold will rise from $1,800 to $2,000 but not higher, and she wants limited risk and low cost, the move is a call spread.

Buy a call with a lower strike and sell a call with a higher strike.

That reduces the net premium. It caps upside at the higher strike. Loss is limited to the net premium. It’s exactly designed for “moderate upside with low cost.”

---

## PART 5: Volatility and why options get more valuable (4 minutes)

Now the Debbie versus Mimi question.

Debbie believes there is a 50% chance gold is $1,900 and 50% chance it is $1,700. The expected value is $1,800.

Mimi believes there is a 50% chance gold is $2,300 and 50% chance it is $1,300. The expected value is also $1,800.

So for buying gold today, they should pay the same in expectation.

But for a call option, Mimi should pay more.

Reason: options are convex. The payoff increases more on the upside than it decreases on the downside because downside for the option buyer is capped at the premium.

More volatility increases the expected payoff of a convex function. That’s the clean mathematical fact behind why volatility makes options more valuable.

---

## COLD CALL PREP (3 minutes)

If you’re asked “forward versus option”:

Answer starter: “A forward is an obligation with symmetric payoff; a call option is a right that caps downside at the premium and keeps upside.”

If you’re asked to replicate a forward:

Answer starter: “Long forward at strike K equals long call at K plus short put at K, same maturity.”

If you’re asked why Mimi pays more for the call:

Answer starter: “Because options are convex; higher volatility increases expected option value even when expected price is unchanged.”

---

## 60‑SECOND RECAP (1 minute)

> A forward is linear exposure. An option is convex exposure.
>
> Long means you benefit if the underlying rises; short means you benefit if it falls.
>
> Forward prices reflect financing and carry more than prediction.
>
> Higher volatility increases option value because convexity makes dispersion valuable.

---

## CLOSING (1 minute)

Go into class ready to compute payoffs quickly and to say, out loud, which side is long and which side is short. That’s most of what you’ll be asked today.

---

## SOURCE NOTE
- Syllabus: `01_SOURCES/syllabus/Class 13 Derivatives The Basic Building Blocks Panel 3/Dealsdiscussion.13-4.md`
- Class reference: `02_PREP/text/2026-04-15_class13_text.md`
