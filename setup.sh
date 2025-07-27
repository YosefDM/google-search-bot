#!/bin/bash

echo "🚀 Setting up Google Search Bot in GitHub Codespaces..."
echo "=================================================="

# Update system packages
echo "📦 Updating system packages..."
sudo apt-get update -y

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

# Install Playwright browsers
echo "🎭 Installing Playwright browsers..."
playwright install chromium

# Install additional dependencies for headless browsing
echo "🖥️  Installing additional browser dependencies..."
sudo apt-get install -y \
    libnss3 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    libasound2

# Test proxy connection
echo "🌐 Testing Bright Data proxy connection..."
python test_proxy.py

echo "✅ Setup complete!"
echo ""
echo "🎯 To run the bot:"
echo "   python google_bot.py"
echo ""
echo "🔧 To test proxy only:"
echo "   python test_proxy.py"