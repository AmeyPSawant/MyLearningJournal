# Flow Orchestration Basics

## Meet Flow Orchestration

Flow Orchestration helps combine automated processes into a single workflow, and use Flow Orchestration’s no-code approach to create orchestrations and transform flows into steps that are organized by stages.  
Flow Orchestration also lets you combine multiple flows together and map out how each flow interacts with one another.

## Get to Know Flow Orchestration

### Orchestration Types

- Autolaunched Orchestration (No Trigger)
- Record-Triggered Orchestration

### Stages, Steps, and Flows

#### Stages

A stage groups related steps, organizing them into logical phases.  
Stages are executed sequentially, and only one stage in an orchestration can be in progress at a time.  
You configure the conditions that must be met for the stage to be considered complete.

#### Steps

Steps are grouped in stages and can be run sequentially or concurrently.  
Interactive steps require user intervention.  
Background steps require no user interaction.

#### Flows

What both step types have in common, regardless of whether they are interactive or background steps, is that they each require a flow to be specified in order to run.  
An interactive step runs a screen flow, while a background step runs an autolaunched flow.  
You can use an evaluation flow to set custom criteria for starting a step or to mark an interactive step complete.

## Build a Simple Orchestration

### Flow Orchestration to the Rescue

Flow Orchestration is a powerful tool for automating processes like case management.

### Orchestration Building Blocks

An orchestration consists of triggers (like a new case record), steps (background and interactive), decisions (to determine outcomes), and stages (to organize steps).  
These elements work together to automate processes like triaging, closing, or escalating cases.
