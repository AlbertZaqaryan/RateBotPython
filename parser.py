from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time


def parse_rate():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") # for Chrome >= 109

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url='https://www.rate.am/hy/armenian-dram-exchange-rates/banks')
        time.sleep(3)
        usd = driver.find_element(By.CSS_SELECTOR, 'body > div.px-4.md\:px-0 > main > div > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\:absolute.before\:inset-0.before\:pointer-events-none.before\:bottom-auto.before\:h-16.before\:border.before\:rounded-xl.before\:border-N40.before\:outline.before\:outline-\[0\.375rem\].before\:outline-white.before\:z-10.after\:z-10.after\:absolute.after\:inset-0.after\:top-\[4\.375rem\].after\:border.after\:border-N40.after\:rounded-xl.after\:pointer-events-none.after\:shadow-\[0px_4px_0px_8px_white\] > div.w-\[55\%\].grow.-mb-1.md\:w-\[60\%\].reg\:w-\[50\%\].relative.lg\:w-\[54\%\].bg-N30 > div > div.w-full.grow.bg-white > div.group.flex.items-center.h-10.bg-N30 > div:nth-child(1) > div:nth-child(2)').text
        euro = driver.find_element(By.CSS_SELECTOR, 'body > div.px-4.md\:px-0 > main > div > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\:absolute.before\:inset-0.before\:pointer-events-none.before\:bottom-auto.before\:h-16.before\:border.before\:rounded-xl.before\:border-N40.before\:outline.before\:outline-\[0\.375rem\].before\:outline-white.before\:z-10.after\:z-10.after\:absolute.after\:inset-0.after\:top-\[4\.375rem\].after\:border.after\:border-N40.after\:rounded-xl.after\:pointer-events-none.after\:shadow-\[0px_4px_0px_8px_white\] > div.w-\[55\%\].grow.-mb-1.md\:w-\[60\%\].reg\:w-\[50\%\].relative.lg\:w-\[54\%\].bg-N30 > div > div.w-full.grow.bg-white > div.group.flex.items-center.h-10.bg-N30 > div:nth-child(2) > div:nth-child(2)').text
        rub = driver.find_element(By.CSS_SELECTOR, 'body > div.px-4.md\:px-0 > main > div > div.w-full.overflow-auto.-mt-40.pt-40 > div.flex.cursor-default.grow.rounded-xl.relative.mb-1.before\:absolute.before\:inset-0.before\:pointer-events-none.before\:bottom-auto.before\:h-16.before\:border.before\:rounded-xl.before\:border-N40.before\:outline.before\:outline-\[0\.375rem\].before\:outline-white.before\:z-10.after\:z-10.after\:absolute.after\:inset-0.after\:top-\[4\.375rem\].after\:border.after\:border-N40.after\:rounded-xl.after\:pointer-events-none.after\:shadow-\[0px_4px_0px_8px_white\] > div.w-\[55\%\].grow.-mb-1.md\:w-\[60\%\].reg\:w-\[50\%\].relative.lg\:w-\[54\%\].bg-N30 > div > div.w-full.grow.bg-white > div.group.flex.items-center.h-10.bg-N30 > div:nth-child(3) > div:nth-child(2)').text
        return [float(usd), float(euro), float(rub)]
    except Exception as ex:
        return ex.__class__.__name__
    finally:
        driver.close()
        driver.quit()
