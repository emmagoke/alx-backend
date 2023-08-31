// This script connects the app to redis
import { createClient, print } from "redis";
import util from "util";

const client = createClient();

// onnecting to localhost on port 6379
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const redisGet = util.promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  // It should display a confirmation message using redis.print
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await redisGet(schoolName);
    console.log(value);
  } catch (err) {
    console.log(err);
  }
}

async function execute() {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");
}

client.on("connect", async () => {
  console.log("Redis client connected to the server");
  await execute();
});
