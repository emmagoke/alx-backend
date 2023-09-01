import { createQueue } from "kue";

const queue = createQueue();

const blackList = ["4153518780", "4153518781"];

function sendNotification(phoneNumber, message, job, done) {
  let total = 2,
    pending = 2;
  //   every 1 second check
  let interval = setInterval(() => {
    if (total - pending <= total / 2) {
      // job.progress(completed, total [, data]):
      // job.progress(frames, totalFrames);
      job.progress(total - pending, total);
    }
    if (blackList.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(interval);
      return;
    }
    if (total === pending) {
      console.log(
        `Sending notification to ${phoneNumber}, with message: ${message}`
      );
    }
    --pending || done();
    pending || clearInterval(interval);
  }, 1000);
}

// Processing 2 at a time
queue.process("push_notification_code_2", 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
