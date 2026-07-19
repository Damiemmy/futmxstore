# ADR-003: User Registration and Role Assignment Strategy

**Status:** Accepted

**Date:** 2026-07-19

## Title

Register Every New User as a Customer and Use an Approval Workflow for Elevated Roles

## Context

FutMxStore will eventually support multiple user roles:

* Customer
* Course Representative
* Lecturer
* Vendor
* Administrator

Allowing users to self-select privileged roles during registration introduces significant security risks and increases the complexity of the onboarding process.

The MVP goal is to provide students with secure access to academic materials while keeping registration simple, reliable, and easy to maintain.

## Decision

Every newly registered account will automatically receive the **Customer** role.

Users who wish to become:

* Course Representative
* Lecturer
* Vendor

must submit a role request after registration.

An administrator will review and approve the request before the user's active role changes.

## Alternatives Considered

### Option 1: Allow Users to Select Their Role During Registration

**Pros**

* Fewer onboarding steps.
* Simpler registration experience for privileged users.

**Cons**

* Users could falsely register as lecturers or administrators.
* Increases security risks.
* Requires immediate verification during registration.
* Introduces additional validation and approval complexity.

**Decision**

Rejected.

---

### Option 2: Register Everyone as Customer

**Pros**

* Secure by default.
* Simple registration process.
* Supports an approval workflow.
* Easier permission management.
* Aligns with MVP goals.
* Prevents privilege escalation.

**Cons**

* Users requesting elevated roles must wait for administrative approval.
* Requires a role request workflow in a future iteration.

**Decision**

Accepted.

## Consequences

### Positive

* Prevents unauthorized access to privileged functionality.
* Keeps authentication simple.
* Enables administrative verification.
* Provides a clean path for future role management.
* Follows the Principle of Least Privilege.

### Negative

* Additional workflow required for role requests.
* Elevated users cannot immediately access privileged features.

## Future Considerations

Version 1 will support a single active role per user.

If future business requirements require users to hold multiple concurrent roles, a dedicated role-assignment model can be introduced without replacing the authentication system.

## Rationale

Starting every user as a Customer provides a secure default while keeping the registration process straightforward.

It minimizes abuse, simplifies the authentication domain, and creates a scalable foundation for future role management.

This decision also follows FutMxStore's engineering principle:

> **Architect for the Future. Implement for the Present.**
