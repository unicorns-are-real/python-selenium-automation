# Created by HP at 27.06.2024
Feature: Target.com - cart test


  Scenario: Verify "Your cart is empty" message is shown for empty cart
    Given Open target.com
    When Click on cart icon
    Then "Your cart is empty" message is shown
