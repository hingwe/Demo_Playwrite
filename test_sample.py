


# # ---------------- Playwright Test Cases ----------------

# def test_google_search(page: Page):
#     # Navigate to Google
#     page.goto("https://www.google.com")
#     assert "Google" in page.title(), "Google homepage title is incorrect"
#     page.fill("textarea[name='q']", "Playwright Python")
#     page.keyboard.press("Enter")

#     # Wait for search results to load
#     page.wait_for_selector("text=Playwright")
#     assert "Playwright" in page.content(), "Search results do not contain 'Playwright'"


# def test_demo_website_workflow(page: Page):
#     # Step 1: Navigate to the demo website
#     page.goto("https://demo.playwright.dev/login")
#     assert "Login" in page.title(), "Login page title is incorrect"

#     # Step 2: Perform login
#     page.fill("input[name='username']", "admin")
#     page.fill("input[name='password']", "password")
#     page.click("button[type='submit']")

#     # Wait for navigation after login
#     page.wait_for_selector("text=Welcome")
#     assert "Welcome" in page.content(), "Login failed or Welcome message not found"

#     # Step 3: Navigate to the dashboard
#     page.click("a[href='/dashboard']")
#     page.wait_for_selector("text=Dashboard")
#     assert "Dashboard" in page.title(), "Failed to navigate to the Dashboard"

#     # Step 4: Interact with a table (e.g., sorting)
#     page.click("th[data-column='name']")  # Sort by name
#     page.wait_for_timeout(1000)  # Wait for sorting to complete

#     # Step 5: Perform a search in the dashboard
#     page.fill("input[placeholder='Search']", "Test Item")
#     page.wait_for_selector("text=Test Item")
#     assert "Test Item" in page.content(), "Search results do not contain 'Test Item'"

#     # Step 6: Log out
#     page.click("button#logout")
#     page.wait_for_selector("text=Login")
#     assert "Login" in page.title(), "Logout failed"


# def test_page_not_found(page: Page):
#     # Navigate to a non-existent page
#     page.goto("https://demo.playwright.dev/non-existent-page")
#     assert "404" in page.content(), "404 error page not displayed"


# def test_invalid_login(page: Page):
#     # Navigate to the login page
#     page.goto("https://demo.playwright.dev/login")

#     # Attempt login with invalid credentials
#     page.fill("input[name='username']", "invalid_user")
#     page.fill("input[name='password']", "invalid_password")
#     page.click("button[type='submit']")

#     # Assert that an error message is displayed
#     page.wait_for_selector("text=Invalid username or password")
#     assert "Invalid username or password" in page.content(), "Error message not displayed for invalid login"


# def test_logout_redirect(page: Page):
#     # Navigate to the demo website and log in
#     page.goto("https://demo.playwright.dev/login")
#     page.fill("input[name='username']", "admin")
#     page.fill("input[name='password']", "password")
#     page.click("button[type='submit']")
#     page.wait_for_selector("text=Welcome")

#     # Log out
#     page.click("button#logout")
#     page.wait_for_selector("text=Login")
#     assert "Login" in page.title(), "Logout did not redirect to the login page"


# def test_dashboard_search_no_results(page: Page):
#     # Navigate to the demo website and log in
#     page.goto("https://demo.playwright.dev/login")
#     page.fill("input[name='username']", "admin")
#     page.fill("input[name='password']", "password")
#     page.click("button[type='submit']")
#     page.wait_for_selector("text=Welcome")

#     # Navigate to the dashboard
#     page.click("a[href='/dashboard']")
#     page.wait_for_selector("text=Dashboard")

#     # Perform a search for a non-existent item
#     page.fill("input[placeholder='Search']", "NonExistentItem")
#     page.wait_for_timeout(1000)  # Wait for search results to update
#     assert "No results found" in page.content(), "No results message not displayed for non-existent item"


# # ---------------- Utility Functions ----------------

# def open_browser(url):
#     browser = webbrowser.get('chrome')
#     browser.open(url)


# def count_frequency(arr):
#     freq = {}
#     for num in arr:
#         freq[num] = freq.get(num, 0) + 1
#     print(freq)


# def count_frequency_string(s):
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#     print(char_count)


# def reverse_string():
#     b = "Sudama"
#     print(b[2::-1])  # Reverse first 3 characters
#     print(b[::-1])   # Reverse the entire string


# def find_missing_number(nums):
#     n = len(nums) + 1
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum


# def check_anagram(str1, str2):
#     if sorted(str1.lower()) == sorted(str2.lower()):
#         print("Strings are anagrams")
#     else:
#         print("Strings are not anagrams")

from playwright.sync_api import sync_playwright
############################################ Sample Playwright Test Case ###########################
def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        browser.close()



        
        
#################################################### Sample Playwright Test Case ###########################        
        

        
                
