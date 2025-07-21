# Migrating to the AWS Cloud

## Three phases of Migration process
* Pre-migration Assessment tools - Migration Evaluator to evaluate the migration process
* Migration tools - AWS Application Discovery Service and AWS Migration Hub
* Migration tools - AWS Application Migration Service and AWS Database Migration Service
* Data Transfer tools - AWS DataSync, AWS Transfer Family, AWS Snow Family

## AWS Cloud Adoption Framework (_CAF_)
The AWS CAF is a framework that brings AWS experience and best practices to companies preparing to migrate to the AWS Cloud.  
Six areas CAF is divided into are
* __Business__  
The Business perspective makes sure that IT aligns with business needs and that IT investments link to key business results.  
* __People__  
The People perspective supports development of an organization-wide change management strategy for successful cloud adoption.  
* __Governance__  
The Governance perspective focuses on skills and processes to align IT strategy with business strategy. This perspective helps you maximize business value and minimize risks.  
* __Platform__  
The Platform perspective includes principles and patterns for implementing new solutions in the cloud and migrating on-premises workloads to the cloud.  
* __Security__  
The Security perspective makes sure that the organization meets security objectives for visibility, auditability, control, and agility.  
* __Operations__  
The Operations perspective helps you to enable, run, use, operate, and recover IT workloads to the level agreed upon with your business stakeholders.  

## 7R's of Cloud Migration
* __Rehost__  
Also called as lift and shift.
* __Relocate__  
Relocating is changing the hosting location to the cloud. 
* __Replatform__  
Lift, tinker and shift.
* __Refactor__  
Refactoring, also known as re-architecting, involves reimagining how an application is architected and developed by using features built for the cloud.
* __Repurchase__  
Repurchasing involves moving from a traditional license to a software-as-a-service (SaaS) model.
* __Retain__  
Retaining consists of keeping applications that are critical for the business in the source environment. 
* __Retire__  
Retiring is the process of removing applications that are no longer needed.

## Migration services and tools
1. **AWS Application Discovery Service**  
Automatically maps your on-premises apps and infrastructure for migration planning.  
2. **AWS Application Migration Service**  
"Lift-and-shift" tool that replatforms apps to AWS with minimal downtime.  
3. **Migration Evaluator**  
Calculates cost projections and savings for cloud migration.  
4. **AWS Migration Hub**  
Central dashboard to track all migration progress across AWS tools. 

## Database Migrations
* __AWS Database Migration Service (_DMS_)__  
    - Migrates databases to AWS (SQL/NoSQL/warehouses)  
    - Minimal downtime with continuous replication  
    - Supports cross-region/availability zone copies  

* __AWS Schema Conversion Tool (_SCT_)__  
    - Converts schemas between different database engines  
    - Automates code conversion with manual review options  

* __Key Benefits__  
    - Faster than manual migration (weeks → days)  
    - Cost-effective & secure  
    - Enables database modernization  