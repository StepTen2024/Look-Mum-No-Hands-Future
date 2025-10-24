# 🚀 Quick Setup: LMNH-Builder Agent

**Get the agent running in 5 minutes**

---

## ✅ CONFIRMED WORKING

**The agent is tested and working!**
- ✅ Connects to Slack as "lmnh2"
- ✅ Listens in #agent-tasks channel  
- ✅ Ready to receive @LMNH-Builder mentions

---

## 📋 Setup Steps

### 1. Configure API Keys

```bash
cd agent
cp lmnh_config.example.json lmnh_config.json
nano lmnh_config.json
```

**Add your keys** (they're already in MESSY/coding-agents/configs/lmnh.json):
- `slack_bot_token`
- `claude_api_key`  
- `github_token`
- `openai_api_key`
- `supabase_url` and `supabase_key`

### 2. Test Connection

```bash
cd agent
python3 test_connection.py
```

**Expected output:**
```
🧪 Testing LMNH-Builder Connection...

1️⃣ Testing Slack connection...
   ✅ Connected as: lmnh2
   ✅ Bot User ID: U09MQMTSRD5

2️⃣ Testing channel access...
   ✅ Found channel: #agent-tasks
   ✅ Bot is a member of this channel

3️⃣ Sending test message...
   ✅ Test message sent!

============================================================
✅ ALL TESTS PASSED!
```

### 3. Start the Agent

```bash
cd ..
./start_builder.sh
```

**Agent will:**
- Set up Python venv (first time)
- Install dependencies
- Start listening in Slack

---

## 💬 Using the Agent

### In Slack (#agent-tasks):

**Give it a task:**
```
@LMNH-Builder task: Read all the documentation and understand the architecture
```

**Agent responds:**
```
🚴‍♂️ LOOK MUM! Starting task: Read docs
📚 Consuming documentation... Understanding the vision...
[Reads 12 docs from /system/]
✅ Got it! I understand:
   - Vision: Accessibility for everyone
   - Tech: Next.js + FastAPI + Supabase + Solana
   - Strategy: Complete deployment, multi-dimensional learning
Ready to build! What should I start with?
```

**Start building:**
```
@LMNH-Builder task: Set up the Supabase database schema with users, bots, tasks, and projects tables. Include RLS policies.
```

---

## 🎯 What Agent Will Do

**Before coding:**
1. ✅ Read AI-BUILDER-INSTRUCTIONS.md
2. ✅ Read all 12 required docs in /system/
3. ✅ Confirm understanding

**While coding:**
1. ✅ Follow documented patterns
2. ✅ Use documented tech stack
3. ✅ Implement security (RLS, encryption)
4. ✅ Test before committing
5. ✅ Report progress in Slack

**After coding:**
1. ✅ Commit with clear messages
2. ✅ Push to GitHub
3. ✅ Report completion
4. ✅ Ready for next task

---

## 🔒 What Agent WON'T Do

**Hard-coded rules:**
- ❌ Won't code without reading docs
- ❌ Won't use different tech stack
- ❌ Won't expose technical details to users
- ❌ Won't skip security
- ❌ Won't commit API keys
- ❌ Won't delete working code

---

## 🐛 Troubleshooting

### "Bot not responding"
```bash
# Check if agent is running
ps aux | grep run_agent

# Restart agent
./start_builder.sh
```

### "Bot not in channel"
```
# In Slack
/invite @LMNH-Builder
```

### "Connection failed"
```bash
# Verify API keys
cd agent
python3 test_connection.py
```

---

## 📊 Current Status

**As of:** October 24, 2025  
**Bot:** lmnh2 (U09MQMTSRD5)  
**Channel:** #agent-tasks (C09N45F0VN2)  
**Status:** ✅ LIVE and listening  
**Test message:** ✅ Sent successfully  

---

## 🎯 Next Steps

1. ✅ Agent is configured
2. ✅ Agent is tested
3. ✅ Agent is listening
4. 🎯 Tag it in Slack: `@LMNH-Builder task: Read all docs`
5. 🚀 Watch it build LMNH!

---

**Look Mum No Hands - Now it builds itself!** 🚴‍♂️🤖

