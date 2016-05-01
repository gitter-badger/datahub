# Data Broker

## What is a broker?

A broker acts as an independent intermediary between entities that are involved in a transaction of goods. In the case of a data broker, the broker facilitates exchange of information (data) between entities.

## Why this data broker?

The information being exchanged could be anything, but for this data broker it tends to be two types of data:

1. Transient message events; these have a short life-span and tend to be primarily of value at the actual time of transmission/reception.
2. Persistent data records; these have a longer life-span and are stored on the broker's filesystem while awaiting collection by other entities.

The idea behind using a data broker is that it allows you to abstract entity-specific details and exchange data in a consistent manner. For example, if you have a Devops environment with several different types of continuous integration build system (e.g. Jenkins, Buildbot, Teamcity) it can be useful to be able to send out build events and build artifacts in a standard manner regardless of which system produced the build. In fact designing any data exchange using such a system means that you could at any time decide to change the build system, without needing to make any change to other systems that rely on inter-operation with the CI systems.

## How would I use it?

The core of this data broker is the Message Queue, which runs on ZMQ. Events can be accessed via ZMQ or Websocket, and typically require authentication via a security token (more about the authentication scheme later). The ZMQ event system provides the "transient message events" facility of the data broker.

In addition to this, there is the capability to upload and download files ("persistent data records"). Files can be uploaded or downloaded via HTTP GET/POST - in future it might also be possible to just use plain old scp or rsync as well. As with the event system, security tokens are required to access these interfaces. When a file changes, a FILE UPDATED event is published to the events broker.

For the most part, the data broker is independent and impartial to the format of the data records uploaded to it. However some files are also validated before updates are accepted (for example, the 'broker_users.xml' that describes the users that can access the broker, along with their security tokens, SSL certificates, etc).

## What does it run on?

There are several components to the system:

1. Nginx - this provides a front-end for Websocket, HTTP, and TCP access to the internal systems. It allows limits to be placed on connection attempts, and as Nginx is very performant, it can tolerate a moderate level of DoS-type activity without failing.
2. The Event Broker - provides ZMQ and Websocket access.
3. The Web Server - provides HTTP GET/POST authentication and file validation.
4. The File Watcher - watches for changes to the filesystem and sends FILE UPDATED, FILE CREATED, and FILE DELETED events accordingly.

The servers (including the Broker, Web Server, and File Watcher) are written in Python. The code stays out of the way as much as possible, serving files and processing events using the underlying applications (e.g. Nginx) - primarily the job of the code is to handle authentication and validation, and that's it.

Python was chosen for expedience - the lxml implementation in Python is surprisingly fast and memory-efficient, and the Tornado HTTP and ZMQ implementations are also quite good, albeit lacking in scalability due to Python's inherent limitations. Above all else, Python is extremely easy to comprehend and very fast to get up and running. It is quite possible or likely that the relatively small amount of code required for these applications will later be rewritten in a more performant language, if Python proves to be any kind of bottleneck. If it doesn't, there is simply no good reason to bother with another language.

