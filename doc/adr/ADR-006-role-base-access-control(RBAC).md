# ADR-006: Adopt Role-Based Access Control (RBAC)

- **Status:** Accepted
- **Date:** 2026-07-28

## Context

FUTMXStore is designed as a multi-role academic platform rather than a traditional online bookstore.

Different categories of users require different permissions and capabilities within the system.

For example:

- Students browse and purchase materials.
- Vendors publish and manage products.
- Course Representatives upload departmental resources.
- Lecturers publish academic materials.
- Administrators manage the entire platform.

Granting every authenticated user unrestricted access would violate the principle of least privilege and introduce significant security risks.

The application therefore requires a structured authorization model.

---

## Decision

FUTMXStore will implement **Role-Based Access Control (RBAC)**.

Permissions will be granted through assigned roles instead of being attached directly to individual users.

The initial system roles include:

- Student
- Vendor
- Lecturer
- Course Representative
- Administrator

Each role represents a collection of permissions that define what a user is allowed to do within the platform.

---

## Rationale

This decision was made for several reasons.

### Separation of Identity and Authorization

Authentication identifies **who the user is**.

Authorization determines **what the user is allowed to do**.

Separating these responsibilities keeps the architecture modular and easier to maintain.

### Principle of Least Privilege

Users should only have access to features necessary for their assigned responsibilities.

Restricting permissions reduces accidental misuse and improves system security.

### Maintainability

Managing permissions through roles is significantly easier than assigning permissions individually to every user.

When permissions change, only the role definition needs to be updated.

### Scalability

As FUTMXStore grows, new roles can be introduced without redesigning the authorization system.

Examples include:

- Alumni
- Teaching Assistant
- Library Staff
- Department Coordinator

### Consistency

Every user assigned the same role receives the same permissions, ensuring predictable system behavior.

---

## Consequences

### Positive

- Improved security.
- Centralized permission management.
- Easier maintenance.
- Scalable authorization architecture.
- Consistent user experience.

### Negative

- Additional database relationships.
- More complex authorization checks.
- Requires careful permission design.

The added complexity is justified by the increased flexibility and security.

---

## Alternatives Considered

### Direct User Permissions

Assigning permissions directly to individual users was considered.

Although this provides flexibility, it quickly becomes difficult to manage as the number of users grows.

Permission assignments become inconsistent and harder to audit.

For these reasons, this approach was rejected.

---

## Implementation Notes

Roles are stored independently from users.

Permissions are associated with roles.

Users receive permissions through their assigned roles.

Conceptually:

```text
User
   │
   ▼
Assigned Role(s)
   │
   ▼
Permissions
```

This design keeps authentication independent from authorization while allowing the permission system to evolve as the platform expands.

---

## Summary

Role-Based Access Control provides a secure, maintainable, and scalable authorization strategy for FUTMXStore.

By assigning permissions to roles instead of individual users, the platform remains flexible while adhering to established software architecture principles.

> **Architectural Principle:** Authenticate users, authorize roles, and grant permissions through those roles.