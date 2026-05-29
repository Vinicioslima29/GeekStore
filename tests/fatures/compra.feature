Feature: Compra de Produto

  Scenario: Compra com sucesso
    Given que existe um produto "teclado"
    When eu realizo a compra
    Then a compra deve ser aprovada