#!/bin/bash

echo "🔧 Fixing Playwright browser installation..."
echo "============================================="

# Fix the Playwright installation using Python module
echo "🎭 Installing Chromium browser..."
python -m playwright install chromium

# Install missing audio dependencies
echo "🔊 Installing audio dependencies..."
sudo apt-get install -y libasound2t64

# Install additional browser dependencies
echo "🖥️  Installing additional browser dependencies..."
sudo apt-get install -y \
    fonts-liberation \
    libappindicator3-1 \
    libasound2t64 \
    libatk-bridge2.0-0t64 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgtk-3-0t64 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    xdg-utils

# Test Playwright installation
echo "🧪 Testing Playwright installation..."
python -c "
import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://example.com')
        title = await page.title()
        await browser.close()
        print(f'✅ Browser test successful! Page title: {title}')

asyncio.run(test())
"

echo "✅ Playwright fix complete!"
echo "🚀 Now run: python google_bot.py"