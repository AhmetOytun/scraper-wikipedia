from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    dict = {}
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://tr.wikipedia.org/wiki/G%C4%B1da_boyas%C4%B1#:~:text=Rengi%20ve%20di%C4%9Ferleri-,%C4%B0nsan%20sa%C4%9Fl%C4%B1%C4%9F%C4%B1%20%C3%BCzerindeki%20etkisi,oldu%C4%9Fuyla%20ilgili%20ortaya%20%C3%A7%C4%B1kan%20iddialard%C4%B1r.")
    table = page.locator("xpath=//*[@id='mw-content-text']/div[1]/table[1]/tbody")
    for row in table.locator("tr").all():
        cells = row.locator("th").all()
        if len(cells) == 0:
            continue
        dict[cells[0].inner_text()] = [cells[1].inner_text()]

    browser.close()

    # Save the dictionary to a text file

    with open("scraped_data.txt", "w", encoding="utf-8") as f:
        for key, value in dict.items():
            f.write(f"{key}: {value}\n")
