# Class 13 Prep Sheet: Derivatives — The Basic Building Blocks (Panel 3)

**Course:** Deals  
**Topic:** Derivatives as contracts that repackage risk: forwards/futures/swaps and options; leverage; replication; why volatility matters  
**Date:** 2026-04-15

---

## Key Concepts Overview

Derivatives are contracts whose value is tied to some underlying variable (price of gold, interest rate, weather index, etc.). They let parties:
- **Hedge:** shed a risk you already have.
- **Speculate:** take on a risk you want.
- **Engineer payoffs:** design exposure very precisely (which is why they show up in tax planning).

Core building blocks:
- **Forward:** obligation to buy/sell later at fixed price.
- **Futures:** standardized forward with margin + daily settlement.
- **Swap:** series of forward-style settlements (periodic netting).
- **Option:** right, not obligation (call = buy; put = sell).

Core payoff intuition:
- **Forwards are linear** (symmetric upside/downside).
- **Options are convex** (limited downside for buyer; upside retained), so **volatility increases option value**.

---

## I. Forward Contracts and Swaps

### 1. What is a derivative?

**Derivative:** a contract whose value derives from an underlying asset, rate, index, or event.
- It reallocates risk between counterparties.
- Payoffs are often close to **zero-sum** between the parties (ignoring transaction costs and market-wide effects).

### 2. Difference between “long” and “short”

- **Long:** benefits when the underlying value goes up (exposure to increase).
- **Short:** benefits when the underlying value goes down (exposure to decrease).

### 3. What is a forward?

**Forward contract:** bilateral agreement to buy/sell an underlying asset at a fixed future date for a fixed price.
- No choice: both sides are obligated (unlike options).

### 4. Gold forward: spot $1,800 (June 1, 2022); forward buy June 1, 2024 at $1,900

#### 4A. Who is long? Who is short?

- Debbie agrees to **buy** at a fixed price later → **Debbie is long** (long forward).
- Larry agrees to **sell** later → **Larry is short** (short forward).

#### 4B. If spot in June 2024 is $2,100, what are the consequences?

Debbie:
- Pays $1,900 for an ounce worth $2,100.
- **Economic gain = $2,100 − $1,900 = $200.**

Larry:
- Must deliver an ounce worth $2,100 for $1,900.
- **Economic loss = $200.**

(Larry’s decision to buy gold earlier affects his total economics, but the forward’s settlement logic is still “spot minus forward price” at maturity.)

#### 4C. If spot in June 2024 is $1,500, what changes?

Debbie:
- Pays $1,900 for an ounce worth $1,500.
- **Economic loss = $1,900 − $1,500 = $400.**

Larry:
- Delivers an ounce worth $1,500 for $1,900.
- **Economic gain = $400.**

#### 4D. Cash settlement vs physical settlement

- **Physical settlement:** Larry delivers gold; Debbie pays $1,900.
- **Cash settlement:** no gold changes hands; the out-of-the-money party pays the net difference.
  - If spot is $2,100: Larry pays Debbie **$200**.
  - If spot is $1,500: Debbie pays Larry **$400**.

### 5. Why is the forward price > spot? Is it because parties predict price will rise?

#### 5A. Why $1,900 when spot is $1,800?

Not primarily prediction. The forward price reflects the **cost of carry**:
- If you postpone paying for the asset, you keep your money longer (time value).
- A rough intuition: the forward embeds an interest component (plus storage/insurance/benefits of holding the asset, if relevant).

#### 5B. What is leverage?

**Leverage:** large economic exposure with little upfront cash.
- Forwards can be leveraged because you lock in exposure now without paying full price now.

#### 5C. What’s more leveraged: buying the stock today or entering a forward?

**Forward is more leveraged** (less upfront cash for similar exposure).

### 6. Futures and swaps

#### 6A. Futures contract

**Futures:** standardized forward traded on an exchange with:
- margin requirements,
- daily marking-to-market (gains/losses settled daily),
- reduced counterparty credit risk via clearing.

#### 6B. What is a swap? Cash vs physical settlement? All at once or periodic?

**Swap:** a contract exchanging cash flows based on an underlying (e.g., fixed vs floating interest) over time.
- Typically **cash settled** via net payments.
- Settled **periodically**, not just once at maturity.

#### 6C. Two one-year bets, no physical delivery: what derivative fits?

**Swap** (or equivalently, a strip of forwards settled annually).
- They can structure a two-period swap with annual net settlement tied to gold price changes.

---

## II. Options

### 7. Call option: spot $1,800; Debbie pays $40 for option to buy at $1,850 within a year

#### 7A. What is the option called? American or European?

- Debbie’s option to **buy** is a **call option**.
- “At any time in the next year” = **American-style**.

#### 7B. What is Larry’s position? What is the $40 payment called?

- Larry sold the call → **short call** (writer of the call).
- $40 is the **premium**.

#### 7C. If gold is $1,950 in one year: economic result?

Debbie:
- Exercises: buys at $1,850, values at $1,950.
- Intrinsic value = $100; net of premium = **$100 − $40 = $60 gain**.

Larry:
- Receives $40 premium; loses $100 intrinsic.
- **$40 − $100 = −$60 (loss)**.

#### 7D. If gold is $1,750 in one year: economic result?

Debbie:
- Does not exercise (would buy in market instead).
- **Loss limited to premium: −$40**.

Larry:
- Keeps premium.
- **+$40**.

#### 7E. Compare to a forward at $1,850 when spot is $1,800

Forward is an obligation:
- If gold is $1,950: **gain $100** (no premium).
- If gold is $1,750: **loss $100** (you’re locked in).

Option is asymmetric:
- Upside, but downside capped at premium.
- You pay premium for that downside protection.

### 8. Larry thinks gold will decline: what option should he buy?

**Buy a put option** (right to sell at a fixed strike).

### 9. Replicate a forward using options (synthesize a forward)

To replicate a **long forward** at strike K:
- **Buy a call** at strike K, maturity T (long call)
- **Sell a put** at strike K, maturity T (short put)

This combination gives linear exposure like a forward.

### 10. Leverage ranking: spot gold vs forward vs call option

Most leveraged → least:
1. **Call option** (small premium for large upside exposure)
2. **Forward** (near-zero upfront for full linear exposure)
3. **Direct investment** (pay full price up front)

### 11. Debbie thinks gold rises from $1,800 to $2,000 but no higher; wants low cost and limited risk

Use a **bull call spread**:
- Buy a call with lower strike (e.g., $1,850 or $1,800).
- Sell a call with higher strike (e.g., $2,000).

Effect:
- Lower net premium.
- Gains capped at the upper strike; losses capped at net premium.

### 12. How does option price change if…

#### 12A. Option life extends from 1 year to 3 years

**Premium increases.** More time = more chance to end up in the money.

#### 12B. Spot moves from $1,800 to $1,799 (or $1,801)

For a $1,850 strike call that is currently out-of-the-money:
- The premium changes by **less than $1** for a $1 move in spot (low delta).
- The closer spot is to strike, the more sensitive (delta increases).

### 13. Debbie vs Mimi: same expected price, different volatility

Debbie believes: 50% $1,900, 50% $1,700 (EV = $1,800).  
Mimi believes: 50% $2,300, 50% $1,300 (EV = $1,800).

#### 13A. Who pays more for gold today?

**Same (in expectation).** Both valuations have the same expected future price, so both are willing to pay about $1,800 (ignoring risk preferences).

#### 13B. Who pays more for a call option to buy gold at $1,800?

**Mimi pays more.** Higher volatility increases the value of convex payoffs:
- options benefit from upside but truncate downside (limited to premium),
- more dispersion increases expected option payoff.

---

## Key Takeaways

- **Forward = linear exposure**; **option = convex exposure**.
- **Forward price > spot** mainly because of time value/carry, not prophecy.
- **Swaps** are periodic net-settlement versions of forward-like exposure.
- **Volatility increases option value** even when expected price is unchanged.

---

## Notes for Class Discussion

- Always state payoffs as “intrinsic value minus premium” for options.
- Be ready to explain forward replication: **long call + short put** (same strike/maturity).
- Volatility intuition: options are valuable because they let you keep upside while limiting downside.

