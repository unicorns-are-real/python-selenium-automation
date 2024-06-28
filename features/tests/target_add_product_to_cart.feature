# Created by HP at 28.06.2024
Feature: Add product to cart test
  # Enter feature description here

  Scenario: Verify user can add product to cart
    Given Open product page
    Then Verify product is correct
    When Click on add to cart button
    When Click on cart icon
    Then Check cart has individual item
