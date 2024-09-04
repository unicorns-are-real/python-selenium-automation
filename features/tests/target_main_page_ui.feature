# Created by HP at 29.06.2024
Feature: Tests for main page UI
  # Enter feature description here

  Scenario: Verify header is shown
    Given Open Target.com
    Then Header is shown

  Scenario: Verify header has 5 links
    Given Open Target.com
    Then Header has 5 of links