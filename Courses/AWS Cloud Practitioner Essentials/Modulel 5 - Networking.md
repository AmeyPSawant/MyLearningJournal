# Networking
Amazon Virtual Private Cloud (_VPC_) help us provision a logically isolated section of the AWS Cloud.
The resources can be Public or Private, Public-facing resources have access to the internet, whereas private resources do not have internet access.  

Subnets are chunks of IP addresses in your VPC that you can use to group resources together.

To allow traffic from public internet, Internet gateways are used to get in the VPC.  
Virtual Private Gateway can be used to create a VPN connection between a private network, like your on-premises data center or internal corporate network to your VPC.  
AWS Direct Connect lets you establish a completely private, dedicated fiber connection from your data center to AWS. It ensures both security and consistent high performance.  

## More ways to connect to AWS
* __AWS Client VPN__  
AWS Client VPN is a networking service you can use to connect your remote workers and on-premises networks to the cloud.
* __AWS Site-to-Site VPN__  
Site-to-Site VPN creates a secure connection between your data center or branch offices and your AWS Cloud resources.
* __AWS PrivateLink__  
AWS PrivateLink is a highly available, scalable technology that you can use to privately connect your VPC to services and resources as if they were in your VPC.
* __AWS Direct Connect__  
Direct Connect is a service that makes it possible for you to establish a dedicated private connection between your network and VPC in the AWS Cloud.

## Inside the VPC
The public subnets have access to the internet gateway, the private subnets do not.  
Packets are messages from the internet, and every packet that crosses the subnet boundaries gets checked against something called a network access control list(_network ACL_).  
__Security group__(Instance level security) are stateful(it remembers the state), and it can be modified to accept a type of network.  
It allows a specific traffic in and all traffic out of the VPC.
For example - The doorman at your building
__Network ACL__(Subnet Entry Level security) are stateless(it always checks), and the packets get verified at the gateway with Network ACL.  
It allows only the packets that are allowed in the Subnet and the incoming and outgoing rules can be different.
For example - The passport control officers  

## How packet travels within two instances in two different subnets
1) Packet from EC1 with Subnet1 exits the instance through the Security Group of EC1.
2) Before leaving the Subnet1 it gets verified by the Network ACL(if passed by outgoing rules) of Subnet1.
3) When arrived at Subnet2 it gets verified by the Network ACL(if passed by incoming rules) of Subnet2.
4) Before enetering the EC2 instance in Subnet2 it gets verified by the Security Group of EC2.
5) On the way back it exits the instance through the security group of EC2.
6) Before leaving the Subnet2 it gets verified by the Network ACL(if passed by outgoing rules) of Subnet2.
7) When arrived at Subnet1 it gets verified by the Network ACL(if passed by incoming rules) of Subnet1.
4) Before enetering the EC1 instance in Subnet1 it gets verified by the Security Group of EC1.
All of the above things happen simultaneously.  

## Security Group v/s Network ACL
<img src="SG vs Network ACL.png" alt="SG vs Network ACL" width="500px">

## Steps for creating the following Architecture
<img src="Network Architecture.png" alt="Network Architecture" width="500px" style="background:#FFF">

### 1. Create a VPC
* Search "VPC" in the AWS Management Console search bar
* Select "VPC" from results
* Click "Create VPC"
  * Resource to create: **VPC Only**
  * Name tag: `My VPC`
  * IPv4 CIDR block: `10.0.0.0/16`
  * Click "Create VPC"

### 2. Create Subnets
__Private Subnets__
* Navigate to **Subnets** in the left menu
* Click "Create subnet":
  * VPC ID: `My VPC`
  * Subnet 1:
    - Name: `Private-subnet-1`
    - AZ: `us-east-1a`
    - IPv4 CIDR: `10.0.1.0/24`
  * Subnet 2:
    - Name: `Private-subnet-2`
    - AZ: `us-east-1b` 
    - IPv4 CIDR: `10.0.2.0/24`
  * Click "Create subnet"

* Disable public IP assignment:
  * Select each private subnet
  * Actions → "Edit subnet settings"
  * Uncheck "Auto-assign public IPv4 address"
  * Click "Save"

__Public Subnets__
* Click "Create subnet":
  * VPC ID: `My VPC`
  * Subnet 1:
    - Name: `Public-subnet-1`
    - AZ: `us-east-1a`
    - IPv4 CIDR: `10.0.3.0/24`
  * Subnet 2:
    - Name: `Public-subnet-2`
    - AZ: `us-east-1b`
    - IPv4 CIDR: `10.0.4.0/24`
  * Click "Create subnet"

* Enable public IP assignment:
  * Select each public subnet
  * Actions → "Edit subnet settings"
  * Check "Auto-assign public IPv4 address"
  * Click "Save"

### 3. Create Internet Gateway
* Navigate to **Internet Gateways**
* Click "Create internet gateway":
  * Name: `my-ig`
  * Click "Create"
* Select the new IGW → Actions → "Attach to VPC"
  * Select `My VPC`
  * Click "Attach"

### 4. Configure Route Tables
* Navigate to **Route Tables**
* Create new route table:
  * Name: `public-route-table`
  * VPC: `My VPC`
  * Click "Create"

* Add internet route:
  * Select the new route table
  * "Routes" tab → "Edit routes"
  * Add route:
    - Destination: `0.0.0.0/0`
    - Target: `my-ig` (Internet Gateway)
  * Click "Save changes"

* Associate public subnets:
  * "Subnet Associations" tab → "Edit subnet associations"
  * Select both public subnets (`Public-subnet-1`, `Public-subnet-2`)
  * Click "Save associations"

### Notes
- Private subnets remain isolated from the internet
- Public subnets can now route traffic to/from the internet
- Default security groups are automatically created
- For production environments, consider:
  - Adding NAT gateways for private subnet internet access
  - Configuring Network ACLs
  - Setting up VPC Flow Logs


## Global Networking
* __Amazon Route53__  
Route 53 is a domain name service, or DNS.  
DNS acts as a translation service (translates website names into Internet Protocol, or IP addresses).  
Routing policies -
    * Latency-based routing
    * Geolocation DNS (routed based on location of the customer)
    * Weighted round robin

* __Amazon CloudFront__  
CloudFront is a content delivery network (CDN) service that delivers your content with faster loading times, cost savings, and reliability.

## When to use VPN vs Direct Connect
* **VPN**  
  - Use when you need a secure, flexible connection for remote access to your resources
  - Provides encrypted connectivity over the public internet
  - Ideal for hybrid cloud scenarios with moderate bandwidth needs

* **Direct Connect**  
  - Use when you need much higher bandwidth with a dedicated line
  - Provides a private, physical network connection between on-premises and AWS
  - Ideal for:
    - Large data transfers between on-premises network and AWS
    - Applications requiring consistent network performance
    - Scenarios needing reduced network costs for high-throughput