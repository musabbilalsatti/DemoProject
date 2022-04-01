Feature: Facebook login

  Scenario: Verify FB Login Functionality
    Given User is on Facebook login page
    When user enters valid email and password
    And click on login button
    Then verify user is loggedIn successfully