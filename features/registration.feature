Feature: Registration feature

  Scenario Outline: Validating the registration feature
    Given I navigate to the url: "https://www.qa.way2automation.com/"
    When I validate the page title: Welcome to the Test Site
    And I enter the name as <name>
    And I enter the phone number as <phone_numer>
    And I enter the email as <email>
    And I enter the country as <country>
    And I enter the city as <city>
    And I enter the user name as <username>
    And I enter the password as <password>
    And I submit the registration form

    Examples:
      | name     |  phone_numer  |  email                      |  country |  city |  username   |  password   |
      | Mayuresh |  8927342      |  trainer@way2automation.com |  India  |  Pune |  md_ahirrao |  lsajdfksf  |