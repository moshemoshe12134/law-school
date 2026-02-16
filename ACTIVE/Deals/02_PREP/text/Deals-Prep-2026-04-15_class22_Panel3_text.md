# Class 22 Prep Sheet: Incentive Design (Panel 3)

**Course:** Deals
**Topic:** Moral Hazard, Incentive Compensation, and Multi-Task Problems
**Date:** 2026-04-15

---

## Key Concepts Overview

This class explores **moral hazard** - situations where one party can take actions that benefit themselves but harm another party, and those actions are hard to observe or verify. We'll examine how to design contracts and incentives to align interests when performance is difficult to monitor.

**Core themes:**
- **Moral hazard vs. adverse selection:** Moral hazard is about hidden *actions* (what people do after the deal); adverse selection is about hidden *information* (what people know before the deal)
- **Observable vs. verifiable performance:** Some things you can see but can't prove in court - this limits what contracts can cover
- **Risk-sharing incentives:** Paying for performance creates motivation but also shifts risk to the party being incentivized
- **Multi-task incentive problems:** When you reward one measurable outcome, people may neglect other important but harder-to-measure tasks
- **Leverage and risk-taking:** Debt can encourage equity holders to take excessive risks because they get upside but limited downside

---

## Question 1: Introduction to Moral Hazard

### A. What term do economists use to describe performance that is hard to observe?

**Non-verifiable performance** or **moral hazard**.

**Moral hazard** occurs when one party's actions are:
- **Hidden** (not observable by the other party), OR
- **Observable but not verifiable** (you can see it, but you can't prove it in court)

This makes it difficult or impossible to write contracts that directly punish bad performance or reward good performance.

### B. Even when performance is hard to observe, why might parties perform anyway? (Hint: the answer is not rooted in contract.)

**Reputation and repeat dealings.**

Even without enforceable contracts, parties may perform because:
- They want to maintain a **good reputation** in the market
- They expect **future transactions** with the same counterparty
- They value **trust relationships** that will be damaged if they shirk
- There are **social norms** or **internal motivations** (pride, professionalism)

The shadow of the future can be more powerful than legal enforcement.

### C. How is moral hazard different from adverse selection?

Both are information problems, but they occur at different times:

**Adverse selection (hidden information):**
- Occurs **before** the transaction
- One party knows something about themselves or the deal that the other doesn't
- Example: A used car seller knows the car is a lemon; the buyer doesn't
- Solution: Due diligence, signaling, screening

**Moral hazard (hidden action):**
- Occurs **after** the transaction
- One party takes actions the other can't monitor
- Example: After buying insurance, you drive less carefully
- Solution: Incentives, monitoring, collateral, debt-like features

**Key distinction:** Adverse selection is about what you *know*; moral hazard is about what you *do*.

### D. Adam is CEO of XYZ, a public company. CEO comp tends to rise with the size of the company. Adam has the opportunity for XYZ to acquire ABC. What is the potential for moral hazard here?

**Adam may overpay for ABC to increase company size (and his compensation), even if the acquisition destroys value for shareholders.**

This is a classic agency cost problem:
- **Adam's incentive:** Larger company → higher CEO compensation
- **Shareholders' interest:** Only acquire ABC if it increases value per share
- **Moral hazard:** Adam can pursue size over value, and it's hard for shareholders to prove the acquisition was a bad idea (ex ante, many acquisitions are uncertain)
- **Information asymmetry:** Adam knows more about the acquisition rationale and process than shareholders

**Possible solutions:**
- Performance-based compensation tied to **stock price** (not just company size)
- Shareholder voting on large acquisitions
- Independent board committee to review acquisitions
- Require Adam to hold significant stock (so he loses value if he overpays)

---

## Question 2: Biotech Startup and Big Pharma - Royalties vs. Fixed Payments

Betty is founder and CEO of a biotech startup seeking to cure Disease. Big Pharma ("BP") provides $50 million. In return, if Betty develops a cure, BP gets a mandatory license to commercialize the drug and receives 15% of revenue from selling the cure.

### A. Why didn't BP simply buy the idea from Betty? What problems make this structure more appealing?

**Buying the idea outright creates adverse selection and moral hazard problems:**

**Adverse selection problem:**
- Betty knows more about the true prospects of the cure than BP does
- If BP pays a fixed price upfront, Betty might overstate the likelihood of success
- BP would overpay for weak ideas and underpay for strong ones (but can't tell the difference)

**Moral hazard problem:**
- After BP buys the idea, Betty would have no incentive to continue working hard
- The success of a biotech cure depends heavily on Betty's ongoing effort and expertise
- If BP pays upfront, Betty might shirk or move on to other projects

**The royalty structure solves both:**
- **Royalties align incentives:** Betty only gets paid if she succeeds
- **Betty keeps "skin in the game":** She works hard because her payoff depends on success
- **BP pays for success, not promises:** BP only pays significant amounts if the cure works

### B. Why didn't BP offer a fixed price to Betty's startup, instead of sharing royalties?

**A fixed price would create moral hazard - Betty would have less incentive to work hard.**

With a **fixed price:**
- Betty gets paid the same amount whether she works hard or slacks off
- She might abandon the project if she gets a better offer
- BP bears all the risk if the cure fails

With **royalties:**
- Betty's compensation is tied to the drug's actual success
- She has ongoing incentive to maximize the cure's commercial potential
- Risk is shared: BP pays more only when there's revenue to share

### C. Annual revenue is $10 million. BP has limited cash. Instead of investing in Betty's cure, BP could put money into drug DD, which BP developed itself and expects to generate $9.5 million of annual revenue. Which is BP likely to favor?

**BP will likely favor its own drug DD, even though Betty's cure generates more revenue ($10M vs. $9.5M).**

**Why?**
- **BP's share of Betty's cure:** 15% × $10M = **$1.5 million**
- **BP's share of its own drug DD:** 100% × $9.5M = **$9.5 million**

The royalty structure creates a conflict of interest:
- BP will prioritize projects where it keeps 100% of the upside
- Betty's cure is "worth more" economically ($10M > $9.5M), but BP captures less of that value
- This is a **moral hazard problem**: BP may under-promote Betty's cure or allocate fewer resources to it

### D. To address this issue, is it better to have a larger up-front payment or a larger royalty?

**A larger royalty is better for aligning incentives, but there's a trade-off.**

**Larger royalty (e.g., 50% instead of 15%):**
- **Pro:** BP gets more of the upside → more incentivized to promote the cure
- **Pro:** Better alignment of BP and Betty's interests
- **Con:** Betty keeps less of the upside → weaker incentive for her to work hard
- **Con:** 50% royalty might make the deal unattractive to Betty

**Larger up-front payment:**
- **Pro:** Betty gets more cash upfront → reduces her risk
- **Pro:** Might make the deal more attractive to Betty if she's risk-averse
- **Con:** Creates moral hazard - Betty gets paid regardless of future effort
- **Con:** BP might overpay if the cure fails

**Optimal structure:**
- Balance the split so both parties have strong incentives
- Use staged payments (some upfront, more on milestones, royalties on commercialization)
- Consider making BP's royalty increase if they hit certain promotional targets

### E. Are there other potential responses? (Hint: how can the visibility of BP's actions be increased?)

**Yes - increase monitoring and information flow to reduce moral hazard.**

**Possible solutions:**

1. **Reporting requirements:**
   - BP must report quarterly on its promotional activities, sales force allocation, marketing spend
   - Betty can verify BP is putting adequate effort behind the cure

2. **Milestone-based payments:**
   - BP receives higher royalty rates only if they hit sales targets
   - This aligns incentives: BP works harder → higher royalty → more revenue for both

3. **Minimum effort commitments:**
   - Contract requires BP to spend at least $X on marketing, or employ Y salespeople on the cure
   - If BP fails to meet these, Betty can license to someone else

4. **Competition clause:**
   - Betty can license to other pharma companies if BP underperforms
   - This threat disciplines BP to promote the cure adequately

5. **Joint venture or co-promotion:**
   - Instead of a pure license, BP and Betty form a joint venture
   - Betty has more visibility into BP's actions and more control

6. **Transparency and access:**
   - Betty gets access to BP's sales data, marketing plans, and distribution channels
   - Regular meetings to review performance

**Key insight:** When you can't perfectly align incentives with financial structure alone, you can use **monitoring and reporting** to reduce information asymmetry and moral hazard.

---

## Question 3: Leverage and Risk-Taking - Christine and Debtor Co

Christine is CEO of Debtor Co and owns all its equity (worth $25 million). Emma has lent Debtor Co $50 million. Christine considers a deal with:
- 40% chance of doubling Debtor Co's total value to $150 million
- 60% chance of reducing its value to $0

### A. Is the expected value of this deal positive or negative overall?

**Positive.**

**Expected value calculation:**
- Success case (40%): $150 million
- Failure case (60%): $0 million
- **Expected value = (0.40 × $150M) + (0.60 × $0M) = $60 million**

Since the current total value is $75 million ($50M debt + $25M equity), the expected value would increase from $75M to $60M... wait, that's a decrease.

Let me recalculate:
- **Current value:** $50M (debt) + $25M (equity) = **$75 million**
- **Expected value after deal:** $60 million

So the expected value is **negative overall** (-$15 million). This deal destroys value on average.

### B. For Christine in particular, is the expected value positive or negative?

**Positive for Christine!** Even though the deal destroys overall value, Christine has an incentive to take it.

**Christine's payoff calculation:**
- **Success case (40%):** Debtor Co worth $150M → Emma gets $50M (debt repaid) → Christine gets **$100M**
- **Failure case (60%):** Debtor Co worth $0 → Emma gets $0 → Christine gets **$0**
- **Christine's expected value = (0.40 × $100M) + (0.60 × $0M) = $40 million**

**Current equity value:** $25 million

So Christine's expected value increases from $25M to $40M - a **$15 million gain** for her, even though total firm value falls by $15M!

**Emma's payoff:**
- **Success case (40%):** Gets $50M (loan repaid)
- **Failure case (60%):** Gets $0 (default)
- **Emma's expected value = (0.40 × $50M) + (0.60 × $0M) = $20 million**

**Current loan value:** $50 million

Emma loses $30M in expected value. Christine gains $15M. Total loss: $15M.

### C. Generalizing from this example, how can leverage produce moral hazard for equity holders?

**Leverage (debt) creates asymmetric payoffs that encourage equity holders to take excessive risks.**

**The mechanism:**
1. **Debt holders have fixed upside** (interest/principal) but bear substantial downside risk
2. **Equity holders have unlimited upside** but limited downside (they can only lose their investment - they have limited liability)
3. When a company is highly leveraged, equity holders are effectively **playing with borrowed money**
4. If a risky bet pays off, equity holders capture most of the upside
5. If it fails, debt holders bear most of the loss (equity holders just lose whatever equity they had left)

**This is moral hazard:**
- Christine (equity holder) takes risks that benefit her but harm Emma (debt holder)
- Emma can't fully control or monitor Christine's investment decisions
- Christine may prefer "negative expected value" projects as long as they have high upside (option value)

**Real-world examples:**
- **Financial crisis 2008:** Banks took excessive risks because they were highly leveraged (playing with borrowed money)
- **Distressed companies:** Shareholders may approve "Hail Mary" strategies that are bad on average but have a small chance of huge success
- **Real estate:** Someone with 5% down payment takes more risks than someone with 50% down

**Solutions:**
- **Debt covenants:** Restrict risky investments, require maintenance of certain financial ratios
- **Monitoring:** Lenders get board seats or approval rights for major investments
- **Convertible debt:** Lenders participate in upside if the gamble pays off
- **Personal guarantees:** Equity holders pledge personal assets (so they bear downside risk)

---

## Question 4: How Insurance Companies Address Moral Hazard

In insurance contracts, how do insurance companies address moral hazard?

**Insurance creates moral hazard:** Once you're insured, you might take more risks (drive faster, smoke more, be less careful) because you don't bear the full cost of bad outcomes.

**Insurance companies use several tools to reduce moral hazard:**

### 1. **Deductibles and Co-Payments**
- **Deductible:** You pay the first $X of any loss (e.g., first $500 of car damage)
- **Co-pay:** You pay a percentage of each claim (e.g., 20% of medical bills)
- **Effect:** You still bear some cost of bad outcomes → still have incentive to be careful
- **Trade-off:** Higher deductibles = lower premiums (because moral hazard is reduced)

### 2. **Coverage Limits and Caps**
- **Maximum payout:** Insurance won't pay more than $X (e.g., $500K liability limit)
- **Effect:** You can't be fully careless - you'll still be on the hook for losses above the cap
- **Example:** Umbrella insurance, malpractice caps

### 3. **Exclusions and Conditions**
- **Excluded activities:** Insurance doesn't cover risky behaviors (e.g., drunk driving, using your car for racing)
- **Conditions:** You must take certain precautions (e.g., install smoke alarm, get regular health checkups)
- **Effect:** Reduces the worst moral hazard behaviors

### 4. **Risk-Based Pricing**
- **Premiums reflect risk:** Safer drivers pay less; risky drivers pay more
- **Discounts for precautions:** Lower premium if you take safety measures (alarm system, non-smoker)
- **Effect:** Gives you financial incentive to reduce risk

### 5. **Monitoring and Inspection**
- **Verification:** Insurance company checks that you're following rules (e.g., home inspection, health questionnaire)
- **Telematics:** Some auto insurers install devices to monitor driving speed and habits
- **Effect:** Reduces information asymmetry - insurer can observe your behavior

### 6. **Experience Rating**
- **Claims history affects premiums:** If you make many claims, your premium goes up
- **No-claims bonus:** Premium decreases if you don't make claims for several years
- **Effect:** You pay more if you act recklessly (and file claims)

### 7. **Coinsurance**
- **Shared risk:** You pay a percentage of each loss
- **Example:** Health insurance with 80/20 coinsurance - insurer pays 80%, you pay 20%
- **Effect:** Aligns incentives - you still feel the cost of claims

### 8. **Cancellation and Non-Renewal**
- **Threat:** Insurer can drop you if you make too many claims or act recklessly
- **Effect:** You want to keep your insurance → you moderate risky behavior

**Key insight:** Insurance companies use **partial risk-bearing** by the insured person. Instead of fully eliminating risk (which would create massive moral hazard), they share risk so you still have some skin in the game.

---

## Question 5: Challenges of Using Financial Incentives

In principle, parties should try to introduce financial incentives to head off moral hazard. K&S say this is challenging. Why?

**Designing effective incentive compensation is difficult because of several fundamental problems:**

### 1. **Measurement Problems**
- **Performance is hard to measure:** Many jobs have outputs that are difficult to quantify (teacher quality, research scientist effectiveness, managerial skill)
- **Multiple dimensions:** Success has many facets, and incentives may only capture some (test scores vs. critical thinking; short-term profits vs. long-term value)
- **Time lags:** Results may not be visible for years (R&D, education, legal cases)

### 2. **Risk and Risk Aversion**
- **Incentives shift risk:** When you tie pay to performance, you transfer risk from the principal to the agent
- **Risk-averse workers demand compensation:** "Pay me more for bearing this uncertainty"
- **Trade-off:** Stronger incentives = more risk = higher total compensation cost
- **Some workers can't bear risk:** People with mortgages, families, or limited savings may prefer stable, lower pay than risky, high-variance pay

### 3. **Multi-Task Incentive Problems (see Question 8)**
- **Measureable vs. unmeasureable tasks:** Incentives based on what you can measure cause neglect of what you can't
- **Gaming the system:** Workers focus on hitting the metric rather than doing good work
- **Example:** Teachers "teaching to the test" instead of fostering broader learning

### 4. **Luck vs. Skill**
- **Noisy performance measures:** Results depend on factors outside the worker's control (market conditions, random events, other people's work)
- **Unfairness:** Workers get penalized for bad luck or rewarded for good luck
- **Demotivation:** If pay feels random, workers may disengage

### 5. **Short-Term vs. Long-Term**
- **Time horizon mismatch:** Incentives often reward short-term results (quarterly earnings) at the expense of long-term health (R&D investment, customer loyalty)
- **Example:** CEO cutting costs to boost this year's bonus, even though it harms the company's future

### 6. **Coordination and Teamwork**
- **Individual incentives sabotage collaboration:** "Why should I help you if I get paid based on my performance alone?"
- **Free rider problems:** In teams, some people coast while others do the work
- **Team incentives** can create free riding; **individual incentives** can undermine cooperation

### 7. **Unintended Consequences**
- **Campbell's Law:** "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor"
- **Examples:**
  - Police ticket quotas → focus on minor offenses instead of serious crime
  - Surgeons paid per procedure → unnecessary surgeries
  - Lawyers paid by the hour → inefficient work and padding hours

### 8. **Principal-Agent Information Asymmetry**
- **The principal knows less than the agent:** The worker often knows better what constitutes good performance
- **Hard to write complete contracts:** Can't anticipate every contingency or measure every dimension of performance
- **Subjective evaluations:** May introduce bias or favoritism

**Key insight:** Incentives are powerful but dangerous. Poorly designed incentives can make things worse by:
- Encouraging gaming and cheating
- Undermining intrinsic motivation
- Distorting priorities
- Creating unintended consequences

**The challenge:** Design incentives that **align interests** without creating **perverse incentives** or imposing **excessive risk** on workers.

---

## Question 6: Frank the Salesman - Salary vs. Commission

Frank is a salesman. He would rather earn a fixed salary, but his employer wants to pay him on commission.

### A. What is the advantage of the commission structure?

**Commission aligns Frank's incentives with the employer's interests.**

**Advantages:**

1. **Effort motivation:**
   - Frank works harder because more effort = more sales = more pay
   - He self-motivates; the employer doesn't need to monitor him closely
   - He seeks out sales opportunities proactively

2. **Self-selection:**
   - Confident, skilled salespeople choose commission (they know they'll earn more)
   - Less skilled, lazy salespeople choose salary
   - This helps the employer attract and retain high performers

3. **Flexibility and cost control:**
   - Employer's labor costs automatically adjust to sales revenue
   - In bad months, payroll is lower (reducing fixed costs)
   - In good months, Frank is rewarded and employer earns more

4. **Information revelation:**
   - Commission reveals Frank's true ability and confidence
   - If Frank insists on salary, he may be signaling that he's not confident in his sales ability

5. **Reduced monitoring costs:**
   - Employer doesn't need to supervise Frank's effort
   - Frank monitors himself (he wants to earn more)

**Key economic logic:** When effort is hard to monitor, pay based on results. Commission transforms Frank from an agent who needs supervision into a quasi-entrepreneur who monitors himself.

### B. Why is Frank potentially unhappy with it? What might he demand in return?

**Frank is unhappy because commission shifts risk from employer to employee.**

**Why Frank prefers salary:**

1. **Income instability:**
   - Commission income fluctuates month to month
   - Bad months (economic downturn, slow season) mean low pay
   - Frank has bills (rent, mortgage, groceries) that don't fluctuate with sales

2. **Risk aversion:**
   - Most people prefer stable, predictable income over variable, risky income
   - Even if expected pay is the same, risk-averse people prefer the sure thing

3. **Factors outside Frank's control:**
   - Sales depend on product quality, marketing, pricing, economy - not just Frank's effort
   - Frank can work hard and still have a bad month

4. **Stress and anxiety:**
   - Constant pressure to perform
   - Uncertainty about whether he'll earn enough to cover expenses

**What Frank might demand in return for accepting commission:**

1. **Higher total expected compensation:**
   - "If you want me to bear risk, pay me more on average"
   - Commission structure should have higher expected pay than salary

2. **Draw or guaranteed minimum:**
   - **Draw:** Employer advances Frank money against future commissions (he doesn't earn more until he "repays" the draw)
   - **Minimum:** Guaranteed base salary + lower commission rate (hybrid model)
   - This provides some income stability while preserving incentives

3. **Benefits and perks:**
   - Health insurance, retirement contributions, car allowance, expense account
   - These reduce Frank's personal financial risk

4. **Leads and support:**
   - Employer provides good leads, marketing materials, product training
   - Reduces the risk that Frank will fail due to lack of support

5. **Uncapped commissions:**
   - No limit on how much Frank can earn
   - If he has a great month, he keeps all the upside

6. **Territory or product exclusivity:**
   - Frank gets exclusive access to certain customers or products
   - Reduces competition and increases his chance of success

7. **Longer commission cycles:**
   - Commissions on recurring sales (subscriptions, renewals)
   - Provides ongoing income from past effort

### C. In principle, might it be worth it for Frank's employer to pay him extra as a way to induce him to take more risk?

**YES - this can be a win-win.**

**Why employer might pay Frank extra to accept commission:**

1. **Effort gains outweigh extra pay:**
   - If commission motivates Frank to work 50% harder, and employer pays him 20% more, employer still wins
   - Example: Salary = $50K, Frank generates $100K in sales
     - Commission = $70K expected, Frank generates $200K in sales
     - Employer pays $20K more but gains $100K more revenue

2. **Self-selection benefit:**
   - Higher pay attracts better salespeople
   - Confident, skilled salespeople choose commission over salary at competitor firms
   - Employer gets better talent

3. **Risk-bearing cost:**
   - Employer may be **less risk-averse** than Frank (large company vs. individual)
   - Employer can diversify risk across many salespeople
   - Employer has deeper pockets and better access to credit
   - So it's economically efficient for Frank to bear some risk

4. **Variable cost structure:**
   - Commission turns fixed costs (salary) into variable costs
   - Employer's costs automatically adjust to revenue
   - This reduces the employer's business risk

5. **Information value:**
   - The fact that Frank is willing to accept commission reveals his confidence
   - This is valuable information about his ability

**Key insight:** The employer should be willing to pay a **risk premium** to compensate Frank for bearing income uncertainty, as long as the **incentive effect** (increased effort) creates more value than the premium costs.

**The math:**
- If commission increases Frank's output by ΔOutput
- And employer pays Frank ΔPay extra to accept commission
- Employer wins if: ΔOutput > ΔPay
- Frank wins if: ΔPay compensates for the risk he's bearing
- This is the classic "win-win" from well-designed incentives

---

## Question 7: Law Firm Compensation - Lock-Step vs. "Eat What You Kill"

Georgia is managing partner of a law firm, which traditionally has lock-step compensation. She is considering switching to an "eat what you kill" system.

### A. What advantages do you see in this change?

**"Eat what you kill" means partners are paid based on the business they bring in (hours billed, clients originated, matters managed).**

**Advantages of "eat what you kill":**

1. **Strong incentives for business development:**
   - Partners have direct financial incentive to bring in new clients
   - Partners who originate business are rewarded for their rainmaking
   - Encourages entrepreneurial behavior and client focus

2. **Effort and productivity:**
   - Partners work harder and bill more hours (they keep more of what they generate)
   - Reduces free-rider problem: no one can coast on others' efforts
   - High performers are rewarded, low performers earn less

3. **Attracts and retains rainmakers:**
   - Top billers and business generators are attracted by the upside
   - They won't leave for competitors offering better pay based on their output
   - Firm can recruit stars away from lock-step firms

4. ** Accountability and transparency:**
   - Clear link between contribution and compensation
   - Partners know exactly what they need to do to earn more
   - Reduces politicking (compensation is formula-based, not subjective)

5. **Cost control:**
   - Partner compensation is tied to revenue they generate
   - Firm's labor costs automatically adjust to performance
   - In bad years, partner pay drops (reducing fixed costs)

6. **Information revelation:**
   - Reveals which partners are truly valuable
   - Makes it easier to identify underperformers
   - Helps with promotion and termination decisions

7. **Client service:**
   - Partners incentivized to keep clients happy (repeat business = more compensation)
   - Partners more responsive to client needs (their income depends on it)

### B. What advantages do you see in the lock-step system?

**Lock-step means partners advance in lock-step based on seniority, not individual performance. All partners at the same level earn the same.**

**Advantages of lock-step:**

1. **Collaboration and teamwork:**
   - No incentive to hoard work or clients ("this is MY client")
   - Partners freely refer work to each other (they don't lose compensation)
   - Knowledge-sharing: partners train and mentor juniors without worrying about "creating competitors"

2. **Firm culture and stability:**
   - Creates a sense of partnership and equality
   - Reduces internal competition and conflict
   - "We're all in this together" mentality

3. **Long-term perspective:**
   - Partners focus on building the firm's reputation and client relationships over decades
   - No pressure to maximize short-term personal book of business
   - Partners invest in firm infrastructure, training, brand-building (benefits everyone, not just themselves)

4. **Quality and client service:**
   - Partners assign work to the best lawyer for the client, not the one who needs to hit a billable target
   - No incentive to pad hours or over-bill (compensation doesn't directly depend on hours)
   - Clients get the right lawyer for the matter, not just the one who "owns" the client

5. **Risk-sharing:**
   - Partners bear less individual risk (income doesn't fluctuate as much with personal performance)
   - Good years subsidize bad years across the partnership
   - More stable, predictable income for partners

6. **Supports non-billable contributions:**
   - Partners can do pro bono work, firm governance, training, recruiting
   - These activities are valued even if they don't directly generate revenue
   - Recognizes that a law firm needs more than just billable hours to succeed

7. **Reduces gaming and short-termism:**
   - No incentive to cherry-pick lucrative matters and avoid important but less profitable work
   - No incentive to poach other partners' clients
   - Partners focus on doing excellent work, not maximizing personal credit

8. **Easier administration:**
   - No complex calculations or disputes about who "owns" a client or matter
   - Simpler, more transparent system
   - Less time spent on compensation committee arguments

**Key trade-off:**
- **Lock-step:** Better for teamwork, long-term focus, firm culture, but weaker individual incentives
- **Eat what you kill:** Stronger individual incentives and accountability, but undermines collaboration and long-term perspective

**Real-world trend:** Most large firms moved away from pure lock-step toward hybrid systems (some base pay + performance bonus), attempting to balance incentives with collaboration.

---

## Question 8: Incentivizing Multiple Tasks

### A. Why is it so hard to design an incentive system when the goal is to motivate people to succeed at multiple tasks on multiple dimensions?

**Because you can only measure and reward what you can measure - and important dimensions of performance are often unmeasurable.**

**The multi-task incentive problem:**

1. **Measureability bias:**
   - Some tasks are easy to measure (sales volume, billable hours, test scores)
   - Others are hard to measure (quality, mentoring, long-term relationship building, creativity)
   - Incentives will focus on the measurable, causing neglect of the unmeasurable

2. **Substitution effect:**
   - Workers allocate effort to the rewarded task and away from the unrewarded task
   - Even if both tasks are important, incentives cause distortion
   - Example: Teachers rewarded for test scores → focus on test prep, neglect critical thinking

3. **Conflict between tasks:**
   - Tasks may compete for time and attention
   - Doing more of Task A means doing less of Task B
   - If you only reward Task A, Task B gets neglected

4. **Noise and luck:**
   - Performance measures are imperfect (affected by luck, other people's efforts)
   - Hard to isolate individual contribution to multi-dimensional outcomes
   - Creates unfairness and demotivation

5. **Subjectivity vs. objectivity:**
   - Objective measures are easy to turn into incentives but may capture the wrong things
   - Subjective evaluations (manager ratings) can capture broader performance but introduce bias, favoritism, and politicization

6. **Time horizon problems:**
   - Some tasks have immediate visible results; others take years to bear fruit
   - Incentives typically reward short-term results (can't wait 10 years to pay someone)
   - Long-term, strategic tasks get neglected in favor of short-term, measurable ones

7. **Complexity and cost:**
   - Designing a multi-dimensional incentive system is complicated
   - Multiple metrics can be confusing or gamed
   - Expensive to monitor and measure many different aspects of performance

**The core problem:** You get what you pay for. If you pay for X, you get X (often at the expense of Y and Z, which you also value but don't reward).

### B. Why is this a problem at a law firm?

**Lawyers have many important responsibilities, and only some are easily measured.**

**Measurable tasks (easy to incentivize):**
- Billable hours
- Revenue originated
- New clients brought in
- Cases won

**Unmeasurable but important tasks (hard to incentivize):**
- **Mentoring and training** junior lawyers
- **Knowledge management** (creating precedents, trainings, resources)
- **Pro bono work**
- **Firm governance** (serving on committees, recruiting, hiring)
- **Client relationship maintenance** (keeping clients happy, not just bringing them in)
- **Collaboration** (working effectively with other lawyers, referring work)
- **Quality of work** (not just quantity)
- **Long-term firm building** (reputation, culture, brand)

**If you pay based on billable hours:**
- Lawyers bill lots of hours (maybe padding)
- They neglect mentoring, training, firm-building (those are "non-billable")
- They hoard work (don't delegate to juniors) because delegating means losing billable hours

**If you pay based on revenue originated:**
- Lawyers focus on bringing in new clients
- They neglect client service (keeping existing clients happy)
- They don't mentor or train (time spent training is time not selling)
- They may over-promise to clients to get the business

**If you pay based on cases won:**
- Lawyers avoid risky cases (might hurt their "win rate")
- They push for settlement when they should fight (to protect their record)
- They cherry-pick easy cases and avoid complex, important but difficult matters

**The dilemma:**
- A successful law firm needs ALL of these tasks, not just the measurable ones
- But you can only easily incentivize the measurable ones
- So firms face a trade-off: incentives vs. teamwork/quality/long-term health

**Solutions:**
- **Hybrid compensation:** Base salary (lock-step) + performance bonus
- **Multiple metrics:** Reward a mix of billings, business development, and subjective evaluations of "firm citizenship"
- **Subjective adjustments:** Managing partner can reward unmeasured contributions (but introduces bias)
- **Norms and culture:** Create a culture that values mentoring, collaboration, pro bono (social incentives, not just financial)
- **Up-or-out:** Use promotion to partnership as the reward for overall excellence (not just measurable metrics)

### C. Why was it a problem to give a bonus for home runs? And a penalty for interceptions? And a bonus for completed passes?

**These are all examples of multi-task incentive problems in sports.** Each incentive created distortions because it focused on one dimension of performance while ignoring others.

**Bonus for home runs (baseball):**

**What happened:**
- Players focused exclusively on hitting home runs
- They neglected other aspects of hitting: contact, batting average, on-base percentage, moving runners over, sacrifice flies
- Players altered their swing to maximize home runs, leading to more strikeouts and lower overall hitting performance

**The distortion:**
- A home run is one type of valuable hitting outcome, but not the only one
- Singles, doubles, walks, and productive outs also contribute to winning
- By rewarding only home runs, you get players who swing for the fences and strike out a lot
- This can actually hurt the team's overall performance

**Real-world example:** In the 1990s, some players with high home run totals also had high strikeout rates and low batting averages - they weren't necessarily the most valuable hitters overall.

---

**Penalty for interceptions (football):**

**What happened:**
- Quarterbacks became overly cautious
- They refused to throw into tight coverage (even when the risk/reward was favorable)
- They checked down to short, safe passes instead of taking calculated risks downfield
- Some even intentionally threw the ball away (to avoid being credited with an interception) when they should have tried to make a play

**The distortion:**
- Interceptions are bad, but they're a risk of trying to make big plays
- Great quarterbacks sometimes throw interceptions because they're aggressive and take chances
- If you penalize interceptions heavily, you get timid quarterbacks who don't take enough risks
- This reduces the offense's big-play ability and explosiveness

**Real-world example:** Some quarterbacks with very low interception rates were criticized for being too conservative and "dinking and dunking" instead of pushing the ball downfield.

**Better approach:** Look at interception rate (interceptions per attempt), not total interceptions. A QB who throws 500 passes with 15 interceptions is better than one who throws 200 passes with 10 interceptions.

---

**Bonus for completed passes (football):**

**What happened:**
- Quarterbacks focused on completion percentage
- They threw lots of short, safe passes (screens, check-downs, dump-offs)
- They avoided risky but potentially valuable deep passes
- They padded stats with meaningless completions that didn't actually help the team win

**The distortion:**
- Completion percentage is only one aspect of quarterback performance
- Yards per attempt, touchdowns, and first downs are also important
- A 3-yard completion on 3rd-and-10 is worthless, but it counts as a "completed pass"
- By rewarding completions, you get QBs who are efficient but ineffective

**Real-world example:** Some "game manager" QBs had high completion rates but low yards per attempt and weren't considered elite because they didn't make enough big plays.

---

**General lesson from sports examples:**

You get what you incentivize. When you create a financial incentive for one measurable outcome:
- People focus on that outcome to the exclusion of others
- They game the system (find ways to get the reward without creating real value)
- They avoid risks that might hurt their metric even if those risks are worth taking
- Overall performance can suffer even as the measured metric improves

**Solutions:**
- **Composite metrics:** Combine multiple measures (QB rating, WAR in baseball) to capture overall contribution
- **Film study and subjective evaluation:** Coaches watch game film and evaluate players holistically, not just on stats
- **Team-based incentives:** Reward team performance (wins, championships) rather than individual stats
- **Context awareness:** Recognize that a 5-yard completion on 3rd-and-6 is better than a 20-yard completion on 1st-and-20 (context matters, even if the raw stat doesn't capture it)

---

## Question 9: Venture Capital - Liquidation Preferences and Exit Incentives

Elaine Entrepreneur launches a high-tech startup. Six months later, Veronica (a venture capitalist) invests $20 million for 40% of the company, implying a $50 million valuation. Veronica gets convertible preferred shares with voting control (until IPO, when shares convert to common).

### A. Review: What is the potential tax reason why Veronica's shares are convertible preferred?

**To justify a low 409A valuation for Elaine's common stock.**

**The tax strategy:**
1. **409A valuation:** Startups must get an independent valuation of their common stock
2. **If Veronica bought common stock at $50M valuation:** Common stock would be valued at ~$50M → Elaine's options would have a high strike price → she gets less upside
3. **By issuing convertible preferred to Veronica:** The company can argue that common stock is worth LESS than preferred stock
   - Preferred has special rights (liquidation preference, anti-dilution, voting control)
   - Common is "worth less" because it lacks these protections
4. **Result:** Common stock gets a lower 409A valuation → Elaine's options have lower strike price → more tax savings for Elaine when she exercises

**Key insight:** The tax benefit requires that preferred and common actually be different securities with different rights. If they were economically identical, the IRS would challenge the valuation.

### B. Veronica's shares have a "1X liquidation preference." She needs cash for another startup. Acquiror offers $21 million for the company (obviously less than the $50M implied valuation). Does Veronica have an incentive to take this deal? Will Elaine think this is a good deal?

**Veronica has a strong incentive to take the deal; Elaine will hate it.**

**Veronica's payout with 1X liquidation preference:**
- Veronica invested: $20 million
- Liquidation preference: She gets **1X her investment = $20 million** before common shareholders get anything
- Sale price: $21 million
- **Veronica gets: $20 million** (her full preference, almost all of the sale proceeds)
- **Elaine and other common shareholders get: $1 million** (what's left after Veronica is paid)

**Veronica's incentive:**
- She gets her money back ($20M)
- She can move on to her "more interesting" startup
- Even though the company is worth less than when she invested, she doesn't lose money (thanks to liquidation preference)

**Elaine's perspective:**
- The company was worth $50M when Veronica invested
- Now selling for $21M → huge loss in value
- Elaine only gets $1M (her 60% share of $1M remaining after Veronica's preference)
- She's giving up most of the upside for a tiny payout

**The conflict:** Veronica has asymmetric protection (downside protection via liquidation preference) while Elaine bears all the downside. This creates misaligned incentives on exit.

### C. In this situation, how much must Acquiror offer in order for Veronica to convert to common as part of the deal?

**Veronica will convert if the sale price exceeds $50 million.**

**Here's why:**

**If Veronica DOESN'T convert (keeps preferred):**
- She gets 1X liquidation preference = $20 million (regardless of sale price, as long as it's ≥$20M)

**If Veronica CONVERTS to common:**
- She owns 40% of the company as common stock
- She gets 40% of the sale price
- She will convert if: **40% × Sale Price > $20 million**
- Solving: **Sale Price > $20M / 0.40 = $50 million**

**At exactly $50 million:**
- Don't convert: Veronica gets $20M (1X preference)
- Convert: Veronica gets $20M (40% × $50M)
- She's indifferent

**Above $50 million:**
- Example: Sale at $60M
  - Don't convert: $20M
  - Convert: $24M (40% × $60M)
  - **Veronica converts to get $4M more**

**Below $50 million:**
- Example: Sale at $40M
  - Don't convert: $20M
  - Convert: $16M (40% × $40M)
  - **Veronica keeps preferred**

**The "conversion threshold"** is the post-money valuation: $50M. Below this, preferred acts like debt (Veronica gets her money back first). Above this, preferred converts to equity (Veronica shares proportionally in the upside).

### D. Veronica's shares have a 2X liquidation preference, and Acquiror offers $41 million. How much does Veronica get? How much do Elaine and the other shareholders get?

**Veronica gets the full $41 million. Elaine and common shareholders get $0.**

**Calculation:**
- Veronica's investment: $20 million
- **2X liquidation preference:** She gets **2 × $20M = $40 million** before common gets anything
- Sale price: $41 million

**Payout:**
- **Veronica gets:** $40 million (her 2X preference)
- **Remaining:** $1 million ($41M - $40M)
- **Elaine and common get:** $0 (because Veronica's preferred is "participating" - she gets her preference AND then participates in the remainder as if she converted)

Wait, I need to clarify whether the preferred is "participating" or "non-participating." The question doesn't specify, so let's analyze both:

**Non-participating preferred (more common):**
- Veronica chooses: EITHER get her 2X preference OR convert to common (whichever is higher)
- At $41M sale price:
  - 2X preference: $40M
  - Convert to common: 40% × $41M = $16.4M
  - **She chooses the preference: $40M**
- **Elaine gets:** $41M - $40M = **$1 million** (60% of remaining $1M)

**Participating preferred (less common, more aggressive for investors):**
- Veronica gets her 2X preference AND then also gets her share of the remainder as common
- At $41M sale price:
  - **Veronica gets:** $40M (2X preference) + 40% × $1M (remainder) = **$40.4 million**
  - **Elaine gets:** 60% × $1M = **$0.6 million**

Given the ambiguity, I'll assume **non-participating preferred** (the more standard VC term). In that case:

**Final answer (non-participating preferred):**
- **Veronica gets:** $40 million (her 2X liquidation preference)
- **Elaine and common get:** $1 million (the remainder)

**The horror scenario for founders:** If the sale price is below $40M (2X Veronica's investment), Elaine gets **nothing**. Veronica gets all the proceeds up to $40M.

This is why VCs often push for higher liquidation preferences (2X, 3X) in later rounds or for riskier deals - it gives them more downside protection, but it creates terrible misalignment with founders on exits.

### E. Even though Veronica has voting control, how might Elaine and her team still try to block a sale?

**Elaine and her team have several ways to block or influence a sale, despite Veronica's voting control:**

1. **Board rights:**
   - Even if Veronica controls shareholder votes, the board may approve mergers
   - If Elaine has board seats or board observer rights, she can block there
   - Many VC deals give founders some board representation

2. **Founder veto rights:**
   - Elaine may have contractual veto power over certain decisions (including sales below a threshold)
   - This protects founders from being forced into "fire sale" exits

3. **Key employee retention:**
   - **Threat:** Elaine and her team could quit if the company sells
   - **Leverage:** Acquirors buy startups for the team and technology
   - If the key employees leave, the acquisition becomes much less valuable
   - Elaine can threaten: "If you force this sale, we'll quit and join a competitor"
   - This gives her significant bargaining power

4. **Intellectual property:**
   - If Elaine or key team members hold key patents or IP personally (not through the company)
   - They can refuse to transfer IP to the acquiror
   - This makes the acquisition less attractive

5. **Poison pill or anti-takeover measures:**
   - Charter provisions that make hostile takeovers difficult
   - Requires supermajority vote for mergers (higher than Veronica's ownership %)
   - Rights plan that dilutes shares if someone tries to acquire without board approval

6. **Public pressure and reputation:**
   - Elaine can complain publicly about being forced into a bad deal
   - This could damage Veronica's reputation in the VC community
   - Future founders may refuse to work with Veronica if she's known for pushing fire sales

7. **Suing for breach of fiduciary duty:**
   - Elaine could sue Veronica or the board for approving a sale that unfairly benefits preferred at the expense of common
   - Claims: Breach of fiduciary duty, unfair dealing, oppression of minority shareholders
   - Even if she loses, the lawsuit can block the deal temporarily

8. **Refusing to cooperate with due diligence:**
   - Elaine and her team control the day-to-day operations
   - They can slow-walk or refuse to cooperate with acquiror's due diligence
   - This makes the deal harder to complete

9. **Finding a white knight:**
   - Elaine can shop the company to other buyers who will offer a better price
   - If another bidder offers >$50M, Veronica would actually prefer it (she converts to common and gets more)

**Most powerful weapon: The team threat.** Acquirors buy startups primarily for the talent. If Elaine says "the team will leave if this deal goes through at this price," that's usually enough to force a renegotiation or block the sale.

---

## Question 10: SPACs (Special Purpose Acquisition Companies)

### A. What is a SPAC?

**A SPAC (Special Purpose Acquisition Company) is a "blank-check" company created specifically to acquire or merge with another company.**

**How it works:**
1. **Formation:** Sponsors create a shell company with no operations
2. **IPO:** SPAC goes public and raises cash from investors (typically $10 per share)
3. **Trust account:** Money is held in a trust account while SPAC searches for a target
4. **Acquisition:** Within a time limit (usually 18-24 months), SPAC must find a private company to acquire
5. **De-SPAC:** The acquired company merges with the SPAC and becomes publicly traded
6. **Alternative:** If SPAC doesn't find a target in time, money is returned to investors and the SPAC dissolves

**Key features:**
- SPAC has **no business operations** when it IPOs - it's just cash and a promise to find a company
- Investors don't know what they're investing in (hence "blank check")
- Originally designed as a faster alternative to traditional IPO for private companies to go public

**SPAC boom:** 2020-2021 saw a massive wave of SPACs (hundreds of billions raised), followed by a crash as many performed poorly.

### B. SPACs have a "sponsor." What is their role? What expenses do they bear? What benefits do they get?

**The SPAC sponsor is the person or team that creates and manages the SPAC.** Typically, experienced investors, private equity firms, or celebrities.

**Sponsor's role:**
- Organize and form the SPAC
- Hire lawyers, accountants, underwriters
- Raise capital from investors
- Find and vet acquisition targets
- Negotiate the acquisition deal
- Manage the de-SPAC process

**Expenses the sponsor bears:**
- **Organization costs:** Legal fees, accounting, SEC filing costs (can be $2-5 million)
- **Underwriting fees:** Investment bank fees for the IPO (typically 2-5.5% of raised capital)
- **Due diligence costs:** Investigating potential targets
- **Marketing costs:** "Roadshows" to raise capital from investors
- **Ongoing expenses:** Operating the SPAC while searching for a target
- **Opportunity cost:** Time and effort spent managing the SPAC process

**Benefits the sponsor gets (this is where it gets lucrative):**

1. **"Promote" or "founder shares":**
   - Sponsor typically gets **20% of the SPAC's equity** for free or nominal cost
   - Example: SPAC raises $200M from public investors at $10/share; sponsor gets shares worth $50M for ~$25,000
   - This is the sponsor's compensation for bearing expenses and doing the work

2. **Warrants:**
   - Sponsor often gets warrants to buy additional shares at a low price
   - These become valuable if the SPAC's stock price rises

3. **Carried interest or share of upside:**
   - Some structures give sponsor a percentage of profits if the acquired company performs well

4. **Management fees:**
   - Some SPACs pay the sponsor ongoing management fees (less common)

5. **Reputational benefits:**
   - Being a SPAC sponsor can raise the sponsor's profile and deal flow

6. **Future deal opportunities:**
   - Relationships built during SPAC process can lead to other deals

**The controversy:**
- Sponsor gets 20% of the company for free (the "promote") regardless of performance
- If the acquired company performs poorly, public shareholders lose money while sponsor still made money
- Critics argue this creates misaligned incentives - sponsor may push through bad deals just to get their promote

### C. What is "dilution"? Who gets diluted in a SPAC?

**Dilution occurs when existing shareholders' ownership percentage decreases because new shares are issued.** In a SPAC, dilution happens because the sponsor and other parties get shares for free or at below-market prices.

**Sources of dilution in a SPAC:**

1. **Sponsor's promote (20% founder shares):**
   - Sponsor gets 20% of the company for free
   - Public shareholders who paid $10/share now own less of the company than they thought
   - Example: You invest $10,000 thinking you own 0.01% of the company, but due to sponsor's free shares, you only own 0.008%

2. **Warrants:**
   - SPACs typically include warrants (right to buy shares at $11.50)
   - When warrants are exercised, new shares are issued → dilution
   - Public shareholders' ownership percentage drops

3. ** PIPE (Private Investment in Public Equity):**
   - To complete an acquisition, SPAC often raises additional money from institutional investors via PIPE
   - PIPE investors get shares at a negotiated price → dilution for original IPO investors

4. **Fee shares:**
   - Underwriters, advisors, or the target company's shareholders may receive shares as compensation
   - These shares dilute public investors

**Who gets diluted?**
- **Public shareholders (IPO investors)** get diluted
- The sponsor gets shares upfront, so they're not diluted by later share issuances
- Target company shareholders may also get diluted if PIPE investors come in at a low valuation

**Why dilution matters:**
- If you paid $10/share thinking you owned 5% of a company, but due to dilution you only own 3%, you overpaid
- Dilution reduces the economic value of each share

**Example of SPAC dilution:**
- SPAC raises $200M from public investors at $10/share
- Sponsor gets 20% promote ($50M worth of shares) for free
- If the acquired company is worth $300M:
  - Public shareholders invested $200M but own only 80% of $300M = $240M (good!)
  - But if acquired company is worth $150M:
  - Public shareholders own 80% of $150M = $120M (they lost 40% of their investment)
  - Sponsor still made money: 20% of $150M = $30M (for almost zero investment)

### D. Who has a strong incentive to do an acquisition within the prescribed time period? Why?

**The SPAC sponsor has a very strong incentive to complete an acquisition within the time limit (usually 18-24 months).**

**Why the sponsor is incentivized to act:**

1. **All-or-nothing compensation:**
   - Sponsor only gets their 20% promote IF they complete an acquisition
   - If SPAC fails to find a target and dissolves, sponsor loses the $2-5M they spent on expenses
   - They get nothing for all their work

2. **Sunk costs:**
   - Sponsor has already spent millions on legal fees, underwriting, due diligence
   - If no deal happens, that money is gone with no return

3. **Reputational risk:**
   - Failed SPAC makes sponsor look incompetent
   - Harder to raise money for future SPACs if this one dissolves

4. **Time value of money:**
   - Sponsor has invested time and effort (opportunity cost)
   - They want to get their payday (the promote) sooner rather than later

5. **Competitive pressure:**
   - Other SPACs are competing for the same acquisition targets
   - If sponsor takes too long, good targets will be bought by other SPACs

**The problem:**
- This time pressure can lead to **bad deals**
- Sponsor may overpay for a mediocre target just to get a deal done before the deadline
- Sponsor may accept unfavorable terms or skip thorough due diligence
- **Moral hazard:** Sponsor's incentive (complete any deal) vs. public shareholders' incentive (complete only a good deal)

**This is why many SPACs have performed poorly** - sponsors rushed to complete acquisitions to get their promote, even when the targets weren't great companies or the price was too high.

### E. Are the incentives of managers and shareholders aligned in a SPAC?

**No - SPACs create significant misalignment between sponsors/managers and public shareholders.**

**Incentive conflicts:**

**1. Sponsor vs. Public Shareholders - Any Deal vs. Good Deal**

**Sponsor's incentive:**
- Complete **any** acquisition before the deadline (to get the 20% promote)
- The sponsor makes money even if the acquisition is overpriced or the target is a bad company
- Example: Sponsor spends $5M on expenses, gets 20% of a $200M SPAC = $40M for free
  - If they complete a mediocre deal, they get $40M
  - If they wait for a great deal but run out of time, they get $0 and lose $5M

**Public shareholders' incentive:**
- Complete **only a good acquisition** at a fair price
- They lose money if the SPAC overpays or buys a bad company
- They would rather the SPAC dissolve and return their money than do a bad deal

**Misalignment:** Sponsor is incentivized to do marginal or bad deals; shareholders would prefer no deal to a bad deal.

---

**2. Pricing Conflicts - Overpaying**

**Sponsor's incentive:**
- Accept a higher acquisition price to get the deal done
- Sponsor's 20% promote is worth more if the acquisition valuation is higher
- Example: If SPAC buys a company at $500M valuation vs. $300M valuation, sponsor's 20% is worth $100M instead of $60M

**Public shareholders' incentive:**
- Get a fair price for the acquisition
- Overpaying reduces future returns
- They want sponsor to negotiate hard and walk away if the price is too high

**Misalignment:** Sponsor benefits from higher valuations (bigger promote) even if the target isn't worth it.

---

**3. Due Diligence Thoroughness**

**Sponsor's incentive:**
- Complete due diligence quickly to beat the deadline
- Skip deep investigation to save time and get to a deal
- Overlook red flags to keep the deal moving

**Public shareholders' incentive:**
- Thorough due diligence to uncover problems
- Careful vetting to ensure they're investing in a quality company
- Walk away if significant problems are discovered

**Misalignment:** Time pressure on sponsor conflicts with shareholders' need for careful analysis.

---

**4. Warrant and Dilution Impact**

**Sponsor's incentive:**
- Include warrants (which dilute shareholders) because they make the IPO more attractive to investors and help raise more capital
- Warrants give sponsor more upside if stock price rises

**Public shareholders' incentive:**
- Minimize dilution to maximize their ownership percentage
- Fewer warrants and free shares means their investment is worth more

**Misalignment:** What's good for sponsor's capital raising and potential upside is bad for shareholders' ownership percentage.

---

**5. Long-term vs. Short-term**

**Sponsor's incentive:**
- Get the deal done, get the promote, move on to the next SPAC
- Short-term focus: complete the de-SPAC merger
- Less concerned with long-term performance of the acquired company

**Public shareholders' incentive:**
- Long-term stock price appreciation
- Want the acquired company to succeed over years
- Want management to build a sustainable business

**Misalignment:** Sponsor gets paid upfront; shareholders get paid only if the company performs well over time.

---

**6. Sponsor's Promote as Hidden Cost**

**The 20% promote is effectively a huge fee that public shareholders may not fully understand:**
- It's not disclosed as a "5% fee" - it's buried in the share structure
- Public shareholders may not realize they only own 80% of what they thought they were buying
- This creates a classic agency cost: sponsor gets value at shareholders' expense

---

**Are there any aligning incentives?**

**Some alignment exists:**
- If the acquired company performs very well, both sponsor and shareholders benefit (sponsor owns 20% of a bigger company)
- Sponsor's reputation matters: if they do bad deals, future SPACs will struggle
- Sponsor often buys additional shares or warrants in the IPO (skin in the game)

**But the misalignment is fundamental:**
- Sponsor gets paid regardless of quality (as long as a deal happens)
- Shareholders only get paid if quality is high
- This is the core moral hazard problem in SPACs

**Real-world result:**
- Many SPACs from the 2020-2021 boom saw their stocks crash after de-SPACing
- Studies show SPACs significantly underperform traditional IPOs
- Many sponsors got rich while public shareholders lost money
- This is exactly what the misaligned incentives predict

---

## Key Takeaways

### On Moral Hazard and Hidden Actions

- **Moral hazard is about hidden actions** - when you can't observe or verify what someone is doing after making a deal
- **Reputation and repeat dealings** can solve moral hazard even without contracts (shadow of the future)
- **Adverse selection vs. moral hazard:** Adverse selection is what you know (hidden information); moral hazard is what you do (hidden action)

### On Using Financial Incentives to Address Moral Hazard

**When financial incentives work well:**
- Performance is easily measurable and attributable to individual effort
- Risk can be efficiently allocated (less risk-averse party bears more risk)
- One-dimensional task (sales vs. complex multi-dimensional work)
- Short time horizon between effort and results

**When incentives create problems:**
- Multi-task environments (you get what you measure, neglecting what you don't measure)
- Performance is noisy (affected by luck, not just effort)
- Long time horizons (reward short-term at expense of long-term)
- Teamwork and collaboration needed (individual incentives undermine cooperation)
- Quality is hard to measure (gaming the system, Campbell's Law)

**Key tools for managing moral hazard:**
- **Incentive compensation** (commission, royalties, bonuses) - aligns interests but shifts risk
- **Monitoring and reporting** - reduces information asymmetry but is costly
- **Risk-sharing through deductibles, co-pays, coverage limits** (insurance model) - gives skin in the game
- **Debt and leverage** - but be careful, leverage can create moral hazard for equity holders!
- **Reputation and relationships** - powerful when there are repeat dealings
- **Contract structure** (staged financing, milestones, contingent payments, covenants)

### On Royalty vs. Fixed Payment Structures

- **Royalties align incentives** better than fixed payments when ongoing effort matters
- **Royalties create risk-sharing:** both parties benefit from success and share downside
- **Royalties can create conflicts** when one party has multiple options (Big Pharma may favor its own projects over royalty-bearing partnerships)
- **Monitoring and milestone-based payments** can address these conflicts

### On Leverage and Risk-Taking

- **Debt creates moral hazard for equity holders:** they get upside but limited downside
- **Equity holders may take negative NPV projects** if there's a chance of huge upside (option value)
- **Lenders use covenants, monitoring, and collateral** to reduce this moral hazard
- **Convertible debt** can align incentives (lender shares in upside if gamble pays off)

### On Insurance and Moral Hazard

- **Insurance creates moral hazard** because insured people take more risks
- **Solutions:** deductibles, co-pays, coverage limits, exclusions, experience rating
- **The key insight:** keep some risk with the insured person so they still have incentive to be careful

### On Compensation Design Challenges

- **Sales commission:** Motivates effort but shifts risk to salesperson; need to pay extra for risk-bearing
- **Law firm lock-step vs. eat-what-you-kill:**
  - Lock-step: better for teamwork, collaboration, long-term focus, mentoring
  - Eat-what-you-kill: better for individual accountability, business development, productivity
  - Most firms use hybrid systems to balance these trade-offs

### On Multi-Task Incentive Problems

- **You get what you pay for:** Incentivizing one measurable outcome causes neglect of unmeasurable but important outcomes
- **Sports examples illustrate the problem:** rewarding home runs → strikeouts increase; penalizing interceptions → timid quarterbacks; rewarding completions → dink-and-dunk offense
- **Solutions:** composite metrics (combine multiple measures), subjective evaluation (manager judgment), team-based rewards, strong organizational culture and norms

### On Venture Capital and Exit Incentives

- **Liquidation preferences protect VCs** but create misalignment with founders on exits
- **1X liquidation preference:** VC gets money back first; founders get nothing if sale price is below VC's investment
- **Conversion threshold:** VC converts to common when sale price exceeds post-money valuation (shares upside above that)
- **Founders can block bad exits** through board rights, veto rights, key employee threats (most powerful), IP control, lawsuits

### On SPACs and Incentive Misalignment

- **SPAC structure:** Shell company IPOs, raises cash, searches 18-24 months for acquisition target
- **Sponsor's 20% "promote":** Huge misalignment - sponsor gets paid for completing ANY deal, not just good deals
- **Dilution:** Public shareholders get diluted by sponsor's free shares, warrants, PIPE investors
- **Time pressure** forces sponsors to rush into deals, leading to poor post-SPAC performance
- **SPACs are a case study in moral hazard:** Sponsor's incentive (complete any deal) vs. shareholders' incentive (complete only good deals)

---

## Notes for Class Discussion

**Be ready to distinguish between:**
- Information problems (adverse selection) vs. incentive problems (moral hazard)
- Observable vs. verifiable performance (you can see it but can't prove it in court)
- Risk allocation vs. incentive alignment (these often trade off against each other)

**Connect to prior classes:**
- **VC and staged financing (Class 7):** Milestone-based payments address moral hazard
- **Earnouts (Class 21):** contingent purchase price aligns seller incentives post-acquisition
- **Representations and warranties (Class 4-5):** Legal accountability for hard-to-verify information

**Exam themes:**
- Identify who bears risk in each structure
- Explain how financial incentives change behavior
- Recognize when incentives create unintended consequences (multi-task problems, gaming, short-termism)
- Analyze leverage as both a tool and a source of moral hazard
- Evaluate incentive structures: Do they align interests? What are the trade-offs?

**Common cold call patterns:**
- "What is the moral hazard problem here?" (Identify hidden action and conflicting incentives)
- "How would you design a contract to address this?" (Apply tools: monitoring, incentives, risk-sharing, staging, covenants)
- "What's the trade-off?" (There's always a cost - risk shifting, measurement problems, multi-task distortion)

---

*Prepared by: Claude AI*
*Date: April 2026*
