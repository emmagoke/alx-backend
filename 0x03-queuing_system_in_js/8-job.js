import { createQueue } from "kue";

const queueClient = createQueue();

export default function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error("Jobs is not an array");
  }
  for (const job in jobs) {
    const newJob = queueClient.create("push_notification_code_3", job);

    newJob
      .on("enqueue", () => {
        console.log(`Notification job created: ${newJob.id}`);
      })
      .on("complete", () => {
        console.log(`Notification job ${newJob.id} completed`);
      })
      .on("failed", (errorMessage) => {
        console.log(`Notification job ${newJob.id} failed: ${errorMessage}`);
      })
      .on("progress", (progress, _data) => {
        console.log(`Notification job ${newJob.id} ${progress}% complete`);
      });

    newJob.save();
  }
}
