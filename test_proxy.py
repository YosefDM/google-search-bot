import urllib.request
import ssl
import urllib.error
import json

def test_bright_data_proxy():
    """Test Bright Data proxy connection in Codespaces"""
    print("🧪 Testing Bright Data Proxy in GitHub Codespaces")
    print("=" * 50)
    
    # Test without proxy first
    print("🔍 Getting Codespaces real IP...")
    try:
        response = urllib.request.urlopen('https://httpbin.org/ip', timeout=10)
        content = response.read().decode('utf-8')
        data = json.loads(content)
        real_ip = data['origin']
        print(f"✅ Codespaces IP: {real_ip}")
    except Exception as e:
        print(f"❌ Failed to get real IP: {str(e)}")
        return False
    
    # Test with proxy
    print("\n🌐 Testing with Bright Data proxy...")
    proxy = 'http://brd-customer-hl_d44da890-zone-residential_proxy1-session-test123:b0c5sshjhmx9@brd.superproxy.io:33335'
    
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({'https': proxy, 'http': proxy}),
        urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
    )
    
    try:
        response = opener.open('https://httpbin.org/ip', timeout=15)
        content = response.read().decode('utf-8')
        data = json.loads(content)
        proxy_ip = data['origin']
        
        print(f"✅ Proxy IP: {proxy_ip}")
        
        # Get location info
        try:
            geo_response = opener.open('https://geo.brdtest.com/mygeo.json', timeout=15)
            geo_content = geo_response.read().decode('utf-8')
            geo_data = json.loads(geo_content)
            city = geo_data.get('geo', {}).get('city', 'Unknown')
            state = geo_data.get('geo', {}).get('region_name', 'Unknown')
            isp = geo_data.get('asn', {}).get('org_name', 'Unknown')
            
            print(f"📍 Location: {city}, {state}")
            print(f"🏢 ISP: {isp}")
            
            if proxy_ip != real_ip:
                print("\n🎉 SUCCESS! Proxy is working and rotating IPs!")
                print("✅ Ready to run google_bot.py")
                return True
            else:
                print("\n⚠️  Proxy and real IP are the same")
                print("🔧 Check Bright Data account configuration")
                return False
                
        except Exception as e:
            print(f"⚠️  Geo test failed: {str(e)}")
            return False
            
    except Exception as e:
        print(f"❌ Proxy test failed: {str(e)}")
        print("🔧 Possible issues:")
        print("   - Bright Data account credit low")
        print("   - Zone 'residential_proxy1' not active")
        print("   - Network connectivity issues")
        return False

if __name__ == "__main__":
    success = test_bright_data_proxy()
    
    print("\n" + "=" * 50)
    if success:
        print("🚀 PROXY TEST PASSED!")
        print("Next step: python google_bot.py")
    else:
        print("❌ PROXY TEST FAILED!")
        print("Check your Bright Data configuration")
    print("=" * 50)