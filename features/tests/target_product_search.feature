# Created by HP at 24.06.2024
Feature: Target.com search test
  # Enter feature description here

  Scenario: User can search for a product on target
    Given Open Target.com
      # used for pre-conditions
    When Search for coffee
    # used for actions - steps
    Then Search results for coffee are shown
    # used for expected result

  Scenario: User can search for a mug on target
    Given Open Target.com
      # corresponding code for this step is already created in .py file so no need to code it again
