# 🏗️ LMNH ARCHITECTURE

**Technical Strategy & System Design Documentation**

*DO NOT FUCK THIS UP - READ EVERYTHING BEFORE CODING*

---

## 📋 WHAT'S IN HERE?

This folder contains ALL the technical strategy and architecture decisions for LMNH.

**Before writing ANY code:**
1. Read ALL docs in this folder
2. Understand the strategy
3. Follow the patterns
4. Don't improvise
5. Don't delete working shit

---

## 📚 DOCUMENTATION INDEX

### **Core Architecture:**
- `TECH-STACK.md` - Complete tech stack analysis from MESSY + decisions
- `LEARNING-SYSTEM.md` - Multi-dimensional learning (actions, not just chat)
- `ADAPTIVE-INTELLIGENCE.md` - Bot adapts to user skill level
- `COMPLETE-DEPLOYMENT-SYSTEM.md` - Full infrastructure automation
- `UX-ABSTRACTION-STRATEGY.md` - How we hide complexity from users
- `API-MANAGEMENT.md` - How we handle platform APIs vs user tokens (coming)
- `DATABASE-SCHEMA.md` - Supabase tables, RLS policies (coming)
- `SECURITY-STRATEGY.md` - Encryption, token storage, best practices (coming)

### **Integration Patterns:**
- `SLACK-INTEGRATION.md` - How bots connect to Slack (coming)
- `GITHUB-INTEGRATION.md` - How bots connect to GitHub (coming)
- `SOLANA-INTEGRATION.md` - How $LMNH token works (coming)
- `SUNO-INTEGRATION.md` - How music generation works (coming)

### **System Design:**
- `AGENT-ORCHESTRATION.md` - How AI agents work (coming)
- `TASK-QUEUE-SYSTEM.md` - How tasks are processed (coming)
- `WEBHOOK-HANDLERS.md` - How external events trigger actions (coming)

---

## 🎯 DESIGN PRINCIPLES

### **1. ABSTRACTION IS EVERYTHING**
Users should NEVER see:
- API keys
- Blockchain addresses
- Technical jargon
- Complex workflows
- Error codes (translate to human)

### **2. WE MANAGE, THEY USE**
Platform owns:
- API usage (Suno, Claude, etc.) - we pay
- Crypto wallets (custodial) - we hold keys
- Infrastructure complexity

Users provide:
- Service tokens (Slack, GitHub) - we encrypt
- Creative input - we execute
- Zero technical knowledge required

### **3. SECURITY BY DEFAULT**
- Encrypt ALL sensitive data
- RLS on ALL database tables
- Audit trail for ALL actions
- Rate limiting on ALL endpoints
- Fail secure, not open

### **4. SCALE FROM DAY ONE**
- Async task processing
- Horizontal scaling ready
- Stateless architecture
- Queue-based workflows
- No single points of failure

### **5. PROGRESSIVE DISCLOSURE**
- Start simple (MVP features)
- Add complexity only when needed
- Advanced features hidden by default
- Power users can unlock more
- Never confuse beginners

---

## 🚫 WHAT NOT TO DO

**DON'T:**
- ❌ Over-engineer the MVP
- ❌ Expose technical details to users
- ❌ Store unencrypted secrets
- ❌ Skip RLS policies
- ❌ Hardcode API keys
- ❌ Delete working code without backup
- ❌ Push breaking changes to main
- ❌ Skip error handling
- ❌ Ignore rate limits
- ❌ Build without reading these docs

**DO:**
- ✅ Follow the documented patterns
- ✅ Test everything locally first
- ✅ Encrypt sensitive data
- ✅ Add audit logs
- ✅ Handle errors gracefully
- ✅ Rate limit API calls
- ✅ Version your changes
- ✅ Document as you build
- ✅ Ask before major changes
- ✅ Read ALL these docs first

---

## 🔄 WORKFLOW

### **Before Coding:**
1. Read relevant architecture docs
2. Understand the pattern
3. Check existing implementations (in MESSY if needed)
4. Plan your approach
5. Get approval if unsure

### **While Coding:**
1. Follow established patterns
2. Add comments for complex logic
3. Test as you go
4. Don't break working features
5. Commit small, logical changes

### **After Coding:**
1. Test end-to-end
2. Check security (encryption, RLS)
3. Verify error handling
4. Update docs if architecture changed
5. Get review before merging

---

## 📖 REFERENCE MATERIALS

### **Related Folders:**
- `/LMNH/assets/brand/` - Brand strategy, tokenomics, UX philosophy
- `/LMNH/assets/founder/` - Founder vision, understand the WHY
- `/LMNH/assets/personality/` - LMNH agent personality
- `/MESSY/coding-agents/` - Previous proof-of-concept (reference only)

### **Key Decisions:**
- **Frontend:** Next.js + Tailwind CSS
- **Backend:** Python (FastAPI likely) or Next.js API routes
- **Database:** Supabase (PostgreSQL + RLS)
- **AI:** Claude API (Sonnet 4)
- **Blockchain:** Solana (for $LMNH token)
- **Hosting:** TBD (Vercel for frontend likely)

---

## 🎓 LEARNING RESOURCES

**If you're new to any tech:**
- Supabase: https://supabase.com/docs
- Solana Web3.js: https://solana-labs.github.io/solana-web3.js/
- Next.js: https://nextjs.org/docs
- Prisma/Supabase: https://www.prisma.io/docs

**Don't guess. Read. Then build.**

---

## 🚨 EMERGENCY CONTACTS

**If you fuck something up:**
1. Don't panic
2. Don't try to fix by guessing
3. Stop and assess damage
4. Check git history (what changed?)
5. Revert if needed
6. Ask for help

**Git safety:**
```bash
# Before making big changes
git checkout -b feature-name
git commit -m "clear message"

# If you fuck up
git log --oneline
git checkout main
git reset --hard <last-good-commit>
```

---

## 📊 STATUS TRACKING

**Architecture Docs Status:**
- ✅ Tech Stack Analysis
- ✅ Learning System (multi-dimensional)
- ✅ Adaptive Intelligence
- ✅ Complete Deployment System
- ✅ UX Abstraction Strategy
- ⏳ API Management (next)
- ⏳ Database Schema (next)
- ⏳ Security Strategy (planned)
- ⏳ Behavioral Intelligence (planned)
- ⏳ Integration Patterns (planned)

**Updated:** October 24, 2025

---

## 🎯 THE MISSION

**Build a platform where ANYONE can create AI coding agents...**
- Without knowing how to code
- Without understanding APIs
- Without crypto knowledge
- Without technical skills

**"Look Mum No Hands" - Make it THAT easy.**

---

**NOW GO READ THE DOCS AND BUILD IT RIGHT!** 🚴‍♂️💪

*P.S. - If you delete working code without checking these docs first, you're fired. JK. But seriously, read this shit.* 😂

