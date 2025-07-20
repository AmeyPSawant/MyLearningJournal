# Compute in the cloud
EC2 are Virtaul Machines which share underlying physical host machine.
Multitenancy: Sharing underlying hardware b/w virtual machines.

## EC2 Configurations
OS - Windows/ Linux  
Internal Business Applications/ Web Apps/ Databases/ 3rd Party Software  

* Can be scaled vertically by addign more CPU and Memory.  
* Networking Aspect can be controlled.  
* Compute as a Service (_CaaS_).

## Types of EC2 Instances
* Compute Optimized  
Compute intensive tasks, gaming servers, high performance computing (_HPC_), Scientific modeling.  
* Memory Optimized  
Memory intensive tasks.  
* Accelerated Computing  
Floating point number calcualtions, graphic processing, data pattern matching, hardware accelaration.
* Storage Optimized  
High performance for locally stored data.  

## Interacting with AWS Services
* AWS Management Console (Good for initial learning)
* AWS Command Line Interface (_CLI_)  
Make API Calls using the terminal, can be used for automation through scripting.
* AWS Software Development Kit (_SDK_)  
Can help invoke CLI commands on Python

## Steps to create an EC2 Instance (From Console)
1) Select EC2 on Dashboard
2) Click Launch Instance button
3) Enter a name for the EC2 Instance
4) Select an Amazon Machine Image(_AMI_) such as Amazon Linux, macOS, Ubuntu, Windows, Red Hat, Debian, etc.
5) Select an Instance Type (_t2.micro), helps decide the computing power
6) Key pair login, used to decide how we login to the system, consists of 2 keys, public and private
7) Select Network Settings (Select Security Group)
8) Configure Storage
9) Click Launch Instance

The Amazon Linux AMI doesn't have a web server on creation and in order to create it we need to add a script in the advanced settings.

## EC2 Pricing
* On-Demand
* Savings Plans, best if commited to consistent amount of usage and can offer 72% off for a 1-year and 3-year term.
* Reserved Instances, for steady state use
* Spot Instances, for upto 90% off on On-Demand but AWS can claim the instances anytime with a 2 min warning
* Dedicated Hosts, best for security sensitive and licensing with regulatory needs.

## EC2 Scalability and Elasticity
* Scalability  
    * Scale Up - Add more power to the existing machines.  
    * Scale Out - Add more machines to the cluster spreading out in multiple AZ's.  (a.k.a. Horizontal Scaling)
* Elasticity  
The ability to scale resources up or down based on the real time demand.  
EC2 Auto Scaling, can help solve  


## Elastic Load Balancing (_ELB_)
Load Balancer takes a rquest and routes them to instances.  
ELB takes on the responsibility of scaling, maintaining and directing traffic to the backend.  
It decouples the architecture and spins up a new instance if required.  
ELB uses several routing methods - round robin, least connections, IP Hash, Least Response Time

## Messaging and Queuing
Messaging helps in keeping track of messages in a loosely coupled environment until they are ready to be processed.  
AWS achieves this using Amazon Simple Queue Service (_SQS_) and Amazon Simple Notification Service (_SNS_).
* Amazon SQS - Is a messaging queuing service that facilitates reliable communication between software components. In Amazon SQS, an application places messages into a queue, and a user or service retrieves the message, processes it, and then removes it from the queue.
* Amazon SNS - Amazon SNS is a publish-subscribe service that publishers use to send messages to subscribers through SNS topics.

