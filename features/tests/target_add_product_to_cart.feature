# Created by HP at 28.06.2024
Feature: Add product to cart test
  # Enter feature description here

  Scenario: Verify user can add product to cart
    Given Open Target.com
    When Search for coffee
    When Select a product
    Then Redirect to product page
    When Click on "Add to cart" button
    When Click "View cart & check out" in the side menu
    Then Check cart has individual item
