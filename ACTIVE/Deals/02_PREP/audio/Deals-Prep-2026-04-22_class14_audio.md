---
doc_type: audio_prep
class_number: 14
date: 2026-04-22
day_of_week: Wednesday
title: Derivatives — Hedging and Tax Planning
status: draft # draft|final
time_minutes_target: 11
word_count_target: 1700
inputs:
  syllabus_assignment: 01_SOURCES/syllabus/Class 14 Derivatives Hedging and Tax Planning Panel 1/Dealsdiscussion.14.md
  class_reference: 02_PREP/text/2026-04-22_class14_text.md
  core_sources: []
notes: []
---

# Audio Prep — Class #14 — Derivatives — Hedging and Tax Planning

**Audio length: ~28 minutes | Listen before class on Wednesday, 2026-04-22**

---

## INTRO (2 minutes)

Today is derivatives used for two very different purposes: hedging and tax planning.

The throughline is that derivatives are precise tools for shaping exposure. That precision is valuable for legitimate risk management, and it’s also useful for gaming timing rules in the tax system.

By the end of this prep, you should be able to:
1. Distinguish hedging from speculation quickly.
2. Map a real business problem to a derivative-based hedge.
3. Do the present value math for tax deferral.
4. Explain how a straddle can create a timing benefit with no pretax gain, and how IRC §1092 tries to stop it.

---

## PART 1: Hedging (11 minutes)

### Hedging versus speculation

Hedging means you already have exposure to a risk, and you want to reduce it.

Speculation means you want to take on risk you don’t already have.

Same derivative, different user, different label.

### The hurricane-linked bond

Issuer needs to borrow for two years. Normal fixed rate coupon is 6%. Instead, it pays $12 if hurricane damage is low and $0 if damage is high.

Start with the investor.

Why would an investor buy it? Three plausible answers.

First, speculation. An investor might actually want a bet on hurricane outcomes. That can be because they have a view about climate risks, or because the investor wants exposure that is not easily available elsewhere.

Second, diversification. The payoff is tied to a weather index, which is not the same as equity market returns. In principle that can reduce portfolio correlation, especially for an investor whose portfolio is already heavy in traditional market risk.

Third, price. Investors will demand compensation for bearing a weird, hard-to-model risk. That shows up as a higher expected return in the bond’s terms.

Now the issuer.

Why would the issuer issue it? The issuer’s story is hedging.

If the issuer’s business suffers when hurricanes hit, a bond that pays less in hurricane years reduces the issuer’s cash outflows exactly when it is under stress.

The clean example is an insurance company with heavy exposure in Florida. In a hurricane year it pays claims and needs cash. If the bond coupon goes to zero in that year, the issuer has effectively transferred catastrophe risk to investors.

Hotels, utilities, and other hurricane-sensitive businesses can also have a similar hedging rationale, though the insurance company story is the cleanest.

### Jane the jewelry maker and gold input prices

Jane’s risk is input cost uncertainty. She needs gold to make jewelry, but she doesn’t have a view on where gold is going. Rising gold prices compress margins.

Two straightforward hedges.

One: a forward or futures contract to buy gold in the future at a fixed price. That locks in her input cost. It stabilizes margins.

Two: a call option on gold. That caps her maximum price while allowing her to benefit if gold prices fall. The premium is the price of that flexibility.

In class, the fast way to say this is: forward gives certainty but no upside if prices fall; call gives insurance-like protection with premium.

### Oilco and the decision to invest

Oilco invests $34 million now to bring a million barrels to market in one year. It’s profitable at $65, but management worries price could fall below $65.

Give several solutions, but keep them categorized.

Risk-transfer solutions:
- Sell future production forward at a price that makes the project viable.
- Buy puts on oil to create a floor.
- Use a collar by buying a put and selling a call to lower the net premium.

Deal-structure solutions:
- Stage the investment to learn more before committing full capital.
- Bring in a partner to share risk.
- Delay the project if the option value of waiting is high.

Now the shareholder question.

Why might a diversified shareholder oppose hedging?

One answer is redundancy. A diversified shareholder can diversify away firm-specific risk. They might see firm hedging as unnecessary, or as an implicit bet by management.

The more important answer is agency costs. Managers are not diversified the way shareholders are. Managers care about job security, reputation, and personal wealth tied to the firm. Hedging can be a way to reduce volatility to protect management, even if shareholders would prefer risk-taking when expected value is positive.

Why might shareholders favor hedging anyway?

Because there are real frictions at the firm level that diversified shareholders don’t fully neutralize.

Volatility can cause financial distress and underinvestment. Volatility can raise the cost of capital. External financiers may have less information than insiders, and they price risk conservatively. Hedging can stabilize cash flows and enable positive-NPV projects that might otherwise be abandoned.

So the clean answer is: hedging can be agency-cost motivated, but it can also reduce real financing and distress frictions.

---

## PART 2: Present value and deferral (6 minutes)

Now the tax part starts with plain present value math.

Assume interest rates are 10%.

If someone lends you $100 for a year and charges no interest, what is that worth? It’s worth the foregone interest: $10. You got to use $100 for a year for free.

If you owe $100 in one year, the present value is $100 divided by 1.10, which is about $90.91.

So if you can pay a $100 tax bill next year instead of this year, with no interest, you reduce the present value of the payment from $100 to $90.91. You saved $9.09 in PV terms.

That’s tax deferral. It is not magic. It’s time value of money.

---

## PART 3: The straddle strategy (11 minutes)

Now Ellen’s straddle.

Ellen earns $100,000 a year in wages. Tax rate is 50%.

She enters two offsetting forwards: a long forward and a short forward on the same commodity, same maturity, same strike.

First point: pretax, the combined position is a wash. If one leg gains, the other loses.

That’s the setup for why the tax benefit is suspicious: if there is no pretax economic gain, why is she getting a tax benefit? The answer is timing.

The assumed rule is that gains and losses are taxed when realized at settlement, and tax is computed annually with a hard year-end cutoff.

So she closes out the losing leg at the end of the year, realizes a loss in the current tax year. Then she closes out the winning leg just after midnight, realizing the gain in the next tax year.

Use the numbers from the discussion question.

Commodity is worth $120,000 at maturity.

Long forward gains $20,000. Short forward loses $20,000. Combined pretax is zero.

Now she settles early to split years.

On Dec 31 at 11:59pm, she cancels the short and pays $20,000. That is a realized loss in 2022.

On Jan 1 at 12:01am, she cancels the long and receives $20,000. That is a realized gain in 2023.

Pretax across both legs, still zero. But taxes shift.

Compute taxes.

In 2022, wage income is $100,000. She has a $20,000 derivative loss. Taxable income is $80,000. At 50%, tax is $40,000.

Without the loss, tax would be $50,000.

So she reduced tax this year by $10,000.

Then in 2023, wage income is $100,000 and she has a $20,000 derivative gain. Taxable income is $120,000. Tax is $60,000.

So she pays $10,000 more next year.

Net tax over two years is unchanged. The benefit is that she kept $10,000 for an extra year.

At 10%, the PV benefit of delaying $10,000 for one year is:

$10,000 minus $10,000 divided by 1.10, which is about $909.

That’s the tax planning value of the straddle under these simplified assumptions.

---

## PART 4: IRC §1092 (4 minutes)

Section 1092 exists because Congress doesn’t want you manufacturing losses now while parking gains for later when the underlying economics are offsetting.

A straddle is defined as offsetting positions with a substantial diminution of risk of loss. A long and short forward on the same commodity exposure is exactly that.

Then the rule limits recognizing the loss. You can recognize a loss only to the extent it exceeds unrecognized gains in offsetting positions. Otherwise, the loss is deferred and carried forward.

Translate that into plain English:

You can’t take the loss now if you’re still sitting on an offsetting gain. The system forces matching of the gain and loss timing, which kills the timing arbitrage.

---

## COLD CALL PREP (3 minutes)

If asked “why is the strategy valuable,” answer in PV terms:

Answer starter: “It defers tax from this year to next year, which reduces the present value of tax by the time value of money.”

If asked “why might shareholders oppose hedging,” lead with agency cost:

Answer starter: “Managers are underdiversified and may hedge to protect jobs; shareholders may see it as agency cost, though hedging can reduce distress costs and help finance good projects.”

If asked what §1092 does:

Answer starter: “It limits recognizing losses on a straddle until offsetting gains are recognized, forcing timing matching.”

---

## 60‑SECOND RECAP (1 minute)

> Hedging transfers a risk you already have; speculation takes on a risk you want.
>
> Tax deferral is present value math.
>
> Straddles can create timing benefits without pretax gain by realizing losses now and gains later.
>
> IRC §1092 attacks that by matching losses to unrecognized offsetting gains.

---

## CLOSING (1 minute)

For class, stay disciplined about two things: (1) what is the underlying exposure and who is bearing it, and (2) is there any pretax economic gain, or is the value purely timing. That framing gets you through both the hedging and tax halves.

---

## SOURCE NOTE
- Syllabus: `01_SOURCES/syllabus/Class 14 Derivatives Hedging and Tax Planning Panel 1/Dealsdiscussion.14.md`
- Class reference: `02_PREP/text/2026-04-22_class14_text.md`
