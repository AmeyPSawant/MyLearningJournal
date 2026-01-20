# Autolaunched and Scheduled Flows

## Get Started with Autolaunched Flows

### Autolaunched Flows Overview

Autolaunched flows are background processes that run without user interaction. Unlike other flow types, they are not triggered by schedules, record changes, or platform events, giving you more control over when they run. They are ideal for automations that need to be initiated manually or by external mechanisms.

### Running Autolaunched Flows

You can run Autolaunched flows using various mechanisms, such as custom buttons, Einstein AI conversations, subflows, or other automation tools like Apex code or API calls. These flows are versatile and can be triggered based on user judgment or external events.

### Identifying Autolaunched Flows

To find Autolaunched flows, use the All Flows list view in the Automation app or the Flows page in Setup. In Setup, adding the Trigger field to the list view helps differentiate true Autolaunched flows from other types like record-triggered or schedule-triggered flows.

### Key Features

Autolaunched flows are unique because they run without triggers or user interaction. They are perfect for scenarios where automation needs to be initiated manually or by external systems, making them a powerful tool in Salesforce automation.

## Build an Autolaunched Flow unit

### Automation That Runs with a Single Click

This unit introduces a scenario where support technicians need a way to clone specific details from closed cases without copying unnecessary information. The solution involves creating an autolaunched flow and a custom button to initiate it. This approach allows users to decide when to clone a case while automating the process of copying only the required fields.

### Create an Autolaunched Flow with Input Variables

To build the flow, you first identify the fields to clone (e.g., ID, Subject, Account ID, and Type). Then, you create input variables in the flow to pass these values. The flow includes a "Create Records" element to clone the case and a custom field to link the new case to the original one.

### Get the URL for the Flow

Once the flow is built, you retrieve its relative URL from the Flow Details page in Salesforce Setup. This URL is essential for creating a custom button that runs the flow.

### Create a Custom Button to Run the Flow

The final step is to create a custom button on the Case object. This button is configured to run the flow using its URL. While the button can launch the flow, additional steps are needed to pass record-specific information to the flow, which is covered in the next unit.
