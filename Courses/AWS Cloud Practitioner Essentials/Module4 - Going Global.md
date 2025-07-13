# Going Global

## Introduction to going global
There are number of factors that need to be considered while selecting AWS Regions such as customer deamdn and development cost.  
AWS has smaller footprint facilities called edge locations.  
Edge locations cache items like images, videos, and other resources, so that users can access the content they need with lower latency.  
AWS has services, such as CloudFormation, that you can use to help automate the deployment of your cloud resources.  
These services use infrastructure as code, or IaC, helping you achieve a consistent, reliable set up each time your business grows.

## Choosing AWS Regions
* __Compliance__  
Depending on the requirement such as Data must stay in London then select region closest to London.
* __Proximity__  
We should choose a region closest to the business needs as distant regions can cause latency, such as most customers are in London but the region selected is Virginai where the comapny is.
* __Feature Availability__  
Not all regions might have the features available required for the business needs.
* __Pricing__  
Some regions are more cost effective than other and each region has different number for pricing.

## Diving Deeper into AWS Global Infrastructure
We need to plan for long term stability and less or virtually no down time for your users.  
To build redundant architectures, you can __use multi-Region and multi-AZ resources__ so that in case of failure application can automatically switch over to the backup AZ.  
Amazon CloudFront is a content delivery network, and it’s designed to serve content as close to users as possible.  
Outposts is a content delivery network, and it’s designed to serve content as close to users as possible.

## Infrastructure and Automation
Manually transferring the setups from one region to another can be slow and error prone and this can be easily solved with the help of automation where IaC comes in.  
IaC acts a blueprint for the architecture and it can used to later build the infrastructure using other AWS tools. 
AWS CloudFormation is an IaC service that you can use to define a wide variety of AWS resources in a declarative way by creating text-based documents called CloudFormation templates.  
CloudFormation parses the template and then provisions all of the resources you defined, calling the needed AWS APIs in the background to make it all happen.  


