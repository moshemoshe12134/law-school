# Class 14 Prep Sheet: Derivatives — Hedging and Tax Planning (Panel 1)

**Course:** Deals  
**Topic:** Hedging vs speculation; how derivatives transfer risk; present value and tax deferral; straddles and IRC §1092  
**Date:** 2026-04-22

---

## Key Concepts Overview

Two uses of derivatives dominate this class:
- **Hedging:** transfer a risk you already have and don’t want.
- **Tax planning:** exploit timing rules (especially deferral) using derivative design.

Key cross-cutting theme:
- If a strategy produces **no pretax economic gain** but creates a tax benefit, the tax system will try to attack it with **matching rules** (recognize losses only when offsetting gains are recognized).

---

## I. Hedging

### 1. Hedging vs speculation

- **Hedging:** you are already exposed to a risk; you use a derivative to reduce/transfer that exposure.
- **Speculation:** you are not exposed (or you increase exposure) because you want the risk and its payoff profile.

Same instrument can do either; it depends on the user’s pre-existing exposure.

### 2. Hurricane-contingent bond (CAT-style payoff)

#### 2A. Why would an investor buy it?

Possible reasons:
- **Speculation:** investor wants exposure to hurricane risk.
- **Diversification:** payout tied to weather index may be less correlated with stock market returns.
- **Yield:** investors may demand higher expected returns for bearing nontraditional/uncertain risk.

#### 2B. Why would issuer issue it? Especially attractive for whom?

Issuer motive is often **hedging**:
- If issuer’s business suffers in hurricanes (insurer, reinsurer, hotel chain, coastal utility), this bond reduces cash outflows when hurricanes hit by cutting coupon.
- It transfers catastrophe risk to investors.

---

### 3. Jane the jeweler: input-price risk in gold

Jane’s exposure:
- She needs to buy gold; rising gold prices squeeze margins.

Tools:
- **Forward/futures to buy gold at fixed price** (lock in input cost).
- **Call option on gold** (cap cost while keeping benefit if prices fall; pay premium for flexibility).

Choice depends on risk tolerance:
- If she wants certainty and can tolerate downside, forward/futures.
- If she wants protection but wants upside from price drops, options.

---

### 4. Oilco project: price uncertainty and investment decision

#### 4A. Solutions

Risk-management and structure options:
- **Hedge oil price** with forwards/futures (lock in minimum effective price).
- **Buy puts** (price floor) or use a **collar** (buy put, sell call to reduce premium).
- **Staged investment / option to expand** (delay/capex staging to learn more about price).
- **Joint venture / risk sharing** with another firm.
- **Diversification** at corporate/portfolio level.

#### 4B. Diversified shareholder: oppose vs favor hedging

Oppose:
- Shareholders can diversify/hedge on their own; firm hedging can be redundant.
- Hedging can be **agency-cost motivated** (management reducing volatility to protect jobs/comp).

Favor:
- Reduces probability of **financial distress** and underinvestment.
- Stabilizes cash flows, can lower financing costs.
- Can be a response to **asymmetric information** in external financing: outsiders may price risk conservatively; internal hedging can enable positive-NPV projects.

---

## II. Tax Deferral (present value basics)

### 5. If someone lends you $100 for a year at 10% and charges no interest, what is it worth?

At 10%, the foregone interest is **$10**.
- Borrower effectively gets the time value of using $100 for a year.

### 6. Present value of owing $100 in one year at 10%

Present value = $100 / 1.10 = **$90.91** (rounded).

### 7. Owe $100 tax this year; can pay next year instead, no interest

You save the time value of money:
- PV paid now: $100.
- PV paid next year: $90.91.
- **PV savings = $9.09.**

### 8. True/false: deferring tax reduces PV

**TRUE.**

---

## III. Straddle tax planning

### 9. Four rules (assume tax only at settlement; annual tax accounting; gains/losses symmetric at 50%)

Key lever: choose when to realize losses vs gains by closing out positions around year-end.

### 10. Ellen’s straddle: long forward + short forward, same commodity, same maturity/price

#### 10A. If commodity is $120,000 at maturity

- Long forward: **+$20,000**.
- Short forward: **−$20,000**.
- Combined: **$0 pretax**.

#### 10B. If commodity is $70,000 at maturity

- Long forward: **−$30,000**.
- Short forward: **+$30,000**.
- Combined: **$0 pretax**.

#### 10C. Close short at 11:59pm Dec 31 for −$20,000; close long at 12:01am Jan 1 for +$20,000

Combined pretax across both legs: **$0**.  
But timing differs across tax years.

#### 10D. 2022 taxable income and tax

2022:
- Wage income: $100,000.
- Realized derivative loss: −$20,000.
- Taxable income: **$80,000**.
- Tax at 50%: **$40,000**.

Without derivative loss:
- Taxable income: $100,000.
- Tax: $50,000.

**Tax reduction in 2022: $10,000.**

#### 10E. 2023 taxable income and tax

2023:
- Wage income: $100,000.
- Realized derivative gain: +$20,000.
- Taxable income: **$120,000**.
- Tax: **$60,000**.

#### 10F. What is the effect? Why valuable?

She shifted $10,000 of tax **from 2022 to 2023**.
- Pretax economics are unchanged (net $0).
- Benefit is time value of money from deferral.

At 10% interest, the PV benefit of delaying $10,000 for one year is:
- $10,000 − ($10,000 / 1.10) = **$909** (approx).

---

## IV. IRC §1092 (anti-straddle rule)

### 11A. Is Ellen’s transaction a “straddle”?

**YES.** She holds offsetting positions with substantially diminished risk of loss (long and short on same commodity exposure).

### 11B. What does §1092 do?

It limits loss recognition:
- Losses on one leg are recognized only to the extent they exceed unrecognized gains on offsetting positions.
- Otherwise, the loss is **deferred/carryforward**.

Functional effect:
- Forces **matching** of gain and loss timing.
- Blocks “harvest loss now, recognize gain later” strategies with offsetting positions.

---

## Key Takeaways

- Hedging is about transferring unwanted existing exposure; speculation is choosing exposure.
- The tax value of deferral is pure present value math.
- Straddles can create timing games without changing pretax economics.
- §1092 targets timing games by matching losses to offsetting unrecognized gains.

---

## Notes for Class Discussion

- When asked “why is this valuable,” answer in PV terms, not morality terms.
- When asked “why might shareholders oppose hedging,” lead with agency costs, then concede distress/financing benefits.

