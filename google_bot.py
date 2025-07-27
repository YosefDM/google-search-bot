import asyncio
import random
import time
import json
from playwright.async_api import async_playwright
from typing import List, Dict

class CodespacesGoogleBot:
    def __init__(self):
        # Bright Data configuration for Codespaces
        self.bright_data_config = {
            'endpoint': 'brd.superproxy.io:33335',
            'username': 'brd-customer-hl_d44da890-zone-residential_proxy1-session-codespaces',
            'password': 'b0c5sshjhmx9'
        }
        
        # Linux-compatible user agents
        self.user_agents = [
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        ]
        
        self.viewports = [
            {'width': 1920, 'height': 1080},
            {'width': 1366, 'height': 768},
            {'width': 1440, 'height': 900}
        ]

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def get_random_viewport(self):
        return random.choice(self.viewports)

    def random_delay(self, min_ms: int, max_ms: int) -> float:
        return random.randint(min_ms, max_ms) / 1000.0

    async def create_browser_context(self, playwright):
        """Create browser context optimized for Codespaces"""
        
        browser = await playwright.chromium.launch(
            headless=True,  # Must be headless in Codespaces
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-features=VizDisplayCompositor',
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--disable-web-security',
                '--disable-features=site-per-process',
                '--remote-debugging-port=9222'
            ]
        )
        
        context_config = {
            'user_agent': self.get_random_user_agent(),
            'viewport': self.get_random_viewport(),
            'locale': random.choice(['en-US', 'en-GB', 'en-CA']),
            'timezone_id': random.choice(['America/New_York', 'America/Chicago', 'America/Los_Angeles']),
            'extra_http_headers': {
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Cache-Control': 'max-age=0',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none'
            }
        }
        
        # Add Bright Data proxy
        context_config['proxy'] = {
            'server': f"http://{self.bright_data_config['endpoint']}",
            'username': self.bright_data_config['username'],
            'password': self.bright_data_config['password']
        }
        
        print(f"🌐 Using proxy session: codespaces")
        
        context = await browser.new_context(**context_config)
        
        # Advanced anti-detection
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });
            
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
            
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5],
            });
            
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en'],
            });
        """)
        
        return browser, context

    async def handle_cookie_consent(self, page):
        """Handle Google's cookie consent dialog"""
        try:
            cookie_selectors = [
                'button:has-text("Accept all")',
                'button:has-text("I agree")', 
                'button:has-text("Accept")',
                '#L2AGLb',
                'div[role="button"]:has-text("Accept")'
            ]
            
            for selector in cookie_selectors:
                try:
                    await page.click(selector, timeout=3000)
                    print("🍪 Accepted cookies")
                    await asyncio.sleep(1)
                    return True
                except:
                    continue
        except:
            pass
        return False

    async def handle_google_signin_dialog(self, page):
        """Handle Google's 'Sign in to Google' dialog"""
        try:
            signin_dismiss_selectors = [
                'div[role="button"]:has-text("Stay signed out")',
                ':has-text("Stay signed out")',
                'button:has-text("Stay signed out")', 
                '.YrSbJc:has-text("Stay signed out")',
                ':has-text("No thanks")',
                ':has-text("Skip")'
            ]
            
            for selector in signin_dismiss_selectors:
                try:
                    await page.click(selector, timeout=3000)
                    print("👤 Clicked 'Stay signed out'")
                    await asyncio.sleep(1)
                    return True
                except:
                    continue
        except:
            pass
        return False

    async def human_scroll(self, page):
        """Simulate human scrolling"""
        scroll_steps = random.randint(2, 4)
        
        for _ in range(scroll_steps):
            scroll_amount = random.randint(100, 400)
            await page.evaluate(f"window.scrollBy(0, {scroll_amount})")
            await asyncio.sleep(self.random_delay(300, 800))

    async def human_type(self, page, selector: str, text: str):
        """Type with human-like patterns"""
        element = page.locator(selector)
        await element.fill('')
        
        for i, char in enumerate(text):
            await element.type(char)
            
            # Occasional typo
            if random.random() < 0.03 and i > 0:
                await asyncio.sleep(self.random_delay(100, 200))
                await element.press('Backspace')
                await asyncio.sleep(self.random_delay(50, 100))
                await element.type(char)
            
            await asyncio.sleep(self.random_delay(50, 150))

    async def perform_google_search(self, search_query: str, max_results: int = 3) -> List[str]:
        """Perform Google search with human-like behavior"""
        
        async with async_playwright() as playwright:
            browser, context = await self.create_browser_context(playwright)
            page = await context.new_page()
            
            visited_links = []
            
            try:
                print(f"\n🔍 Searching for: '{search_query}'")
                
                # Navigate to Google
                await page.goto('https://www.google.com', wait_until='networkidle', timeout=30000)
                
                # Handle cookies and sign-in
                await self.handle_cookie_consent(page)
                await self.handle_google_signin_dialog(page)
                
                # Find search box
                search_selectors = ['input[name="q"]', 'textarea[name="q"]', 'input[title="Search"]']
                
                search_element = None
                for selector in search_selectors:
                    try:
                        await page.wait_for_selector(selector, timeout=5000)
                        search_element = selector
                        break
                    except:
                        continue
                
                if not search_element:
                    raise Exception("Could not find search box")
                
                # Type search query
                await self.human_type(page, search_element, search_query)
                
                # Submit search
                await asyncio.sleep(self.random_delay(500, 1500))
                await page.press(search_element, 'Enter')
                
                # Wait for results
                await page.wait_for_selector('h3', timeout=15000)
                print("📊 Search results loaded")
                
                # Check for "sorry" page (detection)
                if 'sorry' in page.url.lower():
                    print("⚠️  Google detection page detected")
                    return []
                
                # Scroll to see results
                await self.human_scroll(page)
                
                # Get search results
                result_elements = await page.query_selector_all('h3')
                total_results = len(result_elements)
                print(f"   Found {total_results} results")
                
                if total_results == 0:
                    print("⚠️  No search results found")
                    return []
                
                # Visit some results
                results_to_visit = min(max_results, total_results, 3)
                
                for i in range(results_to_visit):
                    try:
                        random_index = random.randint(0, min(5, total_results - 1))
                        result_element = result_elements[random_index]
                        
                        # Try to click the result
                        await result_element.hover()
                        await asyncio.sleep(self.random_delay(200, 600))
                        
                        # Get URL before clicking
                        try:
                            parent = await result_element.query_selector('xpath=..')
                            link = await parent.query_selector('a')
                            if link:
                                href = await link.get_attribute('href')
                                if href and href.startswith('http'):
                                    visited_links.append(href)
                        except:
                            pass
                        
                        # Click the result
                        print(f"🖱️  Clicking result {i + 1}")
                        await result_element.click()
                        
                        # Wait on page
                        await asyncio.sleep(self.random_delay(2000, 4000))
                        
                        # Go back
                        await page.go_back()
                        await page.wait_for_selector('h3', timeout=10000)
                        await asyncio.sleep(self.random_delay(1000, 2000))
                        
                    except Exception as e:
                        print(f"⚠️  Error with result {i + 1}: {str(e)[:50]}")
                        continue
                
                print(f"✅ Visited {len(visited_links)} links")
                return visited_links
                
            except Exception as e:
                print(f"❌ Search failed: {str(e)}")
                return []
            
            finally:
                await page.close()
                await context.close()
                await browser.close()

    async def run_multiple_searches(self, queries: List[str], delay_between_searches: int = 60) -> List[Dict]:
        """Run multiple searches with delays"""
        results = []
        
        for i, query in enumerate(queries):
            print(f"\n🚀 Search {i + 1}/{len(queries)}")
            
            try:
                visited_links = await self.perform_google_search(query)
                results.append({
                    'query': query,
                    'visited_links': visited_links,
                    'success': len(visited_links) > 0,
                    'timestamp': time.time()
                })
                
                print(f"✅ Completed: '{query}'")
                
                # Delay between searches
                if i < len(queries) - 1:
                    delay = delay_between_searches + random.randint(-10, 20)
                    print(f"⏱️  Waiting {delay} seconds...")
                    await asyncio.sleep(delay)
                
            except Exception as e:
                results.append({
                    'query': query,
                    'error': str(e),
                    'success': False,
                    'timestamp': time.time()
                })
        
        return results

    def save_results(self, results: List[Dict], filename: str = 'search_results.json'):
        """Save results to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"💾 Results saved to {filename}")


# Main execution
async def main():
    print("🚀 Google Search Bot - GitHub Codespaces Edition")
    print("=" * 60)
    
    bot = CodespacesGoogleBot()
    
    # Test queries
    test_queries = [
        'weather forecast New York',
        'best pizza recipes',
        'Python programming tips',
        'latest tech news'
    ]
    
    print(f"🎯 Running {len(test_queries)} searches with proxy rotation")
    print("🔧 Headless mode: ON (Codespaces environment)")
    print("=" * 60)
    
    try:
        results = await bot.run_multiple_searches(test_queries, delay_between_searches=90)
        
        # Save results
        bot.save_results(results)
        
        # Summary
        successful = sum(1 for r in results if r['success'])
        print(f"\n📋 FINAL SUMMARY:")
        print(f"   Total searches: {len(results)}")
        print(f"   Successful: {successful}")
        print(f"   Failed: {len(results) - successful}")
        
        # Show visited links
        for result in results:
            if result['success'] and result['visited_links']:
                print(f"\n🔍 '{result['query']}':")
                for link in result['visited_links'][:3]:  # Show first 3
                    print(f"   📎 {link[:80]}...")
        
        if successful == len(results):
            print("\n🎉 ALL SEARCHES SUCCESSFUL!")
            print("✅ Your bot is working perfectly in Codespaces!")
        elif successful > 0:
            print(f"\n⚡ {successful}/{len(results)} searches successful")
            print("💡 Some detection occurred but proxy rotation is working")
        else:
            print("\n❌ All searches failed")
            print("🔧 Check proxy configuration and Bright Data account")
        
    except Exception as e:
        print(f"❌ Bot execution failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())