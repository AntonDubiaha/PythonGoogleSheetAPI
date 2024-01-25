from writetosheetfunc import update_spreadsheet
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

file_name = "id_products.txt"
output_file_name = "charvalues2.txt"

# Text for xpath
xpath_text = "Тип обігріву"

with open(output_file_name, "w", encoding="utf-8") as charvalue_file:
    with open(file_name, "r") as file:
        # Read product IDs from the file
        for product_id in file:
            # Ensure that product_id doesn't contain any extra characters,
            # such as spaces or newline characters
            product_id = product_id.strip()

            # Formulate the link using the product ID and open the page
            url = f"https://teplokram.com.ua/index.php?route=product/product&product_id={product_id}"

            driver.get(url)

            try:
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.presence_of_element_located(("xpath", "//a[@href='#tab-specification']")))

                # Attempt to click on the specified element
                element.click()

                # Dynamically update XPath with the search text
                dynamic_xpath = f"//td[contains(text(), '{xpath_text}')]/following-sibling::td"
                value = driver.find_element("xpath", dynamic_xpath).text

            except TimeoutException:
                # Handle the case where the element is not found within the specified time (timeout)
                value = "Error with click"

            except Exception as e:
                # Handle the case where the element is not found
                if "no such element" in str(e).lower():
                    if "href='#tab-specification'" in str(e).lower():
                        value = "Error with click"
                    elif xpath_text in str(e):
                        value = "Element is absent"
                else:
                    # Handle other exceptions if needed
                    raise RuntimeError("Unknown error")

            # Write the value to the file
            charvalue_file.write(f"{value}\n")

update_spreadsheet("charvalues2.txt", "J", 3, "Печи, буржуйки, булерьяны")
