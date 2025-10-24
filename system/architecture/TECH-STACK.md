# ⚙️ LMNH TECH STACK

**Complete technology stack from MESSY proof-of-concept + decisions for clean build**

*Analyzed from: `/MESSY/coding-agents/`*

---

## 📊 WHAT WORKED IN MESSY

**These are PROVEN technologies that worked well:**

---

## 🎨 FRONTEND

### **Framework: Next.js 14**
```json
"next": "^14.0.0"
"react": "^18.2.0"
"react-dom": "^18.2.0"
```

**Why it worked:**
- ✅ Server-side rendering
- ✅ API routes built-in
- ✅ TypeScript support
- ✅ Fast refresh (great DX)
- ✅ Easy deployment (Vercel)

**Verdict:** **KEEP IT** ✅

---

### **Styling: Tailwind CSS 3.3**
```json
"tailwindcss": "^3.3.5"
"autoprefixer": "^10.4.16"
"postcss": "^8.4.31"
```

**Custom theme in MESSY:**
```javascript
colors: {
  lmnh: {
    green: '#00ff88',
    dark: '#1a1a1a',
    gray: '#333',
  }
}
```

**Custom animations:**
- `pulse-slow` - For status indicators
- `glow` - For neon green effects
- `fadeIn`, `scaleIn`, `slideUp` - For smooth transitions
- `flipbook` - For card flips

**Verdict:** **KEEP IT** ✅  
**Action:** Port custom theme to `/system/brand/` for consistency

---

### **Icons: Lucide React**
```json
"lucide-react": "^0.292.0"
```

**Why it worked:**
- ✅ Modern, clean icons
- ✅ Tree-shakeable
- ✅ TypeScript support
- ✅ Consistent style

**Verdict:** **KEEP IT** ✅

---

## 🗄️ DATABASE

### **Primary: Supabase (PostgreSQL)**
```
Transaction Pooler: port 6543 (for queries)
Session Pooler: port 5432 (for migrations)
```

**Why it worked:**
- ✅ PostgreSQL (rock solid)
- ✅ Built-in auth
- ✅ Row Level Security (RLS)
- ✅ Real-time subscriptions
- ✅ RESTful API
- ✅ Vector embeddings support (pgvector)

**Verdict:** **KEEP IT** ✅  
**Critical:** Must use RLS + encryption (per our UX abstraction strategy)

---

### **ORM: Prisma 6.18**
```json
"@prisma/client": "^6.18.0"
"prisma": "^6.18.0"
```

**Schema highlights from MESSY:**
- Multi-user system (Users, Bots, Projects, Tasks)
- Vector embeddings for semantic search
- Task events tracking
- Conversation history
- System logs
- Comprehensive enums (TaskStatus, Priority, etc.)

**Verdict:** **KEEP IT** ✅  
**Action:** Adapt MESSY schema for new clean structure

---

### **Vector Support:**
```sql
embedding Unsupported("vector(1536)")
```

**For:**
- Semantic search in conversations
- Commit history search
- Long-term memory
- Context retrieval

**Verdict:** **KEEP IT** ✅  
**Note:** Supabase supports pgvector natively

---

## 🐍 BACKEND (Python Agent)

### **Core: Python 3.9+**
```python
# requirements.txt
anthropic>=0.25.0
slack-sdk>=3.23.0
gitpython>=3.1.40
requests>=2.31.0
```

**Why it worked:**
- ✅ Mature AI libraries
- ✅ Easy Slack integration
- ✅ Git operations native
- ✅ Fast prototyping

**Verdict:** **KEEP IT** (for agent orchestration) ✅

---

### **API Server: FastAPI**
```python
fastapi>=0.104.0
uvicorn>=0.24.0
```

**What it did in MESSY:**
- Real-time status updates
- Task queue management
- Log streaming
- Stats aggregation
- CORS middleware

**Features:**
- ✅ Fast (as the name suggests)
- ✅ Auto-generated docs (OpenAPI)
- ✅ Type hints (great DX)
- ✅ WebSocket support
- ✅ Easy async/await

**Verdict:** **KEEP IT** ✅

---

### **AI: Anthropic Claude API**
```python
anthropic>=0.25.0
```

**Config from MESSY:**
```json
"claude_api_key": "sk-ant-api03-..."
```

**Why Claude:**
- ✅ Best for coding tasks
- ✅ Large context window
- ✅ Function calling
- ✅ Artifacts support
- ✅ Streaming responses

**Verdict:** **KEEP IT** (Claude Sonnet 4 confirmed) ✅

---

### **Integrations in MESSY:**

**Slack SDK:**
```python
slack-sdk>=3.23.0
```
- Bot token auth
- Channel posting
- Thread management
- Event handling

**Verdict:** **KEEP IT** ✅

**GitHub:**
```python
gitpython>=3.1.40
```
- Clone repos
- Commit changes
- Push to remote
- Branch management

**Config:**
```json
"github_token": "ghp_...",
"github_username": "..."
```

**Verdict:** **KEEP IT** ✅

---

## 🏗️ ARCHITECTURE PATTERNS (from MESSY)

### **1. Config Management**
```python
# agent_core/config.py
class AgentConfig:
    def __init__(self, config_file):
        self.config = self.load_config()
```

**Config file:**
```json
configs/lmnh.json
```

**Stored:**
- Agent name, emoji
- API keys (Slack, Claude, GitHub)
- Workspace path
- Personality settings
- Catchphrases

**Verdict:** **ADAPT IT**  
**Change:** Use `.env` instead of JSON for secrets

---

### **2. State Management**
```python
# Global state dict
agent_state = {
    "status": "offline",
    "current_task": None,
    "progress": 0,
    "tasks": [],
    "logs": [],
    "stats": {}
}
```

**Functions:**
- `update_agent_state()`
- `add_task()`
- `update_task_status()`
- `add_log()`

**Verdict:** **IMPROVE IT**  
**Change:** Use Redis or database for multi-user scalability

---

### **3. Real-time Updates**
```python
# FastAPI endpoints
@app.get("/status")
@app.get("/tasks")
@app.get("/logs")
@app.get("/stats")
```

**Frontend polling:**
```javascript
// Fetch every 2 seconds
setInterval(() => fetch('/api/status'), 2000)
```

**Verdict:** **UPGRADE IT**  
**Change:** Use WebSockets or Server-Sent Events (SSE) for true real-time

---

### **4. Personality System**
```python
# agent_core/personality.py
personality = {
    "catchphrases": {
        "starting": "LOOK MUM! Starting task...",
        "thinking": "🤔 Thinking with NO HANDS...",
        # etc
    }
}
```

**Verdict:** **KEEP IT** ✅  
**Already documented:** `/system/personality/LMNH_PERSONNEL_FILE.md`

---

### **5. Task Event Tracking**
```sql
model TaskEvent {
  eventType: TaskEventType
  -- created, assigned, started, progress_update,
  -- thinking, cloning_repo, reading_file,
  -- writing_code, running_tests, etc.
}
```

**Verdict:** **KEEP IT** ✅  
**Great for:** User transparency, debugging, audit trails

---

## 🔒 SECURITY (from MESSY)

### **What was done:**
❌ API keys in JSON file (unencrypted)  
❌ Database credentials in `.env` (but visible in file)  
⚠️ CORS set to allow all origins  

### **What we need:**
✅ Encrypted token storage (per UX abstraction strategy)  
✅ RLS policies on all tables  
✅ Environment variables for secrets  
✅ Restricted CORS (specific origins only)  
✅ Rate limiting  
✅ User authentication (Supabase Auth)  

**Verdict:** **MAJOR UPGRADE NEEDED** 🔐

---

## 🎯 TECH STACK DECISIONS FOR CLEAN BUILD

### **KEEP (Proven):**

**Frontend:**
- ✅ Next.js 14
- ✅ React 18
- ✅ TypeScript
- ✅ Tailwind CSS (with custom LMNH theme)
- ✅ Lucide React icons

**Backend:**
- ✅ Python 3.9+
- ✅ FastAPI + Uvicorn
- ✅ Anthropic Claude API (Sonnet 4)
- ✅ Slack SDK
- ✅ GitPython

**Database:**
- ✅ Supabase (PostgreSQL)
- ✅ Prisma ORM
- ✅ pgvector (embeddings)

**Integrations:**
- ✅ Slack
- ✅ GitHub
- ✅ Suno (music) - new
- ✅ Solana (crypto) - new

---

### **ADD (New features):**

**Blockchain:**
- ✅ Solana Web3.js
- ✅ @solana/spl-token
- ✅ Phantom wallet integration

**Security:**
- ✅ Crypto library (AES-256-GCM)
- ✅ JWT for sessions
- ✅ Rate limiting (express-rate-limit or similar)

**Real-time:**
- ✅ WebSockets or Server-Sent Events
- ✅ Redis (for state management across instances)

**Music:**
- ✅ Suno API integration

**Voice (future):**
- ✅ OpenAI Whisper API

---

### **CHANGE (Improvements):**

**Config Management:**
- ❌ JSON files for secrets
- ✅ Environment variables (`.env`)

**State Management:**
- ❌ In-memory Python dict
- ✅ Redis + Database

**Authentication:**
- ❌ No auth in MESSY
- ✅ Supabase Auth (email/password, social logins)

**API Keys:**
- ❌ Plaintext storage
- ✅ Encrypted with master key

**CORS:**
- ❌ Allow all origins
- ✅ Whitelist specific domains

---

## 📦 COMPLETE PACKAGE LIST

### **Frontend (`package.json`):**
```json
{
  "dependencies": {
    "@prisma/client": "^6.18.0",
    "@solana/web3.js": "^1.87.0",
    "@solana/spl-token": "^0.3.9",
    "lucide-react": "^0.292.0",
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.31",
    "prisma": "^6.18.0",
    "tailwindcss": "^3.3.5",
    "typescript": "^5.2.2"
  }
}
```

### **Backend (`requirements.txt`):**
```python
# AI & APIs
anthropic>=0.25.0
openai>=1.0.0

# Integrations
slack-sdk>=3.23.0
gitpython>=3.1.40
requests>=2.31.0

# Web framework
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.0.0

# Database
psycopg2-binary>=2.9.9
asyncpg>=0.29.0

# Security
cryptography>=41.0.0
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4

# Utilities
python-dotenv>=1.0.0
redis>=5.0.0
websockets>=12.0
```

---

## 🗂️ PROJECT STRUCTURE

### **From MESSY (what worked):**
```
coding-agents/
  agent_core/           # Python agent logic
    - agent.py
    - claude_handler.py
    - slack_handler.py
    - github_handler.py
    - personality.py
    - api_server.py
    - config.py
  
  dashboard/            # Next.js frontend
    app/                # App router
    components/         # React components
    lib/                # Utilities
    prisma/             # Database schema
    public/             # Static assets
  
  configs/              # Config files
    - lmnh.json
  
  workspace/            # Git repos (agent workspace)
```

### **For Clean Build:**
```
LMNH/
  system/               # Strategy & docs (NEW)
    - architecture/
    - brand/
    - founder/
    - personality/
  
  assets/               # Files only
    - logos/
    - music/
  
  backend-user/         # FastAPI (user-facing)
    - api/
    - services/
    - models/
    - integrations/
  
  backend-admin/        # FastAPI (internal)
    - api/
    - services/
  
  frontend-public/      # Next.js (landing page)
  
  frontend-user/        # Next.js (user portal)
  
  admin-dashboard/      # Next.js (internal)
  
  shared/               # Shared types, utils
    - prisma/           # Single schema for all
```

---

## 🚀 DEPLOYMENT (from MESSY)

**What was used:**
- Local development only
- Port 4002 for dashboard
- Python script to start agent

**For production:**
- **Frontend:** Vercel (Next.js optimized)
- **Backend:** Railway, Fly.io, or DigitalOcean
- **Database:** Supabase (already cloud)
- **Redis:** Upstash (serverless) or Railway
- **Monitoring:** Sentry, LogRocket

---

## 📊 WHAT WE LEARNED FROM MESSY

### **✅ What Worked:**
1. Next.js + Tailwind = fast UI development
2. Prisma = great DX for database
3. FastAPI = perfect for Python backend
4. Claude API = excellent for coding tasks
5. Slack integration = smooth communication
6. Task event tracking = great transparency
7. Real-time dashboard = engaging UX

### **❌ What Didn't Work:**
1. No authentication = insecure
2. Plaintext secrets = vulnerable
3. In-memory state = not scalable
4. No rate limiting = abuse risk
5. Polling for updates = inefficient
6. Single-user architecture = not platform-ready

### **🔄 What We'll Improve:**
1. Add proper auth (Supabase)
2. Encrypt all secrets
3. Use Redis for state
4. Add rate limiting
5. Use WebSockets
6. Multi-tenant from day 1
7. Add crypto layer (Solana)
8. Custodial wallets
9. User-friendly abstraction

---

## 🎯 THE TECH STACK VERDICT

**PROVEN FOUNDATION + NEW FEATURES = LMNH PLATFORM**

**Keep the good stuff:**
- Next.js, Tailwind, Prisma, FastAPI, Claude

**Add the missing pieces:**
- Auth, encryption, WebSockets, Redis, Solana

**Fix the problems:**
- Security, scalability, multi-user

**Result:**
A production-ready platform that's secure, scalable, and user-friendly! 🚴‍♂️

---

**Updated:** October 24, 2025  
**Status:** Tech stack analyzed and documented  
**Next:** Start building with this proven stack + improvements

---

*"Don't reinvent the wheel. Fix the brakes and add rocket boosters."* 🚀

