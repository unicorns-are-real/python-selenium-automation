# Created by HP at 27.06.2024
Feature: Logged out user sign in page
  # Enter feature description here

  Scenario: Logged out user can navigate to sigh in form
    Given Open Target.com
    When Click on Sigh in icon
    When Click Sign in field in the side menu
    Then "Sign in with password" button is present