# Record-Triggered Flows

## Get Started with Triggered Flows

### Flow Types

There are three main types of flows:

- **Screen Flows:** Provide a user interface to guide users through a process, launched via quick actions, Lightning pages, or Experience Cloud sites.
- **Autolaunched Flows:** Run in the background without a user interface, triggered by other flows, Apex code, or REST API.
- **Triggered Flows:** Automatically launched by specific triggers like time, data changes, or platform events.

### Tools

Flow Builder is the go-to tool for creating triggered processes, combining the capabilities of Workflow Rules and Process Builder. It offers a graphical interface, debugging, and testing features, and is 10 times faster than Process Builder for record updates.

### Triggered Flows

Triggered flows consist of a trigger, criteria, and actions. Triggers can be based on schedules, record changes, or platform events. Actions include updating records, sending notifications, or initiating processes. Timing options like "Fast Field Update" and "Run Asynchronously" help optimize performance and avoid conflicts.

### Record-Triggered Flows

These flows are ideal for automating tasks based on record changes, such as updates, notifications, or maintaining data consistency. They can run during or after the record update, asynchronously, or on a scheduled path for future actions.

## Build a Record-Triggered Flow

### Business Requirement

This unit focuses on automating the creation of contracts for high-value opportunities marked as "Closed Won." The process involves defining a trigger (record creation or update), criteria (high-value and closed won), and an action (creating a draft contract).

### Planning and Configuring the Flow

Before building the flow, plan by answering key questions about its timing, purpose, and conditions. Use the Flow Builder to configure the start element by selecting the object (Opportunity), setting the trigger (record creation or update), and defining conditions (e.g., Stage equals "Closed Won" and Amount greater than 25,000).

### Creating a New Record

The flow creates a new Salesforce record (Contract) using values from the triggering opportunity. For example, the contract is associated with the opportunity's account, and its status is set to "Draft." This ensures the contract aligns with the business requirement.

### Saving and Debugging

Save the flow frequently and debug it to test different scenarios without affecting live data. Debugging involves running the flow against a sample opportunity to verify its functionality. Once successful, the flow is ready for activation.

## Add a Scheduled Task to Your Flow

### Automation on a Schedule

Record-triggered flows can be delayed using a scheduled path, allowing actions to occur minutes, hours, days, or even months after a record change. Scheduled paths can also be set relative to a specific field on the triggering record, such as a warranty expiration date or a case creation date.

### Business Requirement

The unit demonstrates how to expand an opportunity flow to remind the opportunity owner to follow up with the account owner five days after the opportunity closes. This is achieved by adding a scheduled path to the flow and creating a task for the opportunity owner.

### Configure Scheduled Paths

To configure a scheduled path, you must first ensure the Default Workflow User is set in your org. Then, within the flow, you can add a scheduled path, define the timing (e.g., 5 days after the close date), and specify the actions to take, such as creating a task.

### Debugging and Expanding the Flow

After configuring the flow, you can debug it to ensure it works as intended. The unit also encourages exploring additional criteria and actions, such as automating different actions for opportunities that don’t meet specific conditions.

## Meet Flow Trigger Explorer

### Overview of Flow Trigger Explorer

Flow Trigger Explorer is a visual and interactive tool for managing record-triggered flows. It allows you to view all flows associated with a specific object and trigger, reorder their execution, and manage flow details and versions. This tool simplifies navigation and organization of flows that run under similar conditions.

### Using Flow Trigger Explorer

You can access Flow Trigger Explorer from the Object Manager or the Flows page in Setup. It categorizes flows based on when they run (e.g., before save, after save, asynchronously) and provides options to reorder flows for better automation control. The tool also supports keyboard shortcuts for quick reordering.

### Monitoring Flows with Time-Based Automations

The Time-Based Automations page helps monitor scheduled flow actions, such as paths triggered by specific conditions. You can filter pending actions by criteria like object, scheduled date, or user, and cancel actions if needed.
