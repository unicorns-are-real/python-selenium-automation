# Created by HP at 27.06.2024
Feature: Target.com - empty cart test
  verify 'your cart is empty' message is shown

  Scenario: Verify user can navigate to empty cart
    Given Open target.com
    When Click on cart icon
    Then "Your cart is empty" message is shown
