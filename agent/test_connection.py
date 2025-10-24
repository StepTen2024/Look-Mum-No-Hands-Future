#!/usr/bin/env python3
"""
Quick test to verify LMNH-Builder can connect to Slack
"""
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Load config
with open('lmnh_config.json', 'r') as f:
    config = json.load(f)

print("🧪 Testing LMNH-Builder Connection...")
print("")

# Test Slack connection
print("1️⃣ Testing Slack connection...")
try:
    client = WebClient(token=config['slack_bot_token'])
    auth_response = client.auth_test()
    
    print(f"   ✅ Connected as: {auth_response['user']}")
    print(f"   ✅ Team: {auth_response['team']}")
    print(f"   ✅ Bot User ID: {auth_response['user_id']}")
    print("")
    
    bot_id = auth_response['user_id']
    
except SlackApiError as e:
    print(f"   ❌ Slack Error: {e.response['error']}")
    exit(1)

# Test channel access
print("2️⃣ Testing channel access...")
try:
    channel_id = config['slack_channel']
    channel_info = client.conversations_info(channel=channel_id)
    
    print(f"   ✅ Found channel: #{channel_info['channel']['name']}")
    print(f"   ✅ Channel ID: {channel_id}")
    
    # Check if bot is in channel
    members = client.conversations_members(channel=channel_id)
    if bot_id in members['members']:
        print(f"   ✅ Bot is a member of this channel")
    else:
        print(f"   ⚠️  Bot is NOT in the channel yet")
        print(f"      Run in Slack: /invite @LMNH-Builder")
    print("")
    
except SlackApiError as e:
    print(f"   ❌ Channel Error: {e.response['error']}")
    print(f"      Make sure bot has been invited to channel")
    exit(1)

# Send test message
print("3️⃣ Sending test message...")
try:
    response = client.chat_postMessage(
        channel=channel_id,
        text="🚴‍♂️ *LMNH-Builder*: Connection test successful! Ready to build with NO HANDS! 💪\n\nTag me with: `@LMNH-Builder task: Your task here`"
    )
    print(f"   ✅ Test message sent!")
    print(f"   ✅ Check Slack to see it!")
    print("")
    
except SlackApiError as e:
    print(f"   ❌ Message Error: {e.response['error']}")
    exit(1)

print("=" * 60)
print("✅ ALL TESTS PASSED!")
print("")
print("LMNH-Builder is configured and ready!")
print("")
print("Next steps:")
print("1. Go to Slack")
print("2. Find the test message in your channel")
print("3. Tag the bot: @LMNH-Builder task: Read all docs first")
print("4. Watch it respond!")
print("=" * 60)

