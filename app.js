var tmi = require('tmi.js');

var options = {
	options: {
		debug: true
	},
	connection: {
		cluster: "aws",
		reconnect: true
	},
	identity: {
		username: "PunchBot",
		password: "oauth:orvnb4yp095akpasl7veswgibzoxnp"
	},
	channels: ["punchpunchtest"]
};

var client = new tmi.client(options);
client.connect();

client.on('chat', function(channel, user, message, self) {
	client.action("punchpunchtest", user['display-name'] + " you suck")
});

client.on('connected', function (address, port){
	client.action("punchpunchtest", "Hello Party people");
});