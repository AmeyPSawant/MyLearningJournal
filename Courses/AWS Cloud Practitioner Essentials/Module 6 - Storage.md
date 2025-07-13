# Storage
Data needs to be stored in appropriate storage solutions to organize it accordingly.

## AWS Services for Storage
* __Block Storage__  
Data is divided into pieces called blocks which makes it fast and more efficient to access.  
With block storage, data can be updated, block by block, meaning the whole file doesn't need to be changed every time you make an update.  
This makes it ideal for developers who work with applications or databases that need quick and frequent updates.  

* __Object Storage__  
It saves data in self-contained units a.k.a objects.  
Each of these objects includes the data, a unique ID, and metadata that makes it easy to organize and retrieve.  
This type of storage requires rewriting the entire object for every change.  
Objects are organized in flat structures called buckets and is best for files that don't change constantly, like videos, backups, or logs.

* __File Storage__  
File storage uses a hierarchical file system that can be shared by applications.  
It’s compatible with most systems, which means little or no code modification in most cases.  
File storage is ideal for applications that require shared access, like content management systems.

## Block Storage
* __Amazon EC2 Instance Store Volumes__  
Can be used when its okay to loose data like temporary testing of an application.  
It stores data on the connected hosts storage and when the EC2 instances is stopped and then resumed then it will start up on the different host where the data will not be present.

* __Amazon Elastik Block Store (_EBS_)__  
We can create virtual hard drives, which are EBS volumes, that can be attached to the EC2 instances.  
These are separate drives from the local instance store volumes, and they aren't tied directly to the host that your EC2 instance is running on.  
Data will persist b/w stops and starts of the instance and these volumes can be attached to the EC2 instances and applications can be configured to write to this volume.  
EBS offers different volume types that give you different levels of performance and offer different pricing.  
Performance for EBS volumes is measured in IOPs, or input/output per second.

## Amazon EBS Data Lifecycle
EBS Snapshot are point in time backups, which means that the backup is done at a specific moment—in time.  
They are also incremental meaning, after the first snapshot(data is copied in it entirety), all the other snapshots will only copy what has changed since the previous snapshot was taken.  
This approach makes subsequent snapshots faster and more storage-efficient, which translates to a significant reduction in cost compared to running a full backup every time.  
When you delete a snapshot, only the data unique to that snapshot is removed. Data referenced by other snapshots is preserved.

## Amazon S3 (Simple Storage Service)
Amazon S3 is a fully managed, highly-available object storage service for storing and retrieving any amount of data as objects.  
It offers 99.999999999 percent durability, meaning your data is highly protected against loss, and offers features like versioning, lifecycle management, and various storage classes to optimize costs.  
It has private access by default and can be configured using bucket policies.  
To provide temporary access, and to not set up long-term access policies, time-limited presigned URLs can be used.
Amazon S3 Access Points, simplify the process of creating unique access control policies for shared datasets, where managing different groups and their respective access might be complicated.

## Amazon S3 Storage Classes
* __S3 Standard__  
It’s a general-purpose storage class and gives you fast retrieval speeds and affordable storage costs and is great for data that you access regularly, like files for a dynamic website.
* __S3 Standard-Infrequent Access (_IA_)__  
It’s perfect for things like backup as its a more cost-effective choice, but at a lower storage cost.  
* __Glacier storage classes__  
    * **S3 Glacier Instant Retrieval**  
    Quick access when needed (millisecond retrieval) while optimizing costs - ideal for medical images, media files  
    * **S3 Glacier Flexible Retrieval**  
    Lower cost with retrievals in minutes to hours - good for backups, archives  
    * **S3 Glacier Deep Archive**  
    Lowest cost (12-hour retrieval) - perfect for compliance data, long-term preservation  

* __Single-AZ storage classes__  
    * **S3 Express One Zone**  
    Ultra-low latency for frequently accessed data (single AZ)  
    * **S3 One Zone-IA**  
    Lower-cost infrequent access (single AZ) with 40% cost savings vs standard IA  

* __Automated management features__  
    * **S3 Lifecycle Policies**  
    Rules to automatically transition/expire objects between storage classes  
    * **S3 Storage Class Analysis**  
    Analyzes access patterns to recommend optimal storage transitions  
    * **S3 Intelligent-Tiering**  
    Auto-moves data between 4 tiers (Frequent/Infrequent/Archive/Deep Archive) based on usage  

## S3 Lifecycle
* After 30 days of inaccessivity, the data from Amazon S3 Standard is moved to Amazon S3 Standard-IA.
* After 60 days of inaccessivity, the data from Amazon S3 Standard-IA is moved to Amazon S3 Glacier Instant Retrieval.
* After 365 days of inaccesivity, the data from Amazon S3 Glacier Instant Retrieval is deleted.  

## Amazon Elastic File System (_EFS_)
* Amazon EFS is a scalable, managed file system for shared access across multiple EC2 instances.
* Automatically scales storage capacity and handles replication without manual intervention.
* Supports cross-AZ access (unlike EBS which is AZ-bound) and auto-optimizes costs via lifecycle policies.
* Ideal for shared datasets (e.g., analytics) where multiple servers need concurrent file access.  

## Amazon FSx
Amazon FSx for Windows File Server provides fully managed shared storage built on Windows Server. It delivers a wide range of data access, data management, and administrative capabilities.  
Use cases include the following:
* Migrate Windows file servers to AWS.
* Accelerate hybrid workloads.
* Reduce SQL Server deployment cost.
* Streamline virtual desktops and streaming.

## AWS Storage Gateway
Storage Gateway is a hybrid cloud storage service that makes it possible to seamlessly integrate on-premises environments with AWS Cloud storage.  
You can use it to extend local storage to the cloud while maintaining low-latency access to frequently used data.
__Benefits include:__
* Seamless integration
* Improved data management
* Local caching
* Cost optimization

__Gateway Types__
* Amazon S3 File Gateway  
Amazon S3 File Gateway bridges  local environment with Amazon S3.  
It provides on-premises applications with access to virtually unlimited cloud storage through familiar file protocols.

* Volume Gateway  
With Volume Gateway, you create virtual storage volumes while maintaining local access to  data.  
It actsas a bridge between on-premises infrastructure and AWS Cloud storage by presenting cloud data as iSCSI volumes that can be mounted by existing applications.  

* Tape Gateway  
Tape Gateway makes it possible to replace physical tape infrastructure with virtual tape capabilities while benefitting from the durability and scalability of AWS Cloud storage.  
Tape Gateway provides an interface that works with existing tape backup software, making the transition from physical tapes to cloud storage seamless.

## Real life scenarios for Amazon Storage
__1. Coffee Shop Website: Amazon S3__
- **Service Used**: Amazon S3 (Static Website Hosting)
- **Why Selected**:
  - Simple setup for static assets (HTML, CSS, JavaScript)
  - Automatic scaling for unpredictable traffic
  - Cost-effective pay-as-you-go model
  - No server management required

__2. Fitness Center Mobile App: Amazon EBS__
- **Service Used**: Amazon EBS (Provisioned IOPS SSD Volumes)
- **Why Selected**:
  - Low-latency block storage for database operations
  - Supports rapid read/write transactions
  - High performance for mission-critical apps
  - Tight integration with EC2 instances

__3. Automotive Repair Knowledge Base: Amazon EFS__
- **Service Used**: Amazon EFS
- **Why Selected**:
  - Shared file system accessible across multiple locations
  - Automatic scaling for large media files (images, videos)
  - Low-latency access for real-time collaboration
  - Handles high throughput for media processing

## Key Takeaways
| Service | Best For | Key Advantage |
|---------|----------|--------------|
| **S3** | Static websites, object storage | Simple, scalable, cost-effective |
| **EBS** | Databases, EC2-attached storage | High-performance block storage |
| **EFS** | Shared file systems, media workflows | Multi-instance access, auto-scaling |