# Todo list

This list should transition into github Issues, but for now it is convenient to work with this way.

* Filewatcher - listen to a particular path for a set of patterns, and raise ZMQ events on create/update/delete.
  * Build functional test to verify the file watching works
  * Build the actual file watcher
* HTTP server - listen for HTTP requests, require token authentication
  * Build functional test to verify HTTP GET operation
  * Build functional test to verify HTTP PUT operation
  * Test unauthenticated
* Event server - listen for ZMQ and websocket, broker ZMQ PUBSUB messages
  * Test ZMQ pub-sub
  * Test Websocket pub-sub
  * Test ZMQ-to-websocket pub-sub
  * Test websocket-to-ZMQ pub-sub
  * Test unauthenticated ZMQ
  * Test unauthenticated websocket




