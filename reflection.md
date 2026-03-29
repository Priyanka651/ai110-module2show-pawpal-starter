# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

---

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.

The Owner class stores information about the pet owner, such as name, available time, and preferences. It also manages the pets owned by the user.

The Pet class represents individual pets and stores details like name, type, age, and health notes. Each pet can have multiple tasks associated with it.

The Task class represents specific pet care activities such as feeding, walking, or medication. It includes attributes like duration, priority, category, and completion status.

The Scheduler class is responsible for organizing and prioritizing tasks. It generates a daily plan based on task priority and available time.

---

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

During the design process, I initially considered adding extra classes such as DailyPlan. However, I simplified the design to focus on the four main classes: Owner, Pet, Task, and Scheduler, as required.

This change made the system easier to understand and implement while still meeting all project requirements. The relationships between Owner, Pet, and Task were kept simple, and the Scheduler handles task organization based on time and priority.

### Core Actions of the System

1. The user can enter basic information about the pet and owner, such as pet name, type, and preferences.

2. The user can add, edit, and manage pet care tasks like feeding, walking, medication, grooming, and playtime, including duration and priority.

3. The system generates a daily schedule based on available time, task priority, and constraints, and explains why the schedule was created in that way.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

---

The scheduler considers three main constraints: available time, task priority, and task completion status.

Available time is important because the owner may not have enough time to complete every task in one day. Task priority matters because more important care activities, such as feeding or medicine, should be selected before lower-priority tasks. The scheduler also skips tasks that are already completed.

I decided these constraints mattered most because they directly affect how a practical pet care schedule should be built. The system should choose the most important unfinished tasks while staying within the owner’s available time.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

One tradeoff my scheduler makes is that it always prioritizes higher-priority tasks, even if that means some lower-priority tasks that could also fit are not selected first.

This tradeoff is reasonable for this scenario because pet care often includes essential tasks, such as feeding, medicine, or urgent walks, that should be completed before less important activities. Choosing higher-priority tasks first makes the daily plan more useful and realistic.

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
---------
I used AI tools to help me understand the project requirements, design the system structure, and implement the code step by step.

AI was especially helpful for breaking down the problem into smaller steps, generating UML design ideas, and helping me write Python class structures and scheduling logic. It also helped me debug errors and understand how to connect my backend logic with the Streamlit UI.

The most helpful prompts were simple and specific questions, such as asking how to implement scheduling logic, how to structure classes, and how to fix errors step by step.
-------------------

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

--
There were times when I did not directly accept AI suggestions and instead reviewed the output carefully.

For example, when duplicate code blocks caused errors in the Streamlit app, I identified that the issue was due to repeated UI sections rather than blindly following suggestions. I verified the structure of the code and removed duplicate parts to fix the issue.

I evaluated AI suggestions by testing the code, checking for errors, and ensuring the solution matched the project requirements. This helped me better understand the system instead of just copying answers.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
--
I tested the core behaviors of the scheduler, including task sorting, time constraints, and skipping completed tasks.

I verified that tasks are sorted correctly based on priority, with higher-priority tasks selected first. I also tested that the scheduler does not exceed the available time when generating a daily plan. Additionally, I confirmed that tasks marked as completed are not included in the final schedule.

These tests were important because they ensure that the scheduling logic works correctly and produces a realistic and useful plan for the user.
---


**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---
I am confident that my scheduler works correctly for the main use cases, such as selecting tasks based on priority and available time.

If I had more time, I would test additional edge cases, such as when no tasks fit within the available time, when all tasks are already completed, and when multiple tasks have the same priority. I would also test scenarios with a large number of tasks to ensure the system performs efficiently.
----

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The part of this project I am most satisfied with is successfully connecting the backend logic with the Streamlit UI.

It was rewarding to see the full system working, where user inputs are taken from the interface, processed through the scheduling logic, and then displayed as a daily plan with an explanation. This helped me understand how frontend and backend components work together.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the system by allowing users to add multiple pets and dynamically manage tasks, such as editing or deleting them.

I would also enhance the scheduling logic to consider additional constraints, such as specific time slots or task dependencies, and improve the user interface to make it more interactive and user-friendly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned from this project is how to design a system step by step before jumping into coding.

Using AI as a guide helped me break down complex problems into smaller parts, but I also learned the importance of verifying and understanding the code rather than blindly using suggestions. This improved both my problem-solving skills and confidence in building applications.