# 🤖 LMNH Agent - The Builder

**The AI agent that builds LMNH by reading and following ALL documentation**

---

## 🎯 What This Is

This is the LMNH coding agent that will build the platform by:
1. Reading ALL docs in `/system/`
2. Understanding the vision, strategy, architecture
3. Following the patterns EXACTLY
4. Building what's defined in `AI-BUILDER-INSTRUCTIONS.md`

**This agent is CONFIGURED to read docs first, then build.**

---

## 🚀 Setup

### **1. Install Dependencies**

```bash
cd agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **2. Configure API Keys**

Edit `lmnh_config.json` and add your keys:

```json
{
  "slack_bot_token": "xoxb-YOUR-TOKEN",
  "slack_channel": "C1234567890",
  "claude_api_key": "sk-ant-api03-YOUR-KEY",
  "github_token": "ghp_YOUR-TOKEN"
}
```

**Get API keys:**
- **Slack:** https://api.slack.com/apps
- **Claude:** https://console.anthropic.com/
- **GitHub:** https://github.com/settings/tokens

### **3. Test Configuration**

```bash
python run_agent.py
```

Should see:
```
🚴‍♂️ LMNH-Builder starting...
📚 Required reading list loaded: 12 files
⚠️  Reminder: I will NOT code until I read ALL docs!
✅ Ready and listening...
```

---

## 📖 How It Works

### **Agent Behavior:**

1. **Listens in Slack** for `@LMNH-Builder` mentions
2. **When mentioned:**
   - First checks: "Have I read all required docs?"
   - If NO → Reads them first (from `required_reading` in config)
   - If YES → Proceeds with task
3. **Follows documented patterns** from `/system/architecture/`
4. **Commits code** following the strategy
5. **Reports back** in Slack thread

### **Configuration:**

The agent is pre-configured with:
- **Required reading:** All docs in `/system/`
- **Build rules:** From architecture docs
- **Tech stack:** Next.js, FastAPI, Supabase, Claude
- **Workspace:** This repo
- **Personality:** LMNH character (overconfident, helpful)

---

## 💬 How to Use

### **In Slack:**

**Start a task:**
```
@LMNH-Builder task: Set up the database schema for users and bots
```

**Agent response:**
```
🚴‍♂️ LOOK MUM! Starting task: Set up database schema
📚 First, let me read the architecture docs...
[Reads: TECH-STACK.md, DATABASE-SCHEMA.md, etc.]
✅ Understood! Using Supabase with RLS policies.
💻 Creating schema...
✅ DONE! Tables created with proper RLS policies.
```

**Give feedback:**
```
@LMNH-Builder move back to TODO: Missing user_preferences table
```

**Agent learns:**
```
😅 Hold up... Checking docs...
📚 Found it in LEARNING-SYSTEM.md - user_preferences table
💻 Adding now...
✅ Fixed! Added user_preferences with RLS.
```

---

## 🎓 What Agent Knows

**From reading docs, agent understands:**

### **Vision & Mission:**
- Why LMNH exists (accessibility)
- Who Stephen is and his drive
- The "Look Mum No Hands" philosophy
- Core beliefs (authenticity, accessibility)

### **Technical Architecture:**
- Tech stack: Next.js, FastAPI, Supabase, Solana
- Database: PostgreSQL + RLS + pgvector
- Learning system: Multi-dimensional, embeddings
- Deployment: Complete automation (Vercel, Supabase)
- Security: Encryption, custodial wallets

### **Build Strategy:**
- What to build (MVP features)
- How to build (patterns, workflow)
- What NOT to do (antipatterns)
- Success criteria

---

## 🔒 What Agent Will NOT Do

**Hard-coded rules:**
- ❌ Will NOT code without reading docs first
- ❌ Will NOT use different tech stack
- ❌ Will NOT expose technical details to users
- ❌ Will NOT skip security (RLS, encryption)
- ❌ Will NOT commit secrets
- ❌ Will NOT deviate from documented patterns

**If you ask it to violate rules:**
```
@LMNH-Builder task: Use MySQL instead of Supabase

Agent response:
😅 Hold up... The docs specify Supabase for a reason:
- RLS policies built-in
- Auth included
- pgvector for embeddings
- Already tested in MESSY

Can't use MySQL. Should I proceed with Supabase?
```

---

## 📊 Agent Logs

**Where to find logs:**
- Console output (real-time)
- `agent/logs/lmnh_builder.log` (file)
- Slack threads (conversational)

**What's logged:**
- Tasks received
- Docs read
- Actions taken
- Code changes
- Errors encountered
- Learning patterns

---

## 🎯 Example Tasks

### **Good tasks (specific, actionable):**

```
@LMNH-Builder task: Create the Supabase database schema with users, bots, tasks, and projects tables. Include RLS policies.

@LMNH-Builder task: Build the Next.js landing page with hero section, features, and CTA. Use Tailwind with neon green theme.

@LMNH-Builder task: Implement Supabase Auth with email/password and Google OAuth.

@LMNH-Builder task: Create the FastAPI backend with endpoints for user management, bot creation, and task processing.
```

### **Bad tasks (vague, against strategy):**

```
@LMNH-Builder task: Build the whole thing
→ Too vague, needs breakdown

@LMNH-Builder task: Use MongoDB instead
→ Violates documented tech stack

@LMNH-Builder task: Skip security for now
→ Violates design principles

@LMNH-Builder task: Just start coding
→ Needs to read docs first
```

---

## 🔧 Customizing Agent

### **To change required reading:**

Edit `lmnh_config.json`:
```json
"required_reading": [
  "your-doc.md",
  "another-doc.md"
]
```

### **To add build rules:**

Edit `lmnh_config.json`:
```json
"build_rules": [
  "Your custom rule here"
]
```

### **To change personality:**

Edit `catchphrases` in config or modify `agent_core/personality.py`

---

## 🚨 Troubleshooting

### **Agent won't start:**
- Check Python version (3.9+)
- Check all dependencies installed
- Check API keys in config
- Check Slack bot has permissions

### **Agent ignores tasks:**
- Check bot is in Slack channel
- Check @mention format correct
- Check bot has `app_mentions:read` permission

### **Agent makes mistakes:**
- Check if docs are complete
- Check if task was specific enough
- Give feedback: `@LMNH-Builder move back to TODO: [reason]`
- Agent will learn from feedback

### **Agent violates rules:**
- This shouldn't happen (rules are hard-coded)
- If it does, check config file wasn't modified
- Report as bug

---

## 📈 Progress Tracking

**Agent tracks:**
- Tasks completed
- Docs read
- Files created/modified
- Errors encountered
- Learning patterns discovered

**View progress:**
- Check Slack threads
- Check git commits
- Check `agent/logs/`

---

## 🎯 Success Criteria

**Agent has succeeded when:**
- [ ] All required docs read and understood
- [ ] MVP features built (from AI-BUILDER-INSTRUCTIONS.md)
- [ ] All code follows documented patterns
- [ ] Security implemented (RLS, encryption)
- [ ] Tests passing
- [ ] Deployments working
- [ ] Users can sign up and use platform

---

## 🚴‍♂️ The LMNH-Builder Promise

**This agent promises to:**
1. Read ALL docs before coding
2. Follow documented patterns EXACTLY
3. Build what's specified, not what it thinks
4. Prioritize security and UX
5. Learn from feedback
6. Never expose technical complexity
7. Make Stephen proud 💪

---

## 🎬 Ready to Build

**Start the agent:**
```bash
cd agent
source venv/bin/activate
python run_agent.py
```

**In Slack:**
```
@LMNH-Builder task: Let's start building! First, set up the Supabase project and create the base schema.
```

**And watch it build LMNH with NO HANDS!** 🚴‍♂️🚀

---

**Updated:** October 24, 2025  
**Status:** Ready to build  
**Agent:** LMNH-Builder v1.0

**"Look Mum No Hands - The agent that builds itself!"** 🤖

