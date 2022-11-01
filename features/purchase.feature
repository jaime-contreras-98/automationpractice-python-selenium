Feature: Purchase/Search tests on automationpractice.com website.

  Scenario: Search for a product, then purchase that product
    Given I go to AutomationPractice website on Chrome
    When I search for a product on the searchbar
    And I add to cart that product
    Then My product must appear on the shopping cart