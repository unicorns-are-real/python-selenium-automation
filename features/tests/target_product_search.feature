# Created by HP at 24.06.2024
Feature: Target.com search test
  # Enter feature description here

  Scenario: User can search for a product on target
    # scenario names should be unique
    Given Open Target.com
      # used for pre-conditions
    When Search for coffee
    # used for actions - steps
    Then Search results for coffee are shown
    Then Page url has search term coffee
    # used for expected result

  Scenario: User can search for a coffee mug on target
    Given Open Target.com
      # corresponding code for this step is already created in .py file so no need to code it again
    When Search for coffee mug
    Then Search results for coffee mug are shown
    Then Page url has search term coffee+mug

    Scenario Outline: User can search for a product on target
    Given Open Target.com
    When Search for <product>
    Then Search results for <expected_result> are shown
    Then Page url has search term <expected_part_url>
    Examples:
      |product     |expected_result   |expected_part_url
      |coffee      |coffee            |coffee
      |tea         |tea               |tea
      |coffee mug  |coffee mug        |coffee+mug

      