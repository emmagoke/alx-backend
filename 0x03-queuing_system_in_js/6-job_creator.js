import { createQueue } from "kue";
const queue = createQueue();

const job = queue.create("push_notification_code", {
  phoneNumber: "07060248735",
  message: "Creating a queue with Kue, which is a job",
});
//   .save((err) => {
//     if (!err) {
//       console.log(`Notification job created: ${job.id}`);
//     }
//   });

job.on("enqueue", () => {
  console.log(`Notification job created: ${job.id}`);
});

// when the job is completes
job.on("complete", () => {
  console.log("Notification job completed");
});

// if job fails
job.on("failed attempt", () => {
  console.log("Notification job failed");
});

job.save();
