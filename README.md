# Datahub

This application is designed to broker information between systems. The Datahub broker acts as an independent intermediary between entities that are involved in a transaction of information. The information is typically transient events or persistent data records, and the broker is not meant to get involved in the specifics of the information it is dealing with.
The information being exchanged could be anything, but for this data broker it tends to be two types of data:

1. Transient message events; these have a short life-span and tend to be primarily of value at the actual time of transmission/reception.
2. Persistent data records; these have a longer life-span and are stored on the broker's filesystem while awaiting collection by other entities.

The idea behind using this application is that it allows you to abstract entity-specific details and exchange data in a consistent manner. For example, if you have a Devops environment with several different types of continuous integration build system (e.g. Jenkins, Buildbot, Teamcity) it can be useful to be able to send out build events and build artifacts in a standard manner regardless of which system produced the build. In fact designing any data exchange using such a system means that you could at any time decide to change the build system, without needing to make any change to other systems that rely on inter-operation with the CI systems.

## More details

The core of this data broker is the Message Queue, which runs on ZMQ. Events can be accessed via ZMQ or Websocket, and typically require authentication via a security token (more about the authentication scheme later). The ZMQ event system provides the "transient message events" facility of the data broker.

In addition to this, there is the capability to upload and download files ("persistent data records"). Files can be uploaded or downloaded via HTTP GET/POST - in future it might also be possible to just use plain old scp or rsync as well. As with the event system, security tokens are required to access these interfaces. When a file changes, a FILE UPDATED event is published to the events broker.

For the most part, the data broker is independent and impartial to the format of the data records uploaded to it. However some files are also validated before updates are accepted (for example, the 'broker_users.xml' that describes the users that can access the broker, along with their security tokens, SSL certificates, etc).

There are several components to the code:

1. The Event Broker - provides ZMQ and Websocket access.
2. The Web Server - provides HTTP GET/POST authentication and file validation.
3. The File Watcher - watches for changes to the filesystem and sends FILE UPDATED, FILE CREATED, and FILE DELETED events accordingly.

In addition, a production deployment generally uses Nginx to front-end the sockets for ZMQ, Websocket, and HTTP.

The servers (including the Broker, Web Server, and File Watcher) are written in Python. The code stays out of the way as much as possible, serving files and processing events using the underlying applications (e.g. Nginx) - primarily the job of the code is to handle authentication and validation, and that's it.

Python was chosen for expedience - the lxml implementation in Python is surprisingly fast and memory-efficient, and the Tornado HTTP and ZMQ implementations are also quite good, albeit lacking in scalability due to Python's inherent limitations. Above all else, Python is extremely easy to comprehend and very fast to get up and running. It is quite possible or likely that the relatively small amount of code required for these applications will later be rewritten in a more performant language, if Python proves to be any kind of bottleneck. If it doesn't, there is simply no good reason to bother with another language.

## Getting Started

For development work, you will need Python 3.5.1 or newer. On Linux, it is highly recommended NOT to change the system Python 3 version but instead use a tool like [PyEnv](https://github.com/yyuu/pyenv) to install a local non-system version of Python).

Set up a virtualenv, clone the repository, and run (in the activated virtualenv):

  pip install -r requirements.txt

  setup.py install

You will need some development dependencies installed, notably the development package for lib0mq.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

* Python 3.5.1 or newer
* lib0mq-dev

## Running the tests

TBC: Explain how to run the automated tests for this system

### And coding style tests

TBC: Explain what these tests test and why

```
Give an example
```

## Deployment

To actually use the application, most of the time you probably want to install the Docker image that is being built based on releases of this code. The advantage of the Docker image is that everything is already there, and since the Datahub is intended to be largely configuration-less anyway, you can be up and running almost immediately.

In future, instructions for non-Docker install will be added.

## Built On

* Python 3.5
* pyzmq
* tornado
* lxml

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/dansdans/datahub/tags).

## Authors

* **Kriss Andsten** - *Concept* [kandsten](https://github.com/kandsten/)
* **Dan Sloan** - *Initial work on this implementation* - [dansdans](https://github.com/dansdans)

See also the list of [contributors](https://github.com/dansdans/datahub/contributors) who have participated in this project.

## License

This project is licensed under the ISC License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Kriss Andsten was the inspiration for this work, all credit to him for past work on a "same same but different" variation on this concept (while that wasn't used for this project, it demonstrated that such a thing like this could in fact be done).
* ZMQ is pretty awesome. Hat tip to all the folks that have contributed to making it so nice, and a particular shout-out to the pyzmq guys for their work on their exceptionally easy-to-use ZMQ Python package.
