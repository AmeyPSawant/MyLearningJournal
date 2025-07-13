# Databases
We can use databases to store data in an organized way.

## Amazon Relational Database Service (RDS)
It offers several database engines with many benefits such as  
- Automated patching  
- Backups  
- Redundancy  
- Failover  
- Disaster recovery  

## Amazon Aurora
It supports Postgre, MySQL, and distributed SQL databases, or DSQLs.

## Amazon DynamoDB
DynamoDB is a fully managed serverless NoSQL database.  
NoSQL means data is stored in a non-relational fashion instead of a relational database management system.
Data is stored as items, and items are a collection of attributes.  
Each attribute has a name and a value.  
An attribute value can be simpler types like a number or more complex ones like a set, or a document.  
You can also add or remove attributes at any time, and not every item in the table needs to have the same attributes.

## Amazon ElastiCache
ElastiCache is a fully managed in-memory caching service that was built to help reduce the complexity of administering in-memory caching systems.  
__Benefits__
- High performance for Redis, Valkey, or Memcached instances
- High availability
- Replication across multiple Availability Zones
- Data encryption

## Amazon DocumentDB
A specialized database service that helps manage data with complex, varied information that doesn't fit neatly into traditional spreadsheet-like tables.  
It's great for uses like content management, catalogs, and user profiles.

## Amazon Neptune
It's a graph database designed specifically to store and manage interconnected data, making it convenient to query social networking data to find relationships and patterns.  
It can be used to track a social network that identify who is connected to whom are very clunky to manage in a traditional relational database.

## Amazon Managed Blockchain
It is a service that helps you create and manage blockchain networks.
For example, A grocery store maintaining data on shipments from food suppliers to help ensure food safety.
