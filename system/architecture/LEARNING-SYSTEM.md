# 🧠 LMNH LEARNING SYSTEM

**Multi-Dimensional Self-Improving Intelligence**

*The competitive moat - what makes LMNH different*

---

## 🎯 THE CORE CONCEPT

**LMNH learns from EVERYTHING:**
- Not just chat
- Not just code
- EVERY action, EVERY interaction, EVERY outcome

**Result:** Bot that gets smarter with every use

---

## 📊 WHAT WE LEARN FROM

### **1. CONVERSATIONS (Basic)**
```
User asks question
Bot answers
User rates response
Store: Question + Answer + Rating + Embedding
Next time: Pull high-rated past answers as context
```

### **2. ACTIONS (The differentiator)**
```
User: "Create a song"
Bot: Creates with Suno
User: 👍 loves it

Learn:
- Music preferences (genre, tempo, style)
- Time of day patterns
- Mood preferences
Store for next time
```

### **3. TASKS (Bot's own work)**
```
Bot: Creates landing page
Approach A: Used template → Failed
Approach B: Analyzed existing pages → Success!

Store: Approach B works for this project type
Next task: Use Approach B immediately
```

### **4. CODE/REPOS (Project knowledge)**
```
Bot connects to repo
Reads all files
Understands structure, patterns, dependencies
Stores as embeddings

User asks: "Where's auth logic?"
Bot KNOWS because it learned the codebase
```

### **5. API INTERACTIONS (Pattern recognition)**
```
Bot calls Slack API
Parameters X work
Parameters Y fail

Store: Use parameters X
Next call: Instant success, no trial/error
```

### **6. USER BEHAVIOR (Behavioral intelligence)**
```
Track patterns:
- Music choices → Life insights
- Code quality → Skill level
- Task types → Business insights
- Time patterns → Work habits

Use for: Recommendations, guidance, proactive help
```

### **7. FEEDBACK LOOPS (Improvement)**
```
User moves task back to TODO
User explains why it failed
Bot learns what went wrong
Bot adjusts approach
Next task: Better execution
```

---

## 🗄️ DATABASE SCHEMA

### **Core Learning Tables:**

```sql
-- ALL actions (not just chat)
bot_actions (
  id,
  user_id,
  task_id,
  action_type,          -- "music_created", "code_written", "task_moved"
  action_data,          -- JSON with details
  approach_used,        -- Which method
  success BOOLEAN,
  user_rating,          -- 1-5 stars
  time_taken,
  errors,
  resolution,
  embedding VECTOR(3072), -- OpenAI embedding for semantic search
  created_at
);

-- Bot's learnings
bot_learnings (
  id,
  pattern_type,         -- "coding_style", "music_preference", "workflow"
  pattern_data,         -- JSON
  confidence FLOAT,     -- 0-1 how sure
  times_used INT,
  success_rate FLOAT,
  learned_from_action,  -- Link to bot_actions
  created_at,
  last_used
);

-- Project knowledge (from repos)
project_knowledge (
  id,
  project_id,
  knowledge_type,       -- "file_structure", "dependencies", "patterns"
  content,
  summary,
  embedding VECTOR(3072),
  learned_from,
  last_validated,
  confidence
);

-- User preferences (discovered over time)
user_preferences (
  id,
  user_id,
  preference_type,      -- "music_genre", "code_style", "deployment"
  preference_value,     -- JSON
  confidence FLOAT,
  learned_from,         -- Which action taught us this
  times_observed,
  last_seen
);

-- API patterns (what works)
api_patterns (
  id,
  api_name,             -- "Suno", "Slack", "GitHub"
  action_type,          -- "create_song", "post_message"
  pattern_json,         -- What worked
  success_rate,
  times_used,
  last_used
);

-- Cross-integration learnings
integration_patterns (
  id,
  integration_combo,    -- "Slack + GitHub", "Suno + Storage"
  pattern,              -- "User always posts PR to #dev"
  frequency,
  confidence
);
```

---

## 🔄 THE LEARNING FLOW

### **Every Action Triggers Learning:**

```python
async def execute_action(user_id, action_type, action_data):
    # 1. Do the action
    result = await perform_action(action_type, action_data)
    
    # 2. Store action + result
    action_record = await db.bot_actions.insert({
        'user_id': user_id,
        'action_type': action_type,
        'action_data': action_data,
        'result': result,
        'success': result.success,
        'time_taken': result.time,
        'errors': result.errors
    })
    
    # 3. Generate embedding for semantic search
    embedding = await openai.embed(
        f"{action_type}: {json.dumps(action_data)}"
    )
    await db.bot_actions.update_embedding(action_record.id, embedding)
    
    # 4. Learn patterns from this action
    await learn_from_action(user_id, action_type, result)
    
    # 5. Update user preferences
    await update_preferences(user_id, action_type, result)
    
    # 6. Update confidence scores
    await update_confidence_scores(user_id, action_type, result.success)
    
    return result

async def learn_from_action(user_id, action_type, result):
    """Extract learnings from action"""
    
    if action_type == "music_created":
        # Learn music preferences
        await update_preference(user_id, "music_genre", result.genre)
        await update_preference(user_id, "music_tempo", result.tempo)
        await update_preference(user_id, "music_style", result.style)
        
    elif action_type == "code_written":
        # Learn coding patterns
        patterns = analyze_code_style(result.code)
        for pattern in patterns:
            await store_learning(user_id, "coding_style", pattern)
            
    elif action_type == "task_moved":
        # Learn workflow patterns
        await store_workflow_pattern(
            user_id, 
            result.from_status, 
            result.to_status
        )
        
    # ... for every action type
```

---

## 🧪 TECH STACK FOR LEARNING

### **Embeddings: OpenAI text-embedding-3-large**
- 3072 dimensions (best quality)
- $0.00013 per 1K tokens (cheap)
- Industry standard

### **Vector Storage: Supabase pgvector**
- Already have it
- SQL queries for complex filters
- Built-in RLS for security
- Cosine similarity search

### **AI: Claude Sonnet 4**
- For chat/coding tasks
- For analyzing patterns
- For generating summaries

### **NO Langchain**
- Too heavy, too opaque
- Build custom learning system
- Full control, lighter weight

---

## 🎯 LEARNING TYPES

### **1. Pattern Recognition**
```
After 10 music creations:
Bot learns: User prefers 140+ BPM, hip-hop style
Next request: "Make me a song" → Bot suggests hip-hop at 140 BPM
```

### **2. Error Recovery**
```
Bot hits error: "Module not found"
Bot tries: npm install → Works!
Store: For this error, run npm install
Next time: Auto-fixes before user notices
```

### **3. Optimization**
```
Task took 10 minutes
8 minutes was waiting for build
Learn: Run build in background
Next task: Parallel processing, 2 minutes total
```

### **4. Preference Discovery**
```
User always adds dark mode
User always uses TypeScript
User always deploys to Vercel
Bot learns these patterns
Next project: Suggests these automatically
```

### **5. Proactive Assistance**
```
Bot learns: User deploys Fridays at 3pm
Friday 2:45pm: "Want me to prep deployment?"
= Anticipates needs
```

---

## 📈 CONFIDENCE SCORING

**Every learning has confidence (0-1):**

```python
def calculate_confidence(pattern):
    factors = {
        'times_observed': pattern.times_used,
        'success_rate': pattern.success_rate,
        'recency': days_since_last_use(pattern),
        'consistency': pattern.variance,
    }
    
    confidence = (
        (factors['times_observed'] / 10) * 0.3 +  # More uses = higher
        factors['success_rate'] * 0.4 +            # Higher success = higher
        (1 - factors['recency'] / 30) * 0.2 +      # More recent = higher
        (1 - factors['consistency']) * 0.1         # More consistent = higher
    )
    
    return min(confidence, 1.0)
```

**Use confidence to:**
- Decide when to suggest vs ask
- Filter low-confidence patterns
- Prioritize high-confidence learnings
- Fade unsuccessful patterns

---

## 🔄 FEEDBACK LOOPS

### **User Feedback:**
```
User rates action: 👍 👎
Update: Confidence score, success rate
High ratings: Boost this pattern
Low ratings: Demote this pattern
```

### **Implicit Feedback:**
```
User accepts suggestion: +confidence
User rejects suggestion: -confidence
User modifies result: Learn from modification
User moves task back: Learn what failed
```

### **Outcome Feedback:**
```
Task completed successfully: +confidence in approach
Task failed: -confidence, try different approach
Task took longer: Deprioritize this approach
Task was fast: Prioritize this approach
```

---

## 🚀 CROSS-USER LEARNING (Optional)

**Aggregate anonymous learnings:**

```sql
platform_learnings (
  pattern_type,
  pattern_data,
  times_seen,           -- Across all users
  success_rate,         -- Aggregate
  confidence
);
```

**Example:**
- 100 users build Next.js apps
- 90 use Tailwind CSS
- Store: "Next.js projects typically use Tailwind"
- New user builds Next.js → Suggest Tailwind

**Privacy:**
- Aggregate only
- No personal data
- Opt-out available
- Anonymous patterns

---

## 📊 LEARNING METRICS

**Track effectiveness:**

```sql
learning_metrics (
  date,
  total_learnings,
  confidence_avg,
  success_rate,
  learnings_applied,
  learnings_successful,
  learnings_failed,
  learnings_faded        -- Low confidence removed
);
```

**Success indicators:**
- Increasing first-time success rate
- Decreasing task time
- Higher user satisfaction
- More proactive suggestions accepted
- Fewer corrections needed

---

## 🎯 THE EVOLUTION

**Week 1 (Basic):**
- Learns from explicit feedback
- Stores successful patterns
- 60% first-time success

**Month 1 (Improving):**
- Learns from actions
- Recognizes patterns
- 75% first-time success

**Month 3 (Smart):**
- Anticipates needs
- Proactive suggestions
- 85% first-time success

**Month 6 (Expert):**
- Knows user deeply
- Cross-project intelligence
- 95% first-time success

**Year 1 (Master):**
- Telepathic-level collaboration
- Minimal user input needed
- 99% first-time success

---

## ⚠️ IMPORTANT NOTES

### **Privacy:**
- User controls their data
- Can delete learnings
- Can disable learning
- Transparent about what's learned

### **Security:**
- Never log sensitive data
- Encrypt stored patterns
- RLS on all learning tables
- Audit trail

### **Performance:**
- Async learning (don't block actions)
- Cache frequently-used patterns
- Prune low-confidence learnings
- Optimize vector searches

---

## 🔮 FUTURE ENHANCEMENTS

**Planned:**
- Multi-modal learning (images, voice)
- Collaborative filtering
- Transfer learning between users
- Explainable AI (why bot suggested X)
- Learning visualization for users
- A/B testing of approaches

---

**Status:** Architecture defined, ready for implementation  
**Updated:** October 24, 2025  
**Next:** Build the learning pipeline

---

*"The platform that learns from everything you do becomes irreplaceable."* 🧠

