// This script connects the app to redis
import { createClient, print } from "redis";

const client = createClient();

// onnecting to localhost on port 6379
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
  // It should display a confirmation message using redis.print
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, value) => {
    console.log(value);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
