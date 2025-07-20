# Exploring Compute Services

## Types  of Services
* Unmanaged  
Responsible for setting up, securing, and maintaining the operating system, network configurations, and applications on your instances; Services like EC2
* Managed  
AWS handles much of the operational overhead; Services like ELB, SQS, SNS
* Fully-managed
Infrastructure is fully managed by AWS, so you can focus entirely on writing and deploying code; Services like Serverless, Lambda

## Introduction to Serverless Compute
Serverless - You cannot see or access the underlying infrastructure or instances hosting your application.

## AWS Lambda
Lambda is a serverless compute service that lets you run code without provisioning or managing servers.  
It manages underlying infrastructure and scales the resources based on the volume of requests.

#### How it works?
1) Upload code to Lambda, which uploads as a Lambda Function.
2) Configure your code to be triggered by AWS Services, mobile apps or HTTP Requests.
3) Code rus when an event occurs.
4) You are charged only for the compute time consumed.

## Containers and Orchestration on AWS
* Amazon Elastic Container Service (ECS)  
    * Streamlined and integrated 
    * Define some parameters
    * Fully managed service
* Amazon Elastic Kubernetes Service (EKS)
    * Open source platfrom
    * More complex
    * More control and flexibility
* Amazon Elastic Container Registry
    * Fully managed Docker Registry
    * Stores container images

## Other Compute Services
__AWS Elastic Beanstalk__  
Elastic Beanstalk is a fully managed service that streamlines the deployment, management, and scaling of web applications.  
Developers can upload their code, and Elastic Beanstalk automatically handles the provisioning of infrastructure, scaling, load balancing, and application health monitoring.

__AWS Batch__  
AWS Batch is a fully managed service that you can use to run batch computing workloads on AWS.  
It automatically schedules, manages, and scales compute resources for batch jobs, optimizing resource allocation based on job requirements.

__Lightsail__  
Amazon Lightsail is a cloud service offering virtual private servers (VPSs), storage, databases, and networking at a predictable monthly price.  

__Outposts__  
AWS Outposts is a fully managed hybrid cloud solution that extends AWS infrastructure and services to on-premises data centers.