from selenium import webdriver

from selenium.webdriver.common.by import (
    By,
)

from selenium.webdriver.chrome.service import (
    Service,
)

from webdriver_manager.chrome import (
    ChromeDriverManager,
)

from selenium.webdriver.chrome.options import (
    Options,
)

import time


def test_purchase_flow():

    options = Options()

    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options,
    )

    driver.get(
        "http://127.0.0.1:8000"
    )

    produto = driver.find_element(
        By.ID,
        "produto"
    )

    cartao = driver.find_element(
        By.ID,
        "cartao"
    )

    cupom = driver.find_element(
        By.ID,
        "cupom"
    )

    produto.send_keys("teclado")

    cartao.send_keys("123")

    cupom.send_keys("GEEK20")

    botao = driver.find_element(
        By.TAG_NAME,
        "button"
    )

    botao.click()

    time.sleep(2)

    resultado = driver.find_element(
        By.ID,
        "resultado"
    )

    assert (
        "Compra aprovada!"
        in resultado.text
    )

    driver.quit()