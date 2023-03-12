Feature: Paints and Colours tab functionality

    Scenario: Navigate to colour catalogue
      Given I open the application url in the browser
      And I search colour catalogue in search
      When I click search
      And I see colour catalogue
      Then I can see various colours

    Scenario: Navigate to the interior textures
      Given I open the application url in the browser
      And I hover the mouse on paints and colours tab
      When I click the interior textures
      Then I should see interior textures

    Scenario: Navigate to Exterior textures and check filters
      Given I open the application url in the browser
      And I hover the mouse on paints and colours tab
      When I click the Exterior textures
      Then I can see various filters

    Scenario: Navigate to the exterior paints
      Given I open the application url in the browser
      And I hover the mouse on the paints and colours tab
      When I click the exterior paints
      Then I can see various paints

    Scenario: Navigate to the metal paints
      Given I open the application url in the browser
      And I hover the mouse on the paints and colours tab
      When I click the metal paints
      Then I can see various metal paints


