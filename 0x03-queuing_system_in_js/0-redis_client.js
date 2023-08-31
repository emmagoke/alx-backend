// This script connects the app to redis
import { createClient } from "redis";

const client = createClient();

// onnecting to localhost on port 6379
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});
