from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--headless")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

file_name = "id_products.txt"
output_file_name = "charvalues.txt"

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

            driver.find_element(
                "xpath", "//a[@href='#tab-specification']").click()

            value = driver.find_element(
                "xpath", "//td[contains(text(), 'Матеріал топки')]/following-sibling::td")
            value = value.text

            # Write the value to the file
            charvalue_file.write(f"{value}\n")
