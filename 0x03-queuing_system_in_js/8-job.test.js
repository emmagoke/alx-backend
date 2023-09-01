import { expect } from "chai";
import sinon from "sinon";
import { createQueue } from "kue";
import createPushNotificationsJobs from "./8-job";

describe("createPushNotificationsJobs", () => {
  const spyConsole = sinon.spy(console);
  const queue = createQueue({});

  before(() => {
    queue.testMode.enter(true);
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("display a error message if jobs is not an array", () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, Map, queue)
    ).to.throw("Jobs is not an array");
  });

  it("process to jobs passed in an array", () => {
    expect(queue.testMode.jobs.length).to.equal(0);

    const jobs = [
      {
        phoneNumber: "4153818782",
        message: "This is the code 4321 to verify your account",
      },
      {
        phoneNumber: "4154318781",
        message: "This is the code 4562 to verify your account",
      },
    ];
  });

  createPushNotificationsJobs(jobs, queue);
  expect(queue.testMode.jobs.length).to.equal(2);
  expect(queue.jobs[0].data).to.deep.equal(jobs[0]);
  expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");

  queue.process("push_notification_code_3", () => {
    expect(
      spyConsole.log.calledWith(
        "Notification job created:",
        queue.testMode.jobs[0].id
      )
    ).to.be.true;

    done();
  });
});
