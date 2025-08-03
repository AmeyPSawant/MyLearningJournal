# System Design Basic Concepts
## Glossary
1. [Client-Server Architecture](#client-server-architecture)
2. [IP Address](#ip-address)
3. [DNS](#dns)
4. [Proxy/Reverse Proxy](#proxy-reverse-proxy)
5. [Latency](#latency)
6. [HTTP/HTTPS](#http-https)
7. [APIs](#apis)
8. [Rest API](#rest-api)
9. [GraphQL](#graphql)
10. [Databases](#databases)
11. [SQL vs NoSQL](#sql-vs-nosql)
12. [Vertical Scaling](#vertical-scaling)
13. [Horizontal Scaling](#horizontal-scaling)
14. [Load Balancers](#load-balancers)
15. [Database Indexing](#database-indexing)
16. [Replication](#replication)
17. [Sharding](#sharding)
18. [Vertical Partitioning](#vertical-partitioning)
19. [Caching](#caching)
20. [Denormalization](#denormalization)
21. [CAP Theorem](#cap-theorem)
22. [Blob Storage](#blob-storage)
23. [CDN](#cdn)
24. [WebSockets](#websockets)
25. [Webhooks](#webhooks) 
26. [Microservices](#microservices)
27. [Message Queues](#message-queues)
28. [Rate Limiting](#rate-limiting)
29. [API Gateways](#api-gateways)
30. [Idempotency](#idempotency)


## Client-Server Architecture
A client server architecture comprises of a client and a server.  
Client could be a web browser or a mobile app.  
Server is a machine that runs continously waiting to handle any incoming requests.  
Client sends a request to store, retrieve or modify data on the server.  
Server then processes the request and sends a response back to the client.  

<img src ="client-server-architecture.png" height="300px"></img>

## IP Address
Computers identify each other on the internet using IP Addresses (they kind of act as phone numbers).  
Every publically deployed server has a unique IP addresses.(For example - 34.120.10.5)  
A client needs to send a request to that IP address.

## DNS (Domain Name System)
A DNS Server maps easy to remember domain names to thier corresponding IP Addresses.  
When a client sends a request it first goes through the DNS Server, fetches the IP Address and this IP address is then used to communicate with the actual server.

<img src ="dns.png" height="300px"></img>

## Proxy/Reverse Proxy
A proxy server (__on the client side__) acts as a middleman between the client and the server.  
When a client sends a request to the server, the proxy server processes the request and sends it to the actual server.  
The proxy server hides the actual IP Address of the Client keeping location and identity private.

<img src ="proxy.png" height="300px"></img>

A reverse proxy server (__on the server side__) takes the request from the client and forwards it to the respective server based on some predefined rules.  

<img src ="reverse-proxy.png" height="300px"></img>

## Latency
Latency is the round trip delay caused due to the distance between the server and client.  
It is directly proportional to the distance between the server and client.  
High latency can make applications feel slow and unresponsive.

## HTTP/HTTPS
## APIs
## Rest API
## GraphQL
## Databases
## SQL vs NoSQL
## Vertical Scaling
## Horizontal Scaling
## Load Balancers
## Database Indexing
## Replication
## Sharding
## Vertical Partitioning
## Caching
## Denormalization
## CAP Theorem
## Blob Storage
## CDN
## WebSockets
## Webhooks
## Microservices
## Message Queues
## Rate Limiting
## API Gateways
## Idempotency