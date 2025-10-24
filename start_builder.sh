#!/bin/bash

# LMNH-Builder Start Script
# Activates agent to build the platform

echo "🚴‍♂️ LMNH-Builder Starting..."
echo ""

# Check if in correct directory
if [ ! -d "agent" ]; then
    echo "❌ Error: Run this from /LMNH/ directory"
    exit 1
fi

# Check if venv exists
if [ ! -d "agent/venv" ]; then
    echo "📦 Setting up Python virtual environment..."
    cd agent
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd ..
    echo "✅ Environment ready"
fi

# Check if config exists
if [ ! -f "agent/lmnh_config.json" ]; then
    echo "❌ Error: agent/lmnh_config.json not found"
    echo "   Please configure your API keys first"
    exit 1
fi

echo ""
echo "📚 Agent configured to read these docs first:"
echo "   - AI-BUILDER-INSTRUCTIONS.md"
echo "   - All files in /system/"
echo ""
echo "🔒 Hard-coded rules:"
echo "   - Will NOT code without reading docs"
echo "   - Will NOT violate architecture patterns"
echo "   - Will NOT expose technical complexity"
echo "   - Will NOT skip security"
echo ""
echo "🚀 Starting LMNH-Builder agent..."
echo "   Listening in Slack for @LMNH-Builder mentions"
echo ""

# Start agent
cd agent
source venv/bin/activate
python run_agent.py

