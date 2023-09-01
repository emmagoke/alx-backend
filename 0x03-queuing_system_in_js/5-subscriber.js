import { createClient } from "redis";

const client = createClient();

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.subscribe("holberton school channel");

// waiting to recieve message the channel holberton school channel
client.on("message", (err, message) => {
  console.log(message);
  if (message === "KILL_SERVER") {
    client.unsubscribe(), client.quit();
  }
});
