# Security

Two crucial security components that needs to be known are  
*  __Authentication__ is the process of verifying the identity of a user or entity through credentials like a username and password combination.
* __Authorization__ determines which actions users are permitted to perform in a system or application.
For example - Authentication permits me to log in to our employee portal. But authorization limits me to just the areas that I'm allowed to access, such as my own employee records.  

AWS account root user, you can access and control any resource in the account.
To enhance the security it is recommended to have a strong password with root user and then MFA enabled.  

## AWS IAM
AWS Identity and Access Management can be used to create granular level control access to AWS resources.  
By default when a new IAM user is created, they have absolutely zero permissions.  
User permission needs to explicitily granted.  
Using least privilege principle, access can be given only to what is needed.
Permissions are granted or denied by associating an IAM policy (a JSON document specifying allowed or denied API calls) with an IAM user.  


## Network Security
Security groups operate at the AWS network level, not at the EC2 instance level, like an operating system firewall might.  
AWS Shield Standard can be used to enhance security and it is built into AWS managed services like Elastic Load Balancing, CloudFront, and Route 53 at no extra cost.  
AWS Shield can be combined with AWS Web Application Firewall, or WAF, to further protect your environment.  


## Detecting and Responding to Security Incidents
- **Amazon Inspector** - Automated vulnerability scanning.  
- **Amazon GuardDuty** - Threat detection (malicious activity, anomalies).  
- **Amazon Detective** - Root cause investigation using logs & analytics.  
- **AWS Security Hub** - Unified dashboard for security alerts.  
 
