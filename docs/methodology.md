# Verification Methodology

## Core inclusion criterion

A project qualifies when it updates a component that can improve behavior on **future tasks or future runs**.

Accepted persistent improvement surfaces include:
- prompt or context,
- reusable memory or skills,
- harness/runtime behavior,
- workflow or agent program,
- multi-agent topology, roles, routing, or communication,
- policy/model parameters,
- reusable environment/procedural models.

## What is normally excluded

- ordinary chain-of-thought prompting,
- a retry loop that does not change persistent state,
- reflection that only repairs the current answer,
- benchmark-only repositories,
- paper-only methods without public code,
- projects where the claimed code relationship cannot be verified.

A particularly useful boundary test is:

> If the current task disappeared, would the system retain an improvement that changes how it handles a later task?

If no, the method is usually self-correction rather than persistent self-improvement.

## Code-release labels

### official
Use when the repository is owned by the authors, their lab/company, or is explicitly linked by the paper/project as the official/reference implementation.

### reference
Use when an official platform or associated repository implements the method but is broader than a minimal paper reproduction.

### third-party
Use for community reproductions that are not controlled by the original authors.

### official-borderline
Use for official code that is relevant to the area but does not clearly satisfy persistent cross-task self-improvement.

## Maintenance procedure

Every maintenance pass should:
1. Read upstream lists such as Awesome-Graph-Engineering for newly added self-evolution/harness papers.
2. Re-check every watchlist item for an author-owned or paper-linked repository.
3. Verify repository ownership and the paper↔code relationship.
4. Add only code that is public and materially usable.
5. Record the verification date.
6. Avoid silently upgrading a third-party implementation to official without evidence.
7. Keep failed/uncertain searches on the watchlist rather than guessing.
