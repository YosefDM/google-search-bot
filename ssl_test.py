import asyncio
from playwright.async_api import async_playwright

async def test_ssl_with_proxy():
    """Test if SSL certificate issues are fixed with proxy"""
    print("🔐 Testing SSL fix with Bright Data proxy...")
    
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--disable-web-security',
                '--ignore-certificate-errors',
                '--ignore-ssl-errors',
                '--ignore-certificate-errors-spki-list',
                '--allow-running-insecure-content'
            ]
        )
        
        context = await browser.new_context(
            proxy={
                'server': 'http://brd.superproxy.io:33335',
                'username': 'brd-customer-hl_d44da890-zone-residential_proxy1-session-ssltest',
                'password': 'b0c5sshjhmx9'
            },
            ignore_https_errors=True,  # Key fix for SSL issues
            user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        
        page = await context.new_page()
        
        try:
            print("🌐 Testing Google.com with proxy + SSL fix...")
            await page.goto('https://www.google.com', wait_until='networkidle', timeout=30000)
            
            title = await page.title()
            url = page.url
            
            print(f"✅ SUCCESS! Page loaded successfully")
            print(f"📄 Title: {title}")
            print(f"🔗 URL: {url}")
            
            if 'sorry' in url.lower():
                print("⚠️  Landed on Google 'sorry' page (detection)")
                return False
            else:
                print("🎉 No detection! SSL fix worked!")
                return True
                
        except Exception as e:
            print(f"❌ SSL test failed: {str(e)}")
            return False
        finally:
            await browser.close()

if __name__ == "__main__":
    success = asyncio.run(test_ssl_with_proxy())
    
    if success:
        print("\n🚀 SSL FIX SUCCESSFUL!")
        print("✅ Ready to run: python google_bot.py")
    else:
        print("\n❌ SSL issues persist")
        print("🔧 May need additional proxy configuration")