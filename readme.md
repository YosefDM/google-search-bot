# Google Search Bot - GitHub Codespaces Edition

🤖 **Human-like Google search automation** with **Bright Data proxy rotation** running in **GitHub Codespaces** to bypass local network filters.

## 🚀 Quick Start

### Step 1: Create GitHub Repository
1. **Fork this repository** or create new one
2. **Upload all files** from this project
3. **Make repository PUBLIC** (required for free Codespaces)

### Step 2: Open in Codespaces
1. **Click** the green "Code" button
2. **Select** "Codespaces" tab  
3. **Click** "Create codespace on main"
4. **Wait** for VS Code to load in browser

### Step 3: Run Setup
```bash
# Make setup script executable
chmod +x setup.sh

# Run setup (installs everything)
./setup.sh
```

### Step 4: Test Proxy
```bash
# Test Bright Data connection
python test_proxy.py
```

### Step 5: Run the Bot
```bash
# Start Google search automation
python google_bot.py
```

## 📁 File Structure

```
google-search-bot/
├── google_bot.py      # Main bot script
├── test_proxy.py      # Proxy connection test
├── setup.sh           # Installation script
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## ⚙️ Configuration

### Bright Data Settings
The bot is pre-configured with:
- **Endpoint**: `brd.superproxy.io:33335`
- **Username**: `brd-customer-hl_d44da890-zone-residential_proxy1-session-codespaces`
- **Password**: `b0c5sshjhmx9`

### Bot Behavior
- **Headless mode**: ON (required for Codespaces)
- **Search delay**: 90 seconds between searches
- **Anti-detection**: Advanced fingerprinting protection
- **Results**: Saves to `search_results.json`

## 🧪 Testing

### Test Proxy Only
```bash
python test_proxy.py
```

**Expected output:**
```
✅ Codespaces IP: 52.142.124.15
✅ Proxy IP: 198.51.100.5
📍 Location: Los Angeles, California
🏢 ISP: Comcast Cable
🎉 SUCCESS! Proxy is working and rotating IPs!
```

### Test Full Bot
```bash
python google_bot.py
```

**Expected output:**
```
🚀 Google Search Bot - GitHub Codespaces Edition
🎯 Running 4 searches with proxy rotation
🔧 Headless mode: ON (Codespaces environment)

🚀 Search 1/4
🌐 Using proxy session: codespaces
🔍 Searching for: 'weather forecast New York'
🍪 Accepted cookies
👤 Clicked 'Stay signed out'
📊 Search results loaded
   Found 12 results
🖱️  Clicking result 1
✅ Visited 2 links
✅ Completed: 'weather forecast New York'
```

## 🎯 Features

### Anti-Detection
- ✅ **Residential IP rotation** via Bright Data
- ✅ **Random user agents** and viewports
- ✅ **Human-like typing** with occasional typos
- ✅ **Natural scrolling** and mouse movements
- ✅ **Random delays** between actions
- ✅ **Cookie consent** handling
- ✅ **Google sign-in** dialog dismissal

### Search Automation
- ✅ **Multiple search queries** 
- ✅ **Result link clicking**
- ✅ **Page navigation** (back/forward)
- ✅ **Error handling** and recovery
- ✅ **Results logging** to JSON file

### Cloud Benefits
- ✅ **No local network filters** (bypasses TechloQ, etc.)
- ✅ **Different IP range** from your home
- ✅ **60 hours free** per month
- ✅ **Full Linux environment**
- ✅ **VS Code interface**

## 🔧 Troubleshooting

### Proxy Issues
```bash
# Check Bright Data account
# 1. Login to brightdata.com
# 2. Verify account has credit
# 3. Check zone 'residential_proxy1' is active
# 4. Ensure IP rotation is enabled
```

### Installation Issues
```bash
# Re-run setup if something failed
./setup.sh

# Or install manually
pip install playwright asyncio pysocks
playwright install chromium
```

### Search Failures
```bash
# Check search_results.json for errors
cat search_results.json

# Common issues:
# - Google detection (use longer delays)
# - Proxy rotation not working
# - Network connectivity issues
```

## 📊 Results

Results are automatically saved to `search_results.json`:

```json
[
  {
    "query": "weather forecast New York",
    "visited_links": [
      "https://weather.com/weather/today/l/...",
      "https://www.accuweather.com/en/us/..."
    ],
    "success": true,
    "timestamp": 1703123456.789
  }
]
```

## 🎛️ Customization

### Modify Search Queries
Edit `google_bot.py` line ~280:
```python
test_queries = [
    'your custom search 1',
    'your custom search 2',
    'your custom search 3'
]
```

### Change Delays
Edit `google_bot.py` line ~295:
```python
# Delay between searches (seconds)
delay_between_searches=120  # 2 minutes
```

### Add More Results Per Search
Edit `google_bot.py` line ~100:
```python
max_results = 5  # Click 5 results per search
```

## 💰 Costs

### GitHub Codespaces
- **Free tier**: 60 hours/month
- **Paid tier**: $0.18/hour after free limit

### Bright Data
- **Residential proxies**: ~$15/GB
- **Typical usage**: 1-5MB per search
- **Monthly estimate**: $20-50 for moderate use

## 🚨 Important Notes

### Legal Compliance
- ✅ **Respects robots.txt**
- ✅ **Uses reasonable delays**
- ✅ **Educational/research purposes**
- ⚠️ **Check Google's Terms of Service**
- ⚠️ **Use responsibly**

### Rate Limiting
- **Recommended**: 90+ second delays between searches
- **Maximum**: 20-30 searches per hour
- **Best practice**: Vary timing and patterns

### Account Security
- 🔒 **Keep proxy credentials secure**
- 🔒 **Don't share repository publicly** with real credentials
- 🔒 **Monitor Bright Data usage**

## 📞 Support

### Common Questions

**Q: Bot gets detected by Google**
A: Increase delays, check proxy rotation, verify residential IPs

**Q: Proxy not working**  
A: Check Bright Data account credit and zone status

**Q: Codespaces timeout**
A: Free tier has session limits, upgrade for longer sessions

**Q: Want to run locally**
A: Download files and run on machine without network filters

### Getting Help
1. **Check** `search_results.json` for error details
2. **Run** `python test_proxy.py` to verify proxy
3. **Monitor** Bright Data dashboard for usage/errors
4. **Update** proxy credentials if needed

---

## 🎉 Success Metrics

**Your bot is working correctly if:**
- ✅ Proxy test shows **different IPs**
- ✅ Google searches **complete without "sorry" pages**
- ✅ Results are **clicked and visited**
- ✅ JSON file contains **visited_links**
- ✅ **No TechloQ or network filter interference**

**Happy automating!** 🤖✨